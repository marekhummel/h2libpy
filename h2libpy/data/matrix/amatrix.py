from ctypes import c_uint
from typing import List

import h2libpy.lib.amatrix as libamatrix
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import cptr_to_list, pylist_to_ptr, try_wrap
from h2libpy.data.matrix.enums import ClearType, FillType, NormType
from h2libpy.lib.settings import field


class AMatrix(StructWrapper, cstruct=libamatrix.CStructAMatrix):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, rows: int, cols: int, *, fill: 'FillType' = FillType.Nothing):
        if fill == FillType.Zeros:
            return cls(libamatrix.new_zero_amatrix(rows, cols))
        elif fill == FillType.Identity:
            return cls(libamatrix.new_identity_amatrix(rows, cols))
        else:  # fill == FillType.Nothing
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
        last_coeff = (self.rows-1) + (self.cols-1) * self.ld
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

    def clear(self, *, clear_type: 'ClearType' = ClearType.All):
        if clear_type == ClearType.Lower:
            libamatrix.clear_lower_amatrix(self, False)
        elif clear_type == ClearType.LowerStrict:
            libamatrix.clear_lower_amatrix(self, True)
        elif clear_type == ClearType.Upper:
            libamatrix.clear_upper_amatrix(self, False)
        elif clear_type == ClearType.UpperStrict:
            libamatrix.clear_upper_amatrix(self, True)
        else:  # clear_type == ClearType.All:
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

    def norm(self, *, ntype: NormType = NormType.Spectral):
        if ntype == NormType.Frobenius:
            return libamatrix.normfrob_amatrix(self)
        elif ntype == NormType.SquaredFrobenius:
            return libamatrix.normfrob2_amatrix(self)
        else:  # ntype == NormType.Spectral
            return libamatrix.norm2_amatrix(self)

    def norm2_diff(self, other: 'AMatrix') -> float:
        return libamatrix.norm2diff_amatrix(self, other)

    def add(self, other: 'AMatrix', alpha: float = 1.0, trans: bool = False):
        libamatrix.add_amatrix(alpha, trans, other, self)

    def addmul(self, alpha: float, a: 'AMatrix', b: 'AMatrix',
               trans_a: bool, trans_b: bool):
        libamatrix.addmul_amatrix(alpha, trans_a, a, trans_b, b, self)

    def bidiagmul(self, alpha: float, trans: bool,
                  dia: 'AVector', lo: 'AVector'):
        libamatrix.bidiagmul_amatrix(alpha, trans, self, dia, lo)

    # ***** Operators ******
