from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

from h2libpy.lib.util.helper import get_func
from h2libpy.lib.settings import real

# ------------------------


class LibSurface3d(Struct): pass


# ------------------------


LibSurface3d._fields_ = [
    ('vertices', c_uint),
    ('edges', c_uint),
    ('triangles', c_uint),
    ('g', PTR(real)),
    ('hmin', real),
    ('hmax', real)
]


# ------------------------


del_surface3d = get_func('del_surface3d', None, [PTR(LibSurface3d)])
