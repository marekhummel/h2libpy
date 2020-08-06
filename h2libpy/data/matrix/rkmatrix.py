from ctypes import pointer

import h2libpy.lib.rkmatrix as librkmatrix
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import try_wrap
from h2libpy.data.matrix.amatrix import AMatrix


class RkMatrix(StructWrapper, cstruct=librkmatrix.CStructRkMatrix):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, rows: int, cols: int, k: int):
        return cls(librkmatrix.new_rkmatrix(rows, cols, k))

    @classmethod
    def from_submatrix(cls, src: 'RkMatrix', rows: int, cols: int,
                       roff: int, coff: int):
        return cls(librkmatrix.new_sub_rkmatrix(src, rows, roff, cols, coff))

    # ***** Properties *****

    def __getter_a(self) -> 'AMatrix':
        try_wrap(pointer(self.cobj().a), AMatrix)

    def __getter_b(self) -> 'AMatrix':
        try_wrap(pointer(self.cobj().b), AMatrix)

    def __getter_k(self) -> int:
        return self.cobj().k

    # ***** Methods ******

    def setrank(self, k: int):
        librkmatrix.setrank_rkmatrix(self, k)

    def resize(self, rows: int, cols: int, k: int):
        librkmatrix.resize_rkmatrix(self, rows, cols, k)

    def size(self, *, heaponly: bool = False):
        if heaponly:
            return librkmatrix.getsize_heap_rkmatrix(self)
        else:
            return librkmatrix.getsize_rkmatrix(self)

    def clone(self) -> 'RkMatrix':
        return try_wrap(librkmatrix.clone_rkmatrix(self), RkMatrix)

    def copy(self, target: 'RkMatrix', trans: bool = False):
        librkmatrix.copy_rkmatrix(trans, self, target)

    def scale(self, alpha: float):
        librkmatrix.scale_rkmatrix(alpha, self)

    def rand(self, kmax: int):
        librkmatrix.random_rkmatrix(self, kmax)

    def norm(self):
        return librkmatrix.norm2_rkmatrix(self)

    def norm2_diff(self, other: 'RkMatrix') -> float:
        return librkmatrix.norm2diff_rkmatrix(self, other)
