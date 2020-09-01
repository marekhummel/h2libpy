from typing import List, Tuple, Union

import h2libpy.data.matrix as mat
import h2libpy.data.misc as misc
import h2libpy.lib.amatrix as libamatrix
import h2libpy.lib.avector as libavector
import h2libpy.lib.clusterbasis as libclusterbasis
import h2libpy.lib.h2matrix as libh2matrix
import h2libpy.lib.hmatrix as libhmatrix
import h2libpy.lib.rkmatrix as librkmatrix
import h2libpy.lib.sparsematrix as libsparsematrix
import h2libpy.lib.uniform as libuniform
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import cptr_to_list, pylist_to_ptr, verify_type
from h2libpy.lib.settings import field


mvm_union = Union['mat.AMatrix', 'mat.SparseMatrix', 'mat.HMatrix',
                  'mat.H2Matrix', 'mat.DH2Matrix', 'mat.RkMatrix',
                  'misc.Uniform', 'misc.ClusterBasis']


class AVector(StructWrapper, cstruct=libavector.CStructAVector):
    # ***** Fields *****
    dim: int
    v: Tuple[float, ...]

    # ***** Constructors *****

    @classmethod
    def new(cls, dim: int, *, zeros: bool = False) -> 'AVector':
        obj = libavector.new_zero_avector(dim) if zeros \
            else libavector.new_avector(dim)
        return cls(obj)

    @classmethod
    def from_subvector(cls, src: 'AVector', dim: int,
                       off: int = 0) -> 'AVector':
        return cls(libavector.new_sub_avector(src, dim, off))

    @classmethod
    def from_list(cls, elems: List[float], *, dim: int = -1) -> 'AVector':
        cdim = dim if dim != -1 else len(elems)
        celems = pylist_to_ptr(elems, field)
        obj = libavector.new_pointer_avector(celems, cdim)
        return cls(obj, refs=[celems])

    # ***** Properties *****

    def __getter_dim(self) -> int:
        return self.cobj().dim

    def __getter_v(self) -> Tuple[float, ...]:
        return tuple(cptr_to_list(self.cobj().v, self.dim))

    # ***** Methods ******

    def resize(self, dim: int) -> None:
        libavector.resize_avector(self, dim)

    def shrink(self, dim: int) -> None:
        libavector.shrink_avector(self, dim)

    def memsize(self, heaponly: bool = False) -> int:
        if heaponly:
            return libavector.getsize_heap_avector(self)
        else:
            return libavector.getsize_avector(self)

    def clear(self) -> None:
        libavector.clear_avector(self)

    def fill(self, value: float) -> None:
        libavector.fill_avector(self, value)

    def rand(self, force_real: bool = False) -> None:
        if force_real:
            libavector.random_real_avector(self)
        else:
            libavector.random_avector(self)

    def copy(self, target: 'AVector') -> None:
        if self.dim == target.dim:
            libavector.copy_avector(self, target)
        else:
            libavector.copy_sub_avector(self, target)

    def print(self) -> None:
        libavector.print_avector(self)

    def scale(self, alpha: float) -> None:
        libavector.scale_avector(alpha, self)

    def norm(self) -> float:
        return libavector.norm2_avector(self)

    def dot(self, other: 'AVector') -> float:
        return libavector.dotprod_avector(self, other)

    def add(self, other: 'AVector', alpha: float = 1.0) -> None:
        libavector.add_avector(alpha, other, self)

    def delete(self) -> None:
        super().delete(libavector.del_avector)

    # -------

    def mvm(self, alpha: float, trans: bool, a: mvm_union, src: 'AVector'):
        mvm_types = [mat.AMatrix, mat.SparseMatrix, mat.HMatrix, mat.H2Matrix,
                     mat.DH2Matrix, mat.RkMatrix, misc.Uniform,
                     misc.ClusterBasis]
        verify_type(a, mvm_types)

        if isinstance(a, mat.AMatrix):
            mvm_func = libamatrix.mvm_amatrix_avector
        elif isinstance(a, mat.SparseMatrix):
            mvm_func = libsparsematrix.mvm_sparsematrix_avector
        elif isinstance(a, mat.HMatrix):
            mvm_func = libhmatrix.mvm_hmatrix_avector
        elif isinstance(a, mat.H2Matrix):
            mvm_func = libh2matrix.mvm_h2matrix_avector
        elif isinstance(a, mat.RkMatrix):
            mvm_func = librkmatrix.mvm_rkmatrix_avector
        elif isinstance(a, mat.DH2Matrix):
            raise ValueError('MVM for DH2-matrizes not yet implemented.')
        elif isinstance(a, misc.Uniform):
            mvm_func = libuniform.mvm_uniform_avector
        elif isinstance(a, misc.ClusterBasis):
            def mvm_cb(alpha, trans, cb, src, tgt):
                if trans:
                    func = libclusterbasis.addeval_clusterbasis_avector
                else:
                    func = libclusterbasis.addevaltrans_clusterbasis_avector
                func(alpha, cb, src, self)
            mvm_func = mvm_cb

        mvm_func(alpha, trans, a, src, self)

    def fast_addeval(self, alpha: float, trans: bool,
                     h: Union['mat.HMatrix', 'mat.H2Matrix'], src: 'AVector'):
        verify_type(h, [mat.HMatrix, mat.H2Matrix])

        if isinstance(h, mat.HMatrix):
            if trans:
                func = libhmatrix.fastaddevaltrans_hmatrix_avector
            else:
                func = libhmatrix.fastaddeval_hmatrix_avector
        elif isinstance(h, mat.H2Matrix):
            if trans:
                func = libh2matrix.fastaddevaltrans_h2matrix_avector
            else:
                func = libh2matrix.fastaddeval_h2matrix_avector

        func(alpha, h, src, self)

    def forward_clusterbasis_avector(self, cb: 'misc.ClusterBasis',
                                     src: 'AVector'):
        libclusterbasis.forward_clusterbasis_avector(cb, src, self)

    def forward_parallel_clusterbasis_avector(self, cb: 'misc.ClusterBasis',
                                              src: 'AVector', pardepth: int):
        func = libclusterbasis.forward_parallel_clusterbasis_avector
        func(cb, src, self, pardepth)

    def forward_nopermutation_clusterbasis_avector(self,
                                                   cb: 'misc.ClusterBasis',
                                                   src: 'AVector'):
        func = libclusterbasis.forward_nopermutation_clusterbasis_avector
        func(cb, src, self)

    def forward_notransfer_clusterbasis_avector(self, cb: 'misc.ClusterBasis',
                                                src: 'AVector'):
        libclusterbasis.forward_notransfer_clusterbasis_avector(cb, src, self)

    def backward_clusterbasis_avector(self, cb: 'misc.ClusterBasis',
                                      src: 'AVector'):
        libclusterbasis.backward_clusterbasis_avector(cb, src, self)

    def backward_parallel_clusterbasis_avector(self, cb: 'misc.ClusterBasis',
                                               src: 'AVector', pardepth: int):
        func = libclusterbasis.backward_parallel_clusterbasis_avector
        func(cb, src, self, pardepth)

    def backward_nopermutation_clusterbasis_avector(self,
                                                    cb: 'misc.ClusterBasis',
                                                    src: 'AVector'):
        func = libclusterbasis.backward_nopermutation_clusterbasis_avector
        func(cb, src, self)

    def backward_notransfer_clusterbasis_avector(self, cb: 'misc.ClusterBasis',
                                                 src: 'AVector'):
        libclusterbasis.backward_notransfer_clusterbasis_avector(cb, src, self)

    def compress_clusterbasis_avector(self, cb: 'misc.ClusterBasis',
                                      src: 'AVector'):
        libclusterbasis.compress_clusterbasis_avector(cb, src, self)

    def expand_clusterbasis_avector(self, cb: 'misc.ClusterBasis',
                                    src: 'AVector'):
        libclusterbasis.expand_clusterbasis_avector(cb, self, src)

    # ***** Operators ******

    def __add__(self, rhs: 'AVector') -> 'AVector':
        verify_type(rhs, [AVector])
        v = AVector.new(self.dim, zeros=True)
        v.add(self)
        v.add(rhs)
        return v

    def __sub__(self, rhs: 'AVector') -> 'AVector':
        verify_type(rhs, [AVector])
        v = AVector.new(self.dim, zeros=True)
        v.add(self)
        v.add(rhs, -1)
        return v

    def __mul__(self, rhs: Union[int, float]) -> 'AVector':
        verify_type(rhs, [int, float])
        v = AVector.new(self.dim, zeros=True)
        v.add(self, rhs)
        return v

    def __rmul__(self, lhs: Union[int, float]) -> 'AVector':
        return self * lhs

    def __neg__(self) -> 'AVector':
        v = AVector.new(self.dim, zeros=True)
        v.add(self, -1)
        return v

    def __getitem__(self, index) -> float:
        return list(self.v)[index]

    def __eq__(self, other) -> bool:
        if self.dim != other.dim:
            return False
        return self.v == other.v

    def __len__(self) -> int:
        return self.dim

    def __iadd__(self, rhs: 'AVector') -> 'AVector':
        verify_type(rhs, [AVector])
        self.add(rhs)
        return self

    def __isub__(self, rhs: 'AVector') -> 'AVector':
        verify_type(rhs, [AVector])
        self.add(rhs, -1)
        return self

    def __imul__(self, rhs: Union[int, float]) -> 'AVector':
        verify_type(rhs, [int, float])
        self.scale(rhs)
        return self

    def __str__(self) -> str:
        return str(self.v)
