from ctypes import c_double
from typing import Tuple, List

import h2libpy.lib.avector as libavector
import h2libpy.lib.amatrix as libamatrix
from h2libpy.base.cutil import cptr_to_list
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.matrix.amatrix import AMatrix


class AVector(StructWrapper, cstruct=libavector.CStructAVector):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, dim: int, zero: bool = False) -> 'AVector':
        obj = libavector.new_zero_avector(dim) if zero \
                else libavector.new_avector(dim)
        return cls(obj)

    @classmethod
    def from_subvector(cls, src: 'AVector', dim: int,
                       off: int) -> 'AVector':
        v = libavector.new_avector(dim)
        libavector.init_sub_avector(v, src, dim, off)
        return cls(v)

    @classmethod
    def from_list(cls, elems: List[float], dim: int = -1):
        cdim = dim if dim != -1 else len(elems)
        celems = (c_double * len(elems))(*elems)
        obj = libavector.new_pointer_avector(celems, cdim)
        return cls(obj, refs=[celems])

    # ***** Properties *****

    def __getter_dim(self) -> int:
        return self.cobj().dim

    def __getter_v(self) -> Tuple[float, ...]:
        return tuple(cptr_to_list(self.cobj().v, self.dim))

    # ***** Methods ******

    def fill(self, value):
        libavector.fill_avector(self, c_double(value))

    def rand(self):
        libavector.random_avector(self)

    def norm(self) -> float:
        return libavector.norm2_avector(self)

    def size(self) -> int:
        return libavector.getsize_avector(self)

    def clear(self):
        libavector.clear_avector(self)

    def addeval_matrix(self, alpha: float, a: 'AMatrix', src: 'AVector'):
        libamatrix.addeval_amatrix_avector(alpha, a, src, self)

    def print(self):
        libavector.print_avector(self)
