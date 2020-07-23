from ctypes import POINTER

import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.problem.bem3d.bem3d import Bem3d


class CompData(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libbem3d.CStructCompData))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_bem(self) -> 'Bem3d':
        return Bem3d(self.cobj().bem)

    def __getter_rows(self) -> bool:
        return self.cobj().rows

    # ***** Methods ******
