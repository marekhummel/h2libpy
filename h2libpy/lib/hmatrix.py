from ctypes import POINTER as PTR
from ctypes import c_bool, c_char_p, c_size_t, c_uint

from h2libpy.lib.settings import field, real
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import (CStructAMatrix, CStructAVector,
                                      CStructBlock, CStructCluster,
                                      CStructHMatrix, CStructRkMatrix,
                                      CStructSparseMatrix)

# ------------------------


CStructHMatrix._fields_ = [
    ('rc', PTR(CStructCluster)),
    ('cc', PTR(CStructCluster)),
    ('r', PTR(CStructRkMatrix)),
    ('f', PTR(CStructAMatrix)),
    ('son', PTR(PTR(CStructHMatrix))),
    ('rsons', c_uint),
    ('csons', c_uint),
    ('refs', c_uint),
    ('desc', c_uint),
]


# ------------------------


init_hmatrix = get_func('init_hmatrix', PTR(CStructHMatrix), [PTR(CStructHMatrix), PTR(CStructCluster), PTR(CStructCluster)])
uninit_hmatrix = get_func('uninit_hmatrix', None, [PTR(CStructHMatrix)])
new_hmatrix = get_func('new_hmatrix', PTR(CStructHMatrix), [PTR(CStructCluster), PTR(CStructCluster)])
new_rk_hmatrix = get_func('new_rk_hmatrix', PTR(CStructHMatrix), [PTR(CStructCluster), PTR(CStructCluster), c_uint])
new_full_hmatrix = get_func('new_full_hmatrix', PTR(CStructHMatrix), [PTR(CStructCluster), PTR(CStructCluster)])
new_super_hmatrix = get_func('new_super_hmatrix', PTR(CStructHMatrix), [PTR(CStructCluster), PTR(CStructCluster), c_uint, c_uint])
clone_hmatrix = get_func('clone_hmatrix', PTR(CStructHMatrix), [PTR(CStructHMatrix)])
clonestructure_hmatrix = get_func('clonestructure_hmatrix', PTR(CStructHMatrix), [PTR(CStructHMatrix)])
update_hmatrix = get_func('update_hmatrix', None, [PTR(CStructHMatrix)])
del_hmatrix = get_func('del_hmatrix', None, [PTR(CStructHMatrix)])
ref_hmatrix = get_func('ref_hmatrix', None, [PTR(PTR(CStructHMatrix)), PTR(CStructHMatrix)])
unref_hmatrix = get_func('unref_hmatrix', None, [PTR(CStructHMatrix)])
getsize_hmatrix = get_func('getsize_hmatrix', c_size_t, [PTR(CStructHMatrix)])
getnearsize_hmatrix = get_func('getnearsize_hmatrix', c_size_t, [PTR(CStructHMatrix)])
getfarsize_hmatrix = get_func('getfarsize_hmatrix', c_size_t, [PTR(CStructHMatrix)])
clear_hmatrix = get_func('clear_hmatrix', None, [PTR(CStructHMatrix)])
clear_upper_hmatrix = get_func('clear_upper_hmatrix', None, [PTR(CStructHMatrix), c_bool])
copy_hmatrix = get_func('copy_hmatrix', None, [PTR(CStructHMatrix), PTR(CStructHMatrix)])
identity_hmatrix = get_func('identity_hmatrix', None, [PTR(CStructHMatrix)])
random_hmatrix = get_func('random_hmatrix', None, [PTR(CStructHMatrix), c_uint])
build_from_block_hmatrix = get_func('build_from_block_hmatrix', PTR(CStructHMatrix), [PTR(CStructBlock), c_uint])
build_from_hmatrix_block = get_func('build_from_hmatrix_block', PTR(CStructBlock), [PTR(CStructHMatrix)])
mvm_hmatrix_avector = get_func('mvm_hmatrix_avector', None, [field, c_bool, PTR(CStructHMatrix), PTR(CStructAVector), PTR(CStructAVector)])
fastaddeval_hmatrix_avector = get_func('fastaddeval_hmatrix_avector', None, [field, PTR(CStructHMatrix), PTR(CStructAVector), PTR(CStructAVector)])
addeval_hmatrix_avector = get_func('addeval_hmatrix_avector', None, [field, PTR(CStructHMatrix), PTR(CStructAVector), PTR(CStructAVector)])
fastaddevaltrans_hmatrix_avector = get_func('fastaddevaltrans_hmatrix_avector', None, [field, PTR(CStructHMatrix), PTR(CStructAVector), PTR(CStructAVector)])
addevaltrans_hmatrix_avector = get_func('addevaltrans_hmatrix_avector', None, [field, PTR(CStructHMatrix), PTR(CStructAVector), PTR(CStructAVector)])
fastaddevalsymm_hmatrix_avector = get_func('fastaddevalsymm_hmatrix_avector', None, [field, PTR(CStructHMatrix), PTR(CStructAVector), PTR(CStructAVector)])
addevalsymm_hmatrix_avector = get_func('addevalsymm_hmatrix_avector', None, [field, PTR(CStructHMatrix), PTR(CStructAVector), PTR(CStructAVector)])
enumerate_hmatrix = get_func('enumerate_hmatrix', PTR(PTR(CStructHMatrix)), [PTR(CStructBlock), PTR(CStructHMatrix)])
norm2_hmatrix = get_func('norm2_hmatrix', real, [PTR(CStructHMatrix)])
norm2diff_hmatrix = get_func('norm2diff_hmatrix', real, [PTR(CStructHMatrix), PTR(CStructHMatrix)])
# write_cdf_hmatrix = get_func('write_cdf_hmatrix', None, [PTR(CStructHMatrix), c_char_p])
# write_cdfpart_hmatrix = get_func('write_cdfpart_hmatrix', None, [PTR(CStructHMatrix), c_int, c_char_p])
# read_cdf_hmatrix = get_func('read_cdf_hmatrix', PTR(CStructHMatrix), [c_char_p, PTR(CStructCluster), PTR(CStructCluster)])
# read_cdfpart_hmatrix = get_func('read_cdfpart_hmatrix', PTR(CStructHMatrix), [c_int, c_char_p, PTR(CStructCluster), PTR(CStructCluster)])
# write_cdfcomplete_hmatrix = get_func('write_cdfcomplete_hmatrix', None, [PTR(CStructHMatrix), c_char_p])
# read_cdfcomplete_hmatrix = get_func('read_cdfcomplete_hmatrix', PTR(CStructHMatrix), [c_char_p])
write_hlib_hmatrix = get_func('write_hlib_hmatrix', None, [PTR(CStructHMatrix), c_char_p])
read_hlib_hmatrix = get_func('read_hlib_hmatrix', PTR(CStructHMatrix), [c_char_p])
read_hlibsymm_hmatrix = get_func('read_hlibsymm_hmatrix', PTR(CStructHMatrix), [c_char_p])
# draw_cairo_hmatrix
copy_sparsematrix_hmatrix = get_func('copy_sparsematrix_hmatrix', None, [PTR(CStructSparseMatrix), PTR(CStructHMatrix)])
