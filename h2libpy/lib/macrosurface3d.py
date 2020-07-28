from ctypes import CFUNCTYPE
from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint, c_void_p

from h2libpy.lib.settings import real
from h2libpy.lib.surface3d import CStructSurface3d
from h2libpy.lib.util.helper import get_func

# ------------------------


class CStructMacroSurface3d(Struct): pass


# ------------------------


CFuncPhi = CFUNCTYPE(None, *[c_uint, real, real, c_void_p, real*3])


# ------------------------


CStructMacroSurface3d._fields_ = [
    ('vertices', c_uint),
    ('edges', c_uint),
    ('triangles', c_uint),
    ('x', PTR(real * 3)),
    ('e', PTR(c_uint * 2)),
    ('t', PTR(c_uint * 3)),
    ('s', PTR(c_uint * 3)),
    ('phi', CFuncPhi),
    ('phidata', c_void_p),
]


# ------------------------


new_macrosurface3d = get_func('new_macrosurface3d', PTR(CStructMacroSurface3d), [c_uint, c_uint, c_uint])
del_macrosurface3d = get_func('del_macrosurface3d', None, [PTR(CStructMacroSurface3d)])
new_sphere_macrosurface3d = get_func('new_sphere_macrosurface3d', PTR(CStructMacroSurface3d), [])
new_parabolic_mirror_macrosurface3d = get_func('new_parabolic_mirror_macrosurface3d', PTR(CStructMacroSurface3d), [])
new_cuboid_macrosurface3d = get_func('new_cuboid_macrosurface3d', PTR(CStructMacroSurface3d), [real, real, real, real, real, real])
new_cube_macrosurface3d = get_func('new_cube_macrosurface3d', PTR(CStructMacroSurface3d), [])
new_cylinder_macrosurface3d = get_func('new_cylinder_macrosurface3d', PTR(CStructMacroSurface3d), [])
build_from_macrosurface3d_surface3d = get_func('build_from_macrosurface3d_surface3d', PTR(CStructSurface3d), [PTR(CStructMacroSurface3d), c_uint])
build_interactive_surface3d = get_func('build_interactive_surface3d', PTR(CStructSurface3d), [])
