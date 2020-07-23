from ctypes import POINTER, c_double
from typing import Tuple

import h2libpy.lib.avector as libavector
import h2libpy.lib.amatrix as libamatrix
from h2libpy.base.cutil import cptr_to_list
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.matrix.amatrix import AMatrix


class AVector(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libavector.CStructAVector))
        self._as_parameter_ = cobj

    def __del__(self):
        pass 
        # libavector.del_avector(self)

    @classmethod
    def new(cls, dim: int):
        return cls(libavector.new_avector(dim))

    @classmethod
    def from_subvector(cls, src: 'libavector.CStructAVector', dim: int,
                       off: int):
        v = libavector.new_avector(dim)
        libavector.init_sub_avector(v, src, dim, off)
        return cls(v)

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
