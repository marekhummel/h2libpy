from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_double, c_uint, c_void_p, c_size_t

from h2libpy.util.helper import get_func

# ------------------------


class LibAVector(Struct): pass


# ------------------------


LibAVector._fields_ = [
    ('v', PTR(c_double)),
    ('dim', c_uint),
    ('owner', c_void_p)
]


# ------------------------


new_avector = get_func('new_avector', PTR(LibAVector), [c_uint])
del_avector = get_func('del_avector', None, [PTR(LibAVector)])
init_sub_avector = get_func('init_sub_avector', PTR(LibAVector), [PTR(LibAVector), PTR(LibAVector), c_uint, c_uint])
fill_avector = get_func('fill_avector', None, [PTR(LibAVector), c_double])
random_avector = get_func('random_avector', None, [PTR(LibAVector)])
norm2_avector = get_func('norm2_avector', c_double, [PTR(LibAVector)])
getsize_avector = get_func('getsize_avector', c_size_t, [PTR(LibAVector)])
clear_avector = get_func('clear_avector', None, [PTR(LibAVector)])
