from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

from h2libpy.lib.settings import real
from h2libpy.lib.surface3d import CStructSurface3d
from h2libpy.lib.util.helper import get_func

# ------------------------


class CStructSingquad2d(Struct): pass


# ------------------------


CStructSingquad2d._fields_ = [
    ('x_id', PTR(real)),
    ('y_id', PTR(real)),
    ('w_id', PTR(real)),
    ('base_id', real),
    ('n_id', c_uint),
    ('x_edge', PTR(real)),
    ('y_edge', PTR(real)),
    ('w_edge', PTR(real)),
    ('base_edge', real),
    ('n_edge', c_uint),
    ('x_vert', PTR(real)),
    ('y_vert', PTR(real)),
    ('w_vert', PTR(real)),
    ('base_vert', real),
    ('n_vert', c_uint),
    ('x_dist', PTR(real)),
    ('y_dist', PTR(real)),
    ('w_dist', PTR(real)),
    ('base_dist', real),
    ('n_dist', c_uint),
    ('x_single', PTR(real)),
    ('y_single', PTR(real)),
    ('w_single', PTR(real)),
    ('base_single', real),
    ('n_single', c_uint),
    # ('tri_x', PTR(real)),
    # ('tri_y', PTR(real)),
    # ('tri_z', PTR(real)),
    ('q', c_uint),
    ('q2', c_uint),
    ('nmax', c_uint)
]


# ------------------------


build_singquad2d = get_func('build_singquad2d', PTR(CStructSingquad2d), [PTR(CStructSurface3d), c_uint, c_uint])
del_singquad2d = get_func('del_singquad2d', None, [PTR(CStructSingquad2d)])
weight_basisfunc_ll_singquad2d = get_func('weight_basisfunc_ll_singquad2d', None, [PTR(real), PTR(real), PTR(real), c_uint])
weight_basisfunc_cl_singquad2d = get_func('weight_basisfunc_cl_singquad2d', None, [PTR(real), PTR(real), PTR(real), c_uint])
weight_basisfunc_lc_singquad2d = get_func('weight_basisfunc_lc_singquad2d', None, [PTR(real), PTR(real), PTR(real), c_uint])
weight_basisfunc_l_singquad2d = get_func('weight_basisfunc_l_singquad2d', None, [PTR(real), PTR(real), PTR(real), c_uint])
fast_select_quadrature = get_func('fast_select_quadrature', c_uint, [PTR(c_uint * 3), c_uint, c_uint])
select_quadrature_singquad2d = get_func('select_quadrature_singquad2d', c_uint, [PTR(CStructSingquad2d), PTR(c_uint), PTR(c_uint), PTR(c_uint), PTR(c_uint), PTR(PTR(real)), PTR(PTR(real)), PTR(PTR(real)), PTR(c_uint), PTR(real)])
