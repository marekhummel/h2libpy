from ctypes import POINTER

import h2libpy.lib.amatrix as libamatrix
from h2libpy.base.structwrapper import StructWrapper


class AMatrix(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libamatrix.CStructAMatrix))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

    # ***** Properties *****

    # ***** Methods ******
