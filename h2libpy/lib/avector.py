from ctypes import POINTER as PTR
from ctypes import c_uint, c_void_p, c_size_t

from h2libpy.lib.settings import real, field
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import CStructAVector, CStructAMatrix

# ------------------------


CStructAVector._fields_ = [
    ('v', PTR(field)),
    ('dim', c_uint),
    ('owner', c_void_p)
]


# ------------------------


init_avector = get_func('init_avector', PTR(CStructAVector), [PTR(CStructAVector), c_uint])
init_sub_avector = get_func('init_sub_avector', PTR(CStructAVector), [PTR(CStructAVector), PTR(CStructAVector), c_uint, c_uint])
init_zero_avector = get_func('init_zero_avector', PTR(CStructAVector), [PTR(CStructAVector), c_uint])
init_column_avector = get_func('init_column_avector', PTR(CStructAVector), [PTR(CStructAVector), PTR(CStructAMatrix), c_uint])
init_pointer_avector = get_func('init_pointer_avector', PTR(CStructAVector), [PTR(CStructAVector), PTR(field), c_uint])
uninit_avector = get_func('uninit_avector', None, [PTR(CStructAVector)])
new_avector = get_func('new_avector', PTR(CStructAVector), [c_uint])
new_sub_avector = get_func('new_sub_avector', PTR(CStructAVector), [PTR(CStructAVector), c_uint, c_uint])
new_zero_avector = get_func('new_zero_avector', PTR(CStructAVector), [c_uint])
new_pointer_avector = get_func('new_pointer_avector', PTR(CStructAVector), [PTR(field), c_uint])
del_avector = get_func('del_avector', None, [PTR(CStructAVector)])
resize_avector = get_func('resize_avector', None, [PTR(CStructAVector), c_uint])
shrink_avector = get_func('shrink_avector', None, [PTR(CStructAVector), c_uint])
getactives_avector = get_func('getactives_avector', c_uint, [])
getsize_avector = get_func('getsize_avector', c_size_t, [PTR(CStructAVector)])
getsize_heap_avector = get_func('getsize_heap_avector', c_size_t, [PTR(CStructAVector)])
clear_avector = get_func('clear_avector', None, [PTR(CStructAVector)])
fill_avector = get_func('fill_avector', None, [PTR(CStructAVector), field])
random_avector = get_func('random_avector', None, [PTR(CStructAVector)])
random_real_avector = get_func('random_real_avector', None, [PTR(CStructAVector)])
copy_avector = get_func('copy_avector', None, [PTR(CStructAVector), PTR(CStructAVector)])
copy_sub_avector = get_func('copy_sub_avector', None, [PTR(CStructAVector), PTR(CStructAVector)])
print_avector = get_func('print_avector', None, [PTR(CStructAVector)])
scale_avector = get_func('scale_avector', None, [field, PTR(CStructAVector)])
norm2_avector = get_func('norm2_avector', real, [PTR(CStructAVector)])
dotprod_avector = get_func('dotprod_avector', field, [PTR(CStructAVector), PTR(CStructAVector)])
add_avector = get_func('add_avector', None, [field, PTR(CStructAVector), PTR(CStructAVector)])
