from ctypes import CFUNCTYPE
from ctypes import POINTER as PTR
from ctypes import c_bool, c_size_t, c_uint, c_void_p

from h2libpy.lib.settings import field, real
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import (CStructAMatrix, CStructAVector,
                                      CStructBlock, CStructCluster,
                                      CStructClusterBasis, CStructH2Matrix,
                                      CStructH2MatrixList, CStructHMatrix,
                                      CStructUniform)

# ------------------------


CFuncH2MatrixCallbackT = CFUNCTYPE(None, *[PTR(CStructH2Matrix), c_uint, c_uint, c_uint, c_uint, c_void_p])
CFuncH2MatrixListCallbackT = CFUNCTYPE(None, *[PTR(CStructCluster), c_uint, c_uint, PTR(CStructH2MatrixList), c_void_p])


# ------------------------


CStructH2Matrix._fields_ = [
    ('rb', PTR(CStructClusterBasis)),
    ('cb', PTR(CStructClusterBasis)),
    ('u', PTR(CStructUniform)),
    ('f', PTR(CStructAMatrix)),
    ('son', PTR(PTR(CStructH2Matrix))),
    ('rsons', c_uint),
    ('csons', c_uint),
    ('refs', c_uint),
    ('desc', c_uint),
]

CStructH2MatrixList._fields_ = [
    ('G', PTR(CStructH2Matrix)),
    ('mname', c_uint),
    ('rname', c_uint),
    ('cname', c_uint),
    ('father', PTR(CStructH2MatrixList)),
    ('next', PTR(CStructH2MatrixList)),
]


# ------------------------


