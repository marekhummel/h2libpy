from ctypes import POINTER

import h2libpy.lib.singquad2d as libsingquad2d
from h2libpy.base.structwrapper import StructWrapper


class SingQuad2d(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libsingquad2d.CStructSingquad2d))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

    # ***** Properties *****

    # ***** Methods ******
