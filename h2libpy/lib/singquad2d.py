from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

from h2libpy.lib.settings import real


class CStructSingquad2d(Struct):
    _fields_ = [
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
