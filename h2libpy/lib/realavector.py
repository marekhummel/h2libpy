from ctypes import POINTER as PTR
from ctypes import c_size_t, c_uint, c_void_p

from h2libpy.lib.settings import real
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import CStructRealAVector

# ------------------------


CStructRealAVector._fields_ = [
    ('v', PTR(real)),
    ('dim', c_uint),
    ('owner', c_void_p)
]


# ------------------------


init_realavector = get_func('init_realavector', PTR(CStructRealAVector), [PTR(CStructRealAVector), c_uint])
init_sub_realavector = get_func('init_sub_realavector', PTR(CStructRealAVector), [PTR(CStructRealAVector), PTR(CStructRealAVector), c_uint, c_uint])
init_pointer_realavector = get_func('init_pointer_realavector', PTR(CStructRealAVector), [PTR(CStructRealAVector), PTR(real), c_uint])
uninit_realavector = get_func('uninit_realavector', None, [PTR(CStructRealAVector)])
new_realavector = get_func('new_realavector', PTR(CStructRealAVector), [c_uint])
new_sub_realavector = get_func('new_sub_realavector', PTR(CStructRealAVector), [PTR(CStructRealAVector), c_uint, c_uint])
new_pointer_realavector = get_func('new_pointer_realavector', PTR(CStructRealAVector), [PTR(real), c_uint])
del_realavector = get_func('del_realavector', None, [PTR(CStructRealAVector)])
resize_realavector = get_func('resize_realavector', None, [PTR(CStructRealAVector), c_uint])
shrink_realavector = get_func('shrink_realavector', None, [PTR(CStructRealAVector), c_uint])
getactives_realavector = get_func('getactives_realavector', c_uint, [])
getsize_realavector = get_func('getsize_realavector', c_size_t, [PTR(CStructRealAVector)])
getsize_heap_realavector = get_func('getsize_heap_realavector', c_size_t, [PTR(CStructRealAVector)])
clear_realavector = get_func('clear_realavector', None, [PTR(CStructRealAVector)])
fill_realavector = get_func('fill_realavector', None, [PTR(CStructRealAVector), real])
random_realavector = get_func('random_realavector', None, [PTR(CStructRealAVector)])
copy_realavector = get_func('copy_realavector', None, [PTR(CStructRealAVector), PTR(CStructRealAVector)])
copy_sub_realavector = get_func('copy_sub_realavector', None, [PTR(CStructRealAVector), PTR(CStructRealAVector)])
print_realavector = get_func('print_realavector', None, [PTR(CStructRealAVector)])
scale_realavector = get_func('scale_realavector', None, [real, PTR(CStructRealAVector)])
norm2_realavector = get_func('norm2_realavector', real, [PTR(CStructRealAVector)])
dotprod_realavector = get_func('dotprod_realavector', real, [PTR(CStructRealAVector), PTR(CStructRealAVector)])
add_realavector = get_func('add_realavector', None, [real, PTR(CStructRealAVector), PTR(CStructRealAVector)])
