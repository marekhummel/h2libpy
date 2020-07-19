from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

from h2libpy.util.lib.settings import real


class LibSurface3d(Struct):
    _fields_ = [
        ('vertices', c_uint),
        ('edges', c_uint),
        ('triangles', c_uint),
        ('g', PTR(real)),
        ('hmin', real),
        ('hmax', real)
    ]
