from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_bool, c_size_t, c_uint, c_void_p

from h2libpy.lib.settings import field, real
from h2libpy.lib.util.helper import get_func

# ------------------------


class CStructAMatrix(Struct): pass


# ------------------------

from h2libpy.lib.avector import CStructAVector


CStructAMatrix._fields_ = [
    ('a', PTR(field)),
    ('ld', c_uint),
    ('rows', c_uint),
    ('cols', c_uint),
    ('owner', c_void_p)
]

# ------------------------


init_amatrix = get_func('init_amatrix', PTR(CStructAMatrix), [PTR(CStructAMatrix), c_uint, c_uint])
init_sub_amatrix = get_func('init_sub_amatrix', PTR(CStructAMatrix), [PTR(CStructAMatrix), PTR(CStructAMatrix), c_uint, c_uint, c_uint, c_uint])
init_vec_amatrix = get_func('init_vec_amatrix', PTR(CStructAMatrix), [PTR(CStructAMatrix), PTR(CStructAVector), c_uint, c_uint])
init_pointer_amatrix = get_func('init_pointer_amatrix', PTR(CStructAMatrix), [PTR(CStructAMatrix), PTR(field), c_uint, c_uint])
init_zero_amatrix = get_func('init_zero_amatrix', PTR(CStructAMatrix), [PTR(CStructAMatrix), c_uint, c_uint])
init_identity_amatrix = get_func('init_identity_amatrix', PTR(CStructAMatrix), [PTR(CStructAMatrix), c_uint, c_uint])
uninit_amatrix = get_func('uninit_amatrix', None, [PTR(CStructAMatrix)])
new_amatrix = get_func('new_amatrix', PTR(CStructAMatrix), [c_uint, c_uint])
new_sub_amatrix = get_func('new_sub_amatrix', PTR(CStructAMatrix), [PTR(CStructAMatrix), c_uint, c_uint, c_uint, c_uint])
new_pointer_amatrix = get_func('new_pointer_amatrix', PTR(CStructAMatrix), [PTR(field), c_uint, c_uint])
new_zero_amatrix = get_func('new_zero_amatrix', PTR(CStructAMatrix), [c_uint, c_uint])
new_identity_amatrix = get_func('new_identity_amatrix', PTR(CStructAMatrix), [c_uint, c_uint])
del_amatrix = get_func('del_amatrix', None, [PTR(CStructAMatrix)])
resize_amatrix = get_func('resize_amatrix', None, [PTR(CStructAMatrix), c_uint, c_uint])
resizecopy_amatrix = get_func('resizecopy_amatrix', None, [PTR(CStructAMatrix), c_uint, c_uint])
getactives_amatrix = get_func('getactives_amatrix', c_uint, [])
getsize_amatrix = get_func('getsize_amatrix', c_size_t, [PTR(CStructAMatrix)])
getsize_heap_amatrix = get_func('getsize_heap_amatrix', c_size_t, [PTR(CStructAMatrix)])
clear_amatrix = get_func('clear_amatrix', None, [PTR(CStructAMatrix)])
clear_lower_amatrix = get_func('clear_lower_amatrix', None, [PTR(CStructAMatrix), c_bool])
clear_upper_amatrix = get_func('clear_upper_amatrix', None, [PTR(CStructAMatrix), c_bool])
identity_amatrix = get_func('identity_amatrix', None, [PTR(CStructAMatrix)])
random_amatrix = get_func('random_amatrix', None, [PTR(CStructAMatrix)])
random_invertible_amatrix = get_func('random_invertible_amatrix', None, [PTR(CStructAMatrix), real])
random_selfadjoint_amatrix = get_func('random_selfadjoint_amatrix', None, [PTR(CStructAMatrix)])
random_spd_amatrix = get_func('random_spd_amatrix', None, [PTR(CStructAMatrix), real])
copy_amatrix = get_func('copy_amatrix', None, [c_bool, PTR(CStructAMatrix), PTR(CStructAMatrix)])
copy_colpiv_amatrix = get_func('copy_colpiv_amatrix', None, [c_bool, PTR(CStructAMatrix), PTR(c_uint), PTR(CStructAMatrix)])
clone_amatrix = get_func('clone_amatrix', PTR(CStructAMatrix), [PTR(CStructAMatrix)])
copy_sub_amatrix = get_func('copy_sub_amatrix', None, [c_bool, PTR(CStructAMatrix), PTR(CStructAMatrix)])
print_amatrix = get_func('print_amatrix', None, [PTR(CStructAMatrix)])
print_matlab_amatrix = get_func('print_matlab_amatrix', None, [PTR(CStructAMatrix)])
check_ortho_amatrix = get_func('check_ortho_amatrix', real, [c_bool, PTR(CStructAMatrix)])
scale_amatrix = get_func('scale_amatrix', None, [field, PTR(CStructAMatrix)])
conjugate_amatrix = get_func('conjugate_amatrix', None, [PTR(CStructAMatrix)])
dotprod_amatrix = get_func('dotprod_amatrix', field, [PTR(CStructAMatrix), PTR(CStructAMatrix)])
norm2_amatrix = get_func('norm2_amatrix', real, [PTR(CStructAMatrix)])
normfrob_amatrix = get_func('normfrob_amatrix', real, [PTR(CStructAMatrix)])
normfrob2_amatrix = get_func('normfrob2_amatrix', real, [PTR(CStructAMatrix)])
norm2diff_amatrix = get_func('norm2diff_amatrix', real, [PTR(CStructAMatrix), PTR(CStructAMatrix)])
addeval_amatrix_avector = get_func('addeval_amatrix_avector', None, [field, PTR(CStructAMatrix), PTR(CStructAVector), PTR(CStructAVector)])
addevaltrans_amatrix_avector = get_func('addevaltrans_amatrix_avector', None, [field, PTR(CStructAMatrix), PTR(CStructAVector), PTR(CStructAVector)])
mvm_amatrix_avector = get_func('mvm_amatrix_avector', None, [field, c_bool, PTR(CStructAMatrix), PTR(CStructAVector), PTR(CStructAVector)])
add_amatrix = get_func('add_amatrix', None, [field, c_bool, PTR(CStructAMatrix), PTR(CStructAMatrix)])
addmul_amatrix = get_func('addmul_amatrix', None, [field, c_bool, PTR(CStructAMatrix), c_bool, PTR(CStructAMatrix), PTR(CStructAMatrix)])
bidiagmul_amatrix = get_func('bidiagmul_amatrix', None, [field, c_bool, PTR(CStructAMatrix), PTR(CStructAVector), PTR(CStructAVector)])
