from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_double, c_uint, c_void_p, c_size_t

from h2libpy.lib.util.helper import get_func

# ------------------------


class CStructAVector(Struct): pass


# ------------------------


CStructAVector._fields_ = [
    ('v', PTR(c_double)),
    ('dim', c_uint),
    ('owner', c_void_p)
]


# ------------------------


new_avector = get_func('new_avector', PTR(CStructAVector), [c_uint])
del_avector = get_func('del_avector', None, [PTR(CStructAVector)])
init_sub_avector = get_func('init_sub_avector', PTR(CStructAVector), [PTR(CStructAVector), PTR(CStructAVector), c_uint, c_uint])
fill_avector = get_func('fill_avector', None, [PTR(CStructAVector), c_double])
random_avector = get_func('random_avector', None, [PTR(CStructAVector)])
norm2_avector = get_func('norm2_avector', c_double, [PTR(CStructAVector)])
getsize_avector = get_func('getsize_avector', c_size_t, [PTR(CStructAVector)])
clear_avector = get_func('clear_avector', None, [PTR(CStructAVector)])
