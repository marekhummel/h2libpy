from ctypes import POINTER

import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.problem.bem3d.vertlist import VertList


class TriList(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libbem3d.CStructTriList))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_t(self) -> int:
        return self.cobj().t

    def __getter_vt(self) -> 'VertList':
        return VertList(self.cobj().vl)

    def __getter_next(self) -> 'TriList':
        return TriList(self.cobj().next)

    # ***** Methods ******
