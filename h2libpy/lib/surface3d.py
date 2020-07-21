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
    ('x', PTR(real * 3)),
    ('e', PTR(c_uint * 2)),
    ('t', PTR(c_uint * 3)),
    ('s', PTR(c_uint * 3)),
    ('n', PTR(real * 3)),
    ('g', PTR(real)),
    ('hmin', real),
    ('hmax', real)
]


# ------------------------


new_surface3d = get_func('new_surface3d', PTR(LibSurface3d), [c_uint, c_uint, c_uint])
del_surface3d = get_func('del_surface3d', None, [PTR(LibSurface3d)])
