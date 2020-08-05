from typing import List, Tuple

import h2libpy.lib.amatrix as libamatrix
import h2libpy.lib.avector as libavector
import h2libpy.lib.hmatrix as libhmatrix
import h2libpy.lib.sparsematrix as libsparsematrix
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import (cptr_to_list, is_scalar, pylist_to_ptr,
                               verify_type)
from h2libpy.lib.settings import field


class AVector(StructWrapper, cstruct=libavector.CStructAVector):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, dim: int, *, zeros: bool = False) -> 'AVector':
        obj = libavector.new_zero_avector(dim) if zeros \
            else libavector.new_avector(dim)
        return cls(obj)

    @classmethod
    def from_subvector(cls, src: 'AVector', dim: int,
                       off: int = 0) -> 'AVector':
        v = libavector.new_avector(dim)
        libavector.init_sub_avector(v, src, dim, off)
        return cls(v)

    @classmethod
    def from_list(cls, elems: List[float], *, dim: int = -1):
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

    def resize(self, dim: int):
        libavector.resize_avector(self, dim)

    def shrink(self, dim: int):
        libavector.shrink_avector(self, dim)

    def size(self, heaponly: bool = False) -> int:
        if heaponly:
            return libavector.getsize_heap_avector(self)
        else:
            return libavector.getsize_avector(self)

    def clear(self):
        libavector.clear_avector(self)

    def fill(self, value: float):
        libavector.fill_avector(self, value)

    def rand(self, force_real: bool = False):
        if force_real:
            libavector.random_real_avector(self)
        else:
            libavector.random_avector(self)

    def copy(self, target: 'AVector'):
        if self.dim == target.dim:
            libavector.copy_avector(self, target)
        else:
            libavector.copy_sub_avector(self, target)

    def print(self):
        libavector.print_avector(self)

    def scale(self, alpha: float):
        libavector.scale_avector(alpha, self)

    def norm(self) -> float:
        return libavector.norm2_avector(self)

    def dot(self, other: 'AVector') -> float:
        return libavector.dotprod_avector(self, other)

    def add(self, other: 'AVector', alpha: float = 1.0):
        libavector.add_avector(alpha, other, self)

    # -------

    def addeval_amatrix_avector(self, alpha: float, a: 'AMatrix',
                                src: 'AVector'):
        libamatrix.addeval_amatrix_avector(alpha, a, src, self)

    def addevaltrans_amatrix_avector(self, alpha: float,
                                     a: 'AMatrix', src: 'AVector'):
        libamatrix.addevaltrans_amatrix_avector(alpha, a, src, self)

    def mvm_amatrix_avector(self, alpha: float, trans: bool,
                            a: 'AMatrix', src: 'AVector'):
        libamatrix.mvm_amatrix_avector(alpha, trans, a, src, self)

    def mvm_hmatrix_avector(self, alpha: float, trans: bool,
                            h: 'HMatrix', src: 'AVector'):
        libhmatrix.mvm_hmatrix_avector(alpha, trans, h, src, self)

    def fastaddeval_hmatrix_avector(self, alpha: float, h: 'HMatrix',
                                    src: 'AVector'):
        libhmatrix.fastaddeval_hmatrix_avector(alpha, h, src, self)

    def addeval_hmatrix_avector(self, alpha: float, h: 'HMatrix',
                                src: 'AVector'):
        libhmatrix.addeval_hmatrix_avector(alpha, h, src, self)

    def fastaddevaltrans_hmatrix_avector(self, alpha: float, h: 'HMatrix',
                                         src: 'AVector'):
        libamatrix.fastaddevaltrans_hmatrix_avector(alpha, h, src, self)

    def addevaltrans_hmatrix_avector(self, alpha: float, h: 'HMatrix',
                                     src: 'AVector'):
        libamatrix.addevaltrans_hmatrix_avector(alpha, h, src, self)

    def addeval_sparsematrix_avector(self, alpha: float, a: 'SparseMatrix',
                                     src: 'AVector'):
        libsparsematrix.addeval_sparsematrix_avector(alpha, a, src, self)

    def addevaltrans_sparsematrix_avector(self, alpha: float,
                                          a: 'SparseMatrix', src: 'AVector'):
        libsparsematrix.addevaltrans_sparsematrix_avector(alpha, a, src, self)

    def mvm_sparsematrix_avector(self, alpha: float, trans: bool,
                                 a: 'SparseMatrix', src: 'AVector'):
        libsparsematrix.mvm_sparsematrix_avector(alpha, trans, a, src, self)

    # ***** Operators ******

    def __add__(self, rhs):
        verify_type(rhs, [AVector])
        v = AVector.new(self.dim, zeros=True)
        v.add(self)
        v.add(rhs)
        return v

    def __sub__(self, rhs):
        verify_type(rhs, [AVector])
        v = AVector.new(self.dim, zeros=True)
        v.add(self)
        v.add(rhs, -1)
        return v

    def __mul__(self, rhs):
        verify_type(rhs, [AVector, int, float])
        if isinstance(rhs, AVector):
            return self.dot(rhs)
        elif is_scalar(rhs):
            v = AVector.new(self.dim, zeros=True)
            v.add(self, rhs)
            return v

    def __rmul__(self, lhs):
        return self * lhs

    def __neg__(self):
        v = AVector.new(self.dim, zeros=True)
        v.add(self, -1)
        return v

    def __getitem__(self, index):
        if index not in range(self.dim):
            raise ValueError('Index out of range.')
        return self.v[index]

    def __eq__(self, other):
        if self.dim != other.dim:
            return False
        return self.v == other.v

    def __len__(self):
        return self.dim

    def __iadd__(self, rhs):
        verify_type(rhs, [AVector])
        self.add(rhs)
        return self

    def __isub__(self, rhs):
        verify_type(rhs, [AVector])
        self.add(rhs, -1)
        return self

    def __imul__(self, rhs):
        verify_type(rhs, [int, float])
        self.scale(rhs)
        return self

    def __str__(self):
        return str(self.v)
