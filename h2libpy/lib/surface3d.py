from ctypes import POINTER as PTR
from ctypes import c_bool, c_char_p, c_uint

from h2libpy.lib.settings import real
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import CStructSurface3d

# ------------------------


CStructSurface3d._fields_ = [
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


new_surface3d = get_func('new_surface3d', PTR(CStructSurface3d), [c_uint, c_uint, c_uint])
prepare_surface3d = get_func('prepare_surface3d', None, [PTR(CStructSurface3d)])
del_surface3d = get_func('del_surface3d', None, [PTR(CStructSurface3d)])
getproperties_surface3d = get_func('getproperties_surface3d', None, [PTR(CStructSurface3d), PTR(real), PTR(real), PTR(real), PTR(real)])
print_surface3d = get_func('print_surface3d', None, [PTR(CStructSurface3d)])
check_surface3d = get_func('check_surface3d', c_uint, [PTR(CStructSurface3d)])
isclosed_surface3d = get_func('isclosed_surface3d', c_bool, [PTR(CStructSurface3d)])
isoriented_surface3d = get_func('isoriented_surface3d', c_bool, [PTR(CStructSurface3d)])
scale_surface3d = get_func('scale_surface3d', None, [PTR(CStructSurface3d), PTR(real), PTR(real)])
translate_surface3d = get_func('translate_surface3d', None, [PTR(CStructSurface3d), PTR(real)])
merge_surface3d = get_func('merge_surface3d', PTR(CStructSurface3d), [PTR(CStructSurface3d), PTR(CStructSurface3d)])
write_surface3d = get_func('write_surface3d', None, [PTR(CStructSurface3d), c_char_p])
read_surface3d = get_func('read_surface3d', PTR(CStructSurface3d), [c_char_p])
write_nc_surface3d = get_func('write_nc_surface3d', None, [PTR(CStructSurface3d), c_char_p])
read_nc_surface3d = get_func('read_nc_surface3d', PTR(CStructSurface3d), [c_char_p])
read_netgen_surface3d = get_func('read_netgen_surface3d', PTR(CStructSurface3d), [c_char_p])
read_gmsh_surface3d = get_func('read_gmsh_surface3d', PTR(CStructSurface3d), [c_char_p])
read_unv_surface3d = get_func('read_unv_surface3d', PTR(CStructSurface3d), [c_char_p])
refine_red_surface3d = get_func('refine_red_surface3d', PTR(CStructSurface3d), [PTR(CStructSurface3d)])
