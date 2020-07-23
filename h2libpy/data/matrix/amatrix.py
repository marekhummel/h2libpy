from ctypes import POINTER
from typing import List

import h2libpy.lib.amatrix as libamatrix
from h2libpy.base.cutil import cptr_to_list
from h2libpy.base.structwrapper import StructWrapper


class AMatrix(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libamatrix.CStructAMatrix))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

    @classmethod
    def new(cls, rows: int, cols: int):
        return cls(libamatrix.new_amatrix(rows, cols))

    # ***** Properties *****

    def __getter_a(self) -> List[float]:
        return cptr_to_list(self.cobj().a, self.rows * self.cols)

    def __getter_ld(self) -> int:
        return self.cobj().ld

    def __getter_rows(self) -> int:
        return self.cobj().rows

    def __getter_cols(self) -> int:
        return self.cobj().cols

    # ***** Methods ******

    def size(self):
        return libamatrix.getsize_amatrix(self)