new_h2matrix = get_func('new_h2matrix', PTR(CStructH2Matrix), [PTR(CStructClusterBasis), PTR(CStructClusterBasis)])
new_uniform_h2matrix = get_func('new_uniform_h2matrix', PTR(CStructH2Matrix), [PTR(CStructClusterBasis), PTR(CStructClusterBasis)])
new_full_h2matrix = get_func('new_full_h2matrix', PTR(CStructH2Matrix), [PTR(CStructClusterBasis), PTR(CStructClusterBasis)])
new_super_h2matrix = get_func('new_super_h2matrix', PTR(CStructH2Matrix), [PTR(CStructClusterBasis), PTR(CStructClusterBasis), c_uint, c_uint])
new_zero_h2matrix = get_func('new_zero_h2matrix', PTR(CStructH2Matrix), [PTR(CStructClusterBasis), PTR(CStructClusterBasis)])
clonestructure_h2matrix = get_func('clonestructure_h2matrix', PTR(CStructH2Matrix), [PTR(CStructH2Matrix), PTR(CStructClusterBasis), PTR(CStructClusterBasis)])
clone_h2matrix = get_func('clone_h2matrix', PTR(CStructH2Matrix), [PTR(CStructH2Matrix), PTR(CStructClusterBasis), PTR(CStructClusterBasis)])
update_h2matrix = get_func('update_h2matrix', None, [PTR(CStructH2Matrix)])
del_h2matrix = get_func('del_h2matrix', None, [PTR(CStructH2Matrix)])
ref_h2matrix = get_func('ref_h2matrix', None, [PTR(PTR(CStructH2Matrix)), PTR(CStructH2Matrix)])
unref_h2matrix = get_func('unref_h2matrix', None, [PTR(CStructH2Matrix)])
getsize_h2matrix = get_func('getsize_h2matrix', c_size_t, [PTR(CStructH2Matrix)])
gettotalsize_h2matrix = get_func('gettotalsize_h2matrix', c_size_t, [PTR(CStructH2Matrix)])
getnearsize_h2matrix = get_func('getnearsize_h2matrix', c_size_t, [PTR(CStructH2Matrix)])
getfarsize_h2matrix = get_func('getfarsize_h2matrix', c_size_t, [PTR(CStructH2Matrix)])
clear_h2matrix = get_func('clear_h2matrix', None, [PTR(CStructH2Matrix)])
scale_h2matrix = get_func('scale_h2matrix', None, [field, PTR(CStructH2Matrix)])
random_h2matrix = get_func('random_h2matrix', None, [PTR(CStructH2Matrix)])
build_from_block_h2matrix = get_func('build_from_block_h2matrix', PTR(CStructH2Matrix), [PTR(CStructBlock), PTR(CStructClusterBasis), PTR(CStructClusterBasis)])
build_from_h2matrix_block = get_func('build_from_h2matrix_block', PTR(CStructBlock), [PTR(CStructH2Matrix)])
enumerate_h2matrix = get_func('enumerate_h2matrix', PTR(PTR(CStructH2Matrix)), [PTR(CStructH2Matrix)])
iterate_h2matrix = get_func('iterate_h2matrix', None, [PTR(CStructH2Matrix), c_uint, c_uint, c_uint, c_uint, CFuncH2MatrixCallbackT, CFuncH2MatrixCallbackT, c_void_p])
iterate_rowlist_h2matrix = get_func('iterate_rowlist_h2matrix', None, [PTR(CStructH2Matrix), c_uint, c_uint, c_uint, c_uint, CFuncH2MatrixListCallbackT, CFuncH2MatrixListCallbackT, c_void_p])
iterate_collist_h2matrix = get_func('iterate_collist_h2matrix', None, [PTR(CStructH2Matrix), c_uint, c_uint, c_uint, c_uint, CFuncH2MatrixListCallbackT, CFuncH2MatrixListCallbackT, c_void_p])
iterate_byrow_h2matrix = get_func('iterate_byrow_h2matrix', None, [PTR(CStructH2Matrix), c_uint, c_uint, c_uint, c_uint, CFuncH2MatrixCallbackT, CFuncH2MatrixCallbackT, c_void_p])
iterate_bycol_h2matrix = get_func('iterate_bycol_h2matrix', None, [PTR(CStructH2Matrix), c_uint, c_uint, c_uint, c_uint, CFuncH2MatrixCallbackT, CFuncH2MatrixCallbackT, c_void_p])
mvm_h2matrix_avector = get_func('mvm_h2matrix_avector', None, [field, c_bool, PTR(CStructH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
fastaddeval_h2matrix_avector = get_func('fastaddeval_h2matrix_avector', None, [field, PTR(CStructH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
addeval_h2matrix_avector = get_func('addeval_h2matrix_avector', None, [field, PTR(CStructH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
fastaddevaltrans_h2matrix_avector = get_func('fastaddevaltrans_h2matrix_avector', None, [field, PTR(CStructH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
addevaltrans_h2matrix_avector = get_func('addevaltrans_h2matrix_avector', None, [field, PTR(CStructH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
addevalsymm_h2matrix_avector = get_func('addevalsymm_h2matrix_avector', None, [field, PTR(CStructH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
fastaddmul_h2matrix_amatrix_amatrix = get_func('fastaddmul_h2matrix_amatrix_amatrix', None, [field, c_bool, PTR(CStructH2Matrix), PTR(CStructAMatrix), PTR(CStructAMatrix)])
addmul_h2matrix_amatrix_amatrix = get_func('addmul_h2matrix_amatrix_amatrix', None, [field, c_bool, PTR(CStructH2Matrix), c_bool, PTR(CStructAMatrix), PTR(CStructAMatrix)])
addmul_amatrix_h2matrix_amatrix = get_func('addmul_amatrix_h2matrix_amatrix', None, [field, c_bool, PTR(CStructAMatrix), c_bool, PTR(CStructH2Matrix), PTR(CStructAMatrix)])
collectdense_h2matrix = get_func('collectdense_h2matrix', None, [PTR(CStructAMatrix), PTR(CStructClusterBasis), PTR(CStructClusterBasis), PTR(CStructAMatrix)])
project_amatrix_h2matrix = get_func('project_amatrix_h2matrix', None, [PTR(CStructH2Matrix), PTR(CStructAMatrix)])
project_hmatrix_h2matrix = get_func('project_hmatrix_h2matrix', None, [PTR(CStructH2Matrix), PTR(CStructHMatrix)])
norm2_h2matrix = get_func('norm2_h2matrix', real, [PTR(CStructH2Matrix)])
norm2diff_h2matrix = get_func('norm2diff_h2matrix', real, [PTR(CStructH2Matrix), PTR(CStructH2Matrix)])
# write_cdf_h2matrix = get_func('write_cdf_h2matrix', None, [PTR(CStructH2Matrix), c_char_p])
# write_cdfpart_h2matrix = get_func('write_cdfpart_h2matrix', None, [PTR(CStructH2Matrix), c_int, c_char_p])
# read_cdf_h2matrix = get_func('read_cdf_h2matrix', PTR(CStructH2Matrix), [c_char_p, PTR(CStructClusterBasis), PTR(CStructClusterBasis)])
# read_cdfpart_h2matrix = get_func('read_cdfpart_h2matrix', PTR(CStructH2Matrix), [c_int, c_char_p, PTR(CStructClusterBasis), PTR(CStructClusterBasis)])
# write_cdfcomplete_h2matrix = get_func('write_cdfcomplete_h2matrix', None, [PTR(CStructH2Matrix), c_char_p])
# read_cdfcomplete_h2matrix = get_func('read_cdfcomplete_h2matrix', PTR(CStructH2Matrix), [c_char_p])
# draw_cairo_h2matrix
