from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint, c_void_p

from h2libpy.lib.util.helper import get_func
from h2libpy.lib.settings import real
from h2libpy.lib.surface3d import CStructSurface3d

# ------------------------


class CStructMacroSurface3d(Struct): pass


# ------------------------


CStructMacroSurface3d._fields_ = [
    ('vertices', c_uint),
    ('edges', c_uint),
    ('triangles', c_uint),
    ('x', PTR(real * 3)),
    ('e', PTR(c_uint * 2)),
    ('t', PTR(c_uint * 3)),
    ('s', PTR(c_uint * 3)),
    ('phidata', c_void_p),
]


# ------------------------

new_macrosurface3d = get_func('new_macrosurface3d', PTR(CStructMacroSurface3d), [c_uint, c_uint, c_uint])
new_sphere_macrosurface3d = get_func('new_sphere_macrosurface3d', PTR(CStructMacroSurface3d), [])
build_from_macrosurface3d_surface3d = get_func('build_from_macrosurface3d_surface3d', PTR(CStructSurface3d), [PTR(CStructMacroSurface3d), c_uint])
del_macrosurface3d = get_func('del_macrosurface3d', None, [PTR(CStructMacroSurface3d)])
