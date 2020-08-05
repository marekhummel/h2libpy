from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_bool, c_size_t, c_uint

from h2libpy.lib.settings import field, real
from h2libpy.lib.util.helper import get_func

# ------------------------


class CStructRkMatrix(Struct): pass


# ------------------------


from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.avector import CStructAVector


CStructRkMatrix._fields_ = [
    ('A', CStructAMatrix),
    ('B', CStructAMatrix),
    ('k', c_uint),
]


# ------------------------


init_rkmatrix = get_func('init_rkmatrix', PTR(CStructRkMatrix), [PTR(CStructRkMatrix), c_uint, c_uint, c_uint])
init_sub_rkmatrix = get_func('init_sub_rkmatrix', PTR(CStructRkMatrix), [PTR(CStructRkMatrix), PTR(CStructRkMatrix), c_uint, c_uint, c_uint, c_uint])
uninit_rkmatrix = get_func('uninit_rkmatrix', None, [PTR(CStructRkMatrix)])
new_rkmatrix = get_func('new_rkmatrix', PTR(CStructRkMatrix), [c_uint, c_uint, c_uint])
new_sub_rkmatrix = get_func('new_sub_rkmatrix', PTR(CStructRkMatrix), [PTR(CStructRkMatrix), c_uint, c_uint, c_uint, c_uint])
del_rkmatrix = get_func('del_rkmatrix', None, [PTR(CStructRkMatrix)])
setrank_rkmatrix = get_func('setrank_rkmatrix', None, [PTR(CStructRkMatrix), c_uint])
resize_rkmatrix = get_func('resize_rkmatrix', None, [PTR(CStructRkMatrix), c_uint, c_uint, c_uint])
getsize_rkmatrix = get_func('getsize_rkmatrix', c_size_t, [PTR(CStructRkMatrix)])
getsize_heap_rkmatrix = get_func('getsize_heap_rkmatrix', c_size_t, [PTR(CStructRkMatrix)])
clone_rkmatrix = get_func('clone_rkmatrix', PTR(CStructRkMatrix), [PTR(CStructRkMatrix)])
copy_rkmatrix = get_func('copy_rkmatrix', None, [c_bool, PTR(CStructRkMatrix), PTR(CStructRkMatrix)])
scale_rkmatrix = get_func('scale_rkmatrix', None, [field, PTR(CStructRkMatrix)])
random_rkmatrix = get_func('random_rkmatrix', None, [PTR(CStructRkMatrix), c_uint])
addeval_rkmatrix_avector = get_func('addeval_rkmatrix_avector', None, [field, PTR(CStructRkMatrix), PTR(CStructAVector), PTR(CStructAVector)])
addevaltrans_rkmatrix_avector = get_func('addevaltrans_rkmatrix_avector', None, [field, PTR(CStructRkMatrix), PTR(CStructAVector), PTR(CStructAVector)])
mvm_rkmatrix_avector = get_func('mvm_rkmatrix_avector', None, [field, c_bool, PTR(CStructRkMatrix), PTR(CStructAVector), PTR(CStructAVector)])
norm2_rkmatrix = get_func('norm2_rkmatrix', real, [PTR(CStructRkMatrix)])
norm2diff_rkmatrix = get_func('norm2diff_rkmatrix', real, [PTR(CStructRkMatrix), PTR(CStructRkMatrix)])
