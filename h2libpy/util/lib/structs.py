from ctypes import Structure as Struct
from ctypes import c_double, c_uint, c_void_p, POINTER


class LibAVector(Struct):
    _fields_ = [
        ('v', POINTER(c_double)),
        ('dim', c_uint),
        ('owner', c_void_p)
    ]
