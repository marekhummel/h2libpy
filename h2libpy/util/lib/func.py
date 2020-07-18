from h2libpy.util.lib.helper import get_func
import h2libpy.util.lib.structs as struct
from ctypes import c_uint, c_void_p, c_double, POINTER as PTR


# avector.h
new_avector = get_func('new_avector', PTR(struct.LibAVector), [c_uint])
del_avector = get_func('del_avector', None, [PTR(struct.LibAVector)])
init_sub_avector = get_func('init_sub_avector', PTR(struct.LibAVector), [PTR(struct.LibAVector), PTR(struct.LibAVector), c_uint, c_uint])
fill_avector = get_func('fill_avector', None, [PTR(struct.LibAVector), c_double])
random_avector = get_func('random_avector', None, [PTR(struct.LibAVector)])
norm2_avector = get_func('norm2_avector', c_double, [PTR(struct.LibAVector)])
resize_avector = get_func('resize_avector', None, [PTR(struct.LibAVector), c_uint])
