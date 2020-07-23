from ctypes import POINTER

import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper


class ParBem3d(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libbem3d.CStructParBem3d))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_grcnn(self) -> int:
        return self.cobj().grcnn

    def __getter_gccnn(self) -> int:
        return self.cobj().gccnn

    def __getter_grbnn(self) -> int:
        return self.cobj().grbnn

    def __getter_gcbnn(self) -> int:
        return self.cobj().gcbnn

    # ***** Methods ******
