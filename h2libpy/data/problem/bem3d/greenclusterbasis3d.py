from ctypes import POINTER

import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper


class GreenClusterBasis3d(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libbem3d.CStructGreenClusterBasis3d))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

    # ***** Properties *****

    # ***** Methods ******
