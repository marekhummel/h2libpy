from ctypes import c_uint
from typing import List, Union

import h2libpy.data.matrix as mat
import h2libpy.data.misc as misc
import h2libpy.data.vector as vec
import h2libpy.lib.amatrix as libamatrix
import h2libpy.lib.clusterbasis as libclusterbasis
import h2libpy.lib.h2matrix as libh2matrix
import h2libpy.lib.sparsematrix as libsparsematrix
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import (cptr_to_list, pylist_to_ptr, try_wrap,
                               verify_type)
from h2libpy.lib.settings import field


class AMatrix(StructWrapper, cstruct=libamatrix.CStructAMatrix):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, rows: int, cols: int, *,
            fill: 'mat.FillType' = mat.FillType.Nothing):
        if fill == mat.FillType.Zeros:
            return cls(libamatrix.new_zero_amatrix(rows, cols))
        elif fill == mat.FillType.Identity:
            return cls(libamatrix.new_identity_amatrix(rows, cols))
        else:  # fill == mat.FillType.Nothing
            return cls(libamatrix.new_amatrix(rows, cols))

    @classmethod
    def from_submatrix(cls, src: 'AMatrix', rows: int, cols: int,
                       roff: int, coff: int):
        return cls(libamatrix.new_sub_amatrix(src, rows, roff, cols, coff))

    @classmethod
    def from_list(cls, elems: List[float], rows: int, cols: int):
        assert len(elems) == rows * cols
        celems = pylist_to_ptr(elems, field)
        obj = libamatrix.new_pointer_amatrix(celems, rows, cols)
        return cls(obj, refs=[celems])

    # ***** Properties *****

    def __getter_a(self) -> List[float]:
        last_coeff = (self.rows - 1) + (self.cols - 1) * self.ld
        coeffs = cptr_to_list(self.cobj().a, last_coeff + 1)
        return [[coeffs[i + j * self.ld] for i in range(self.rows)]
                for j in range(self.cols)]

    def __getter_ld(self) -> int:
        return self.cobj().ld

    def __getter_rows(self) -> int:
        return self.cobj().rows

    def __getter_cols(self) -> int:
        return self.cobj().cols

    # ***** Methods ******

    def resize(self, rows: int, cols: int, *, copy: bool = False):
        if copy:
            libamatrix.resizecopy_amatrix(self, rows, cols)
        else:
            libamatrix.resize_amatrix(self, rows, cols)

    def size(self, *, heaponly: bool = False):
        if heaponly:
            return libamatrix.getsize_heap_amatrix(self)
        else:
            return libamatrix.getsize_amatrix(self)

    def clear(self, *, clear_type: 'mat.ClearType' = mat.ClearType.All):
        if clear_type == mat.ClearType.Lower:
            libamatrix.clear_lower_amatrix(self, False)
        elif clear_type == mat.ClearType.LowerStrict:
            libamatrix.clear_lower_amatrix(self, True)
        elif clear_type == mat.ClearType.Upper:
            libamatrix.clear_upper_amatrix(self, False)
        elif clear_type == mat.ClearType.UpperStrict:
            libamatrix.clear_upper_amatrix(self, True)
        else:  # clear_type == mat.ClearType.All:
            libamatrix.clear_amatrix(self)

    def identity(self):
        libamatrix.identity_amatrix(self)

    def rand(self, *, ensure_self_adjoint: bool = False):
        if ensure_self_adjoint:
            libamatrix.random_selfadjoint_amatrix(self)
        else:
            libamatrix.random_amatrix(self)

    def rand_invert(self, alpha: float, *, ensure_pos_def: bool = False):
        if ensure_pos_def:
            libamatrix.random_spd_amatrix(self, alpha)
        else:
            libamatrix.random_invertible_amatrix(self, alpha)

    def copy(self, target: 'AMatrix', trans: bool = False, *,
             pivots: List[int] = None):
        if pivots:
            cpivots = pylist_to_ptr(pivots, c_uint)
            libamatrix.copy_colpiv_amatrix(trans, self, cpivots, target)
        else:
            libamatrix.copy_amatrix(trans, self, target)

    def clone(self) -> 'AMatrix':
        return try_wrap(libamatrix.clone_amatrix(self), AMatrix)

    def print(self, *, matlab: bool = False):
        if matlab:
            libamatrix.print_matlab_amatrix(self)
        else:
            libamatrix.print_amatrix(self)

    def is_isometric(self, trans: bool = False) -> float:
        return libamatrix.check_ortho_amatrix(trans, self)

    def scale(self, alpha: float):
        libamatrix.scale_amatrix(alpha, self)

    def conjugate(self):
        libamatrix.conjugate_amatrix(self)

    def dot(self, other: 'AMatrix') -> float:
        return libamatrix.dotprod_amatrix(self, other)

    def norm(self, *, ntype: 'mat.NormType' = mat.NormType.Spectral):
        if ntype == mat.NormType.Frobenius:
            return libamatrix.normfrob_amatrix(self)
        elif ntype == mat.NormType.SquaredFrobenius:
            return libamatrix.normfrob2_amatrix(self)
        else:  # ntype == mat.NormType.Spectral
            return libamatrix.norm2_amatrix(self)

    def norm2_diff(self, other: 'AMatrix') -> float:
        return libamatrix.norm2diff_amatrix(self, other)

    def add(self, other: Union['AMatrix', 'mat.SparseMatrix'],
            alpha: float = 1.0, trans: bool = False):
        if isinstance(other, AMatrix):
            libamatrix.add_amatrix(alpha, trans, other, self)
        elif isinstance(other, mat.SparseMatrix):
            libsparsematrix.add_sparsematrix_amatrix(alpha, trans, other, self)
        else:
            raise ValueError('AMatrix or SparseMatrix expected.')

    def addmul(self, alpha: float, a: 'AMatrix', b: 'AMatrix',
               trans_a: bool, trans_b: bool):
        libamatrix.addmul_amatrix(alpha, trans_a, a, trans_b, b, self)

    def bidiagmul(self, alpha: float, trans: bool,
                  dia: 'vec.AVector', lo: 'vec.AVector'):
        libamatrix.bidiagmul_amatrix(alpha, trans, self, dia, lo)

    # ---------

    def fastaddmul_h2matrix_amatrix_amatrix(self, alpha: float, trans: bool,
                                            a: 'mat.H2Matrix',
                                            b: 'mat.AMatrix'):
        func = libh2matrix.fastaddmul_h2matrix_amatrix_amatrix
        func(alpha, trans, a, b, self)

    def addmul_h2matrix_amatrix_amatrix(self, alpha: float,
                                        a: 'mat.H2Matrix', b: 'mat.AMatrix',
                                        trans_a: bool, trans_b: bool):
        func = libh2matrix.addmul_h2matrix_amatrix_amatrix
        func(alpha, trans_a, a, trans_b, b, self)

    def addmul_amatrix_h2matrix_amatrix(
            self, alpha: float, a: 'AMatrix', b: 'mat.H2Matrix',
            trans_a: bool, trans_b: bool):
        func = libh2matrix.addmul_amatrix_h2matrix_amatrix
        func(alpha, trans_a, a, trans_b, b, self)

    def collectdense(self, a: 'AMatrix', rb: 'misc.ClusterBasis',
                     cb: 'misc.ClusterBasis'):
        libh2matrix.collectdense_h2matrix(a, rb, cb, self)

    # -------

    def compress_clusterbasis_amatrix(self, cb: 'misc.ClusterBasis',
                                      src: 'AMatrix'):
        libclusterbasis.compress_clusterbasis_amatrix(cb, src, self)

    def compress_parallel_clusterbasis_amatrix(self, cb: 'misc.ClusterBasis',
                                               src: 'AMatrix', pardepth: int):
        func = libclusterbasis.compress_parallel_clusterbasis_amatrix
        func(cb, src, self, pardepth)

    def forward_clusterbasis_amatrix(self, cb: 'misc.ClusterBasis',
                                     src: 'AMatrix'):
        libclusterbasis.forward_clusterbasis_amatrix(cb, src, self)

    def forward_clusterbasis_trans_amatrix(self, cb: 'misc.ClusterBasis',
                                           src: 'AMatrix'):
        libclusterbasis.forward_clusterbasis_trans_amatrix(cb, src, self)

    def backward_clusterbasis_amatrix(self, cb: 'misc.ClusterBasis',
                                      src: 'AMatrix'):
        libclusterbasis.backward_clusterbasis_amatrix(cb, src, self)

    def backward_clusterbasis_trans_amatrix(self, cb: 'misc.ClusterBasis',
                                            src: 'AMatrix'):
        libclusterbasis.backward_clusterbasis_trans_amatrix(cb, src, self)

    # ***** Operators ******

    def __add__(self, rhs):
        verify_type(rhs, [AMatrix])
        a = self.clone()
        a.add(rhs)
        return a

    def __sub__(self, rhs):
        verify_type(rhs, [AMatrix])
        a = self.clone()
        a.add(rhs, -1)
        return a

    def __mul__(self, rhs):
        verify_type(rhs, [int, float])
        a = self.clone()
        a.scale(rhs)
        return a

    def __matmul__(self, rhs):
        verify_type(rhs, [AMatrix])
        a = AMatrix.new(self.rows, self.cols, fill=mat.FillType.Zeros)
        a.addmul(1.0, self, rhs, False, False)
        return a

    def __rmul__(self, lhs):
        return self * lhs

    def __neg__(self):
        return -1 * self

    def __getitem__(self, index):
        if index not in range(self.cols):
            raise ValueError('Index out of range.')
        return self.a[index]

    def __eq__(self, other):
        if self.cols != other.cols or self.rows != other.rows:
            return False
        return self.a == other.a

    def __len__(self):
        return self.cols * self.rows

    def __iadd__(self, rhs):
        verify_type(rhs, [AMatrix])
        self.add(rhs)
        return self

    def __isub__(self, rhs):
        verify_type(rhs, [AMatrix])
        self.add(rhs, -1)
        return self

    def __imul__(self, rhs):
        verify_type(rhs, [int, float])
        self.scale(rhs)
        return self

    def __str__(self):
        return str(self.a)
