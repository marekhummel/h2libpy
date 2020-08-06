from ctypes import CFUNCTYPE
from ctypes import POINTER as PTR
from ctypes import c_bool, c_size_t, c_uint, c_void_p

from h2libpy.lib.settings import field, real
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import (CStructAMatrix, CStructAVector,
                                      CStructBlock, CStructDClusterBasis,
                                      CStructDClusterOperator,
                                      CStructDH2Matrix, CStructDUniform,
                                      CStructTruncMode)

# ------------------------


CFuncDH2MatrixCallbackT = CFUNCTYPE(None, *[PTR(CStructDH2Matrix), c_uint, c_uint, c_uint, c_uint, c_void_p])


# ------------------------


CStructDH2Matrix._fields_ = [
    ('rb', PTR(CStructDClusterBasis)),
    ('cb', PTR(CStructDClusterBasis)),
    ('u', PTR(CStructDUniform)),
    ('f', PTR(CStructAMatrix)),
    ('son', PTR(PTR(CStructDH2Matrix))),
    ('rsons', c_uint),
    ('csons', c_uint),
    ('desc', c_uint),
]


# ------------------------


new_dh2matrix = get_func('new_dh2matrix', PTR(CStructDH2Matrix), [PTR(CStructDClusterBasis), PTR(CStructDClusterBasis)])
new_uniform_dh2matrix = get_func('new_uniform_dh2matrix', PTR(CStructDH2Matrix), [PTR(CStructDClusterBasis), c_uint, PTR(CStructDClusterBasis), c_uint])
new_full_dh2matrix = get_func('new_full_dh2matrix', PTR(CStructDH2Matrix), [PTR(CStructDClusterBasis), PTR(CStructDClusterBasis)])
new_super_dh2matrix = get_func('new_super_dh2matrix', PTR(CStructDH2Matrix), [PTR(CStructDClusterBasis), PTR(CStructDClusterBasis), c_uint, c_uint])
update_dh2matrix = get_func('update_dh2matrix', None, [PTR(CStructDH2Matrix)])
del_dh2matrix = get_func('del_dh2matrix', None, [PTR(CStructDH2Matrix)])
clone_dh2matrix = get_func('clone_dh2matrix', PTR(CStructDH2Matrix), [PTR(CStructDH2Matrix), PTR(CStructDClusterBasis), PTR(CStructDClusterBasis)])
getsize_dh2matrix = get_func('getsize_dh2matrix', c_size_t, [PTR(CStructDH2Matrix)])
getnearsize_dh2matrix = get_func('getnearsize_dh2matrix', c_size_t, [PTR(CStructDH2Matrix)])
getfarsize_dh2matrix = get_func('getfarsize_dh2matrix', c_size_t, [PTR(CStructDH2Matrix)])
gettotalsize_dh2matrix = get_func('gettotalsize_dh2matrix', c_size_t, [PTR(CStructDH2Matrix)])
buildfromblock_dh2matrix = get_func('buildfromblock_dh2matrix', PTR(CStructDH2Matrix), [PTR(CStructBlock), PTR(CStructDClusterBasis), PTR(CStructDClusterBasis)])
copynear_dh2matrix = get_func('copynear_dh2matrix', None, [PTR(CStructAMatrix), PTR(CStructDH2Matrix)])
fastaddeval_dh2matrix_avector = get_func('fastaddeval_dh2matrix_avector', None, [field, PTR(CStructDH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
fastaddevaltrans_dh2matrix_avector = get_func('fastaddevaltrans_dh2matrix_avector', None, [field, PTR(CStructDH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
addeval_dh2matrix_avector = get_func('addeval_dh2matrix_avector', None, [field, PTR(CStructDH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
addevaltrans_dh2matrix_avector = get_func('addevaltrans_dh2matrix_avector', None, [field, PTR(CStructDH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
mvm_dh2matrix_avector = get_func('mvm_dh2matrix_avector', None, [field, c_bool, PTR(CStructDH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
addeval_parallel_dh2matrix_avector = get_func('addeval_parallel_dh2matrix_avector', None, [field, PTR(CStructDH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
addevaltrans_parallel_dh2matrix_avector = get_func('addevaltrans_parallel_dh2matrix_avector', None, [field, PTR(CStructDH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
slowaddeval_dh2matrix_avector = get_func('slowaddeval_dh2matrix_avector', None, [field, PTR(CStructDH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
slowaddevaltrans_dh2matrix_avector = get_func('slowaddevaltrans_dh2matrix_avector', None, [field, PTR(CStructDH2Matrix), PTR(CStructAVector), PTR(CStructAVector)])
expand_dh2matrix = get_func('expand_dh2matrix', None, [field, PTR(CStructDH2Matrix), PTR(CStructAMatrix)])
enumerate_dh2matrix = get_func('enumerate_dh2matrix', PTR(PTR(CStructDH2Matrix)), [PTR(CStructDH2Matrix)])
iterate_dh2matrix = get_func('iterate_dh2matrix', None, [PTR(CStructDH2Matrix), c_uint, c_uint, c_uint, c_uint, CFuncDH2MatrixCallbackT, CFuncDH2MatrixCallbackT, c_void_p])
norm2_dh2matrix = get_func('norm2_dh2matrix', real, [PTR(CStructDH2Matrix)])
norm2diff_dh2matrix = get_func('norm2diff_dh2matrix', real, [PTR(CStructDH2Matrix), PTR(CStructDH2Matrix)])
# draw_cairo_dh2matrix
resize_coupling_dh2matrix = get_func('resize_coupling_dh2matrix', None, [PTR(CStructDH2Matrix), PTR(CStructDClusterOperator), PTR(CStructDClusterOperator)])
build_projected_dh2matrix = get_func('build_projected_dh2matrix', PTR(CStructDH2Matrix), [PTR(CStructDH2Matrix), PTR(CStructDClusterBasis), PTR(CStructDClusterBasis), PTR(CStructDClusterOperator), PTR(CStructDClusterOperator)])
compress_dh2matrix_dh2matrix = get_func('compress_dh2matrix_dh2matrix', PTR(CStructDH2Matrix), [PTR(CStructDH2Matrix), c_bool, c_bool, PTR(CStructTruncMode), real])
truncate_dclusterbasis = get_func('truncate_dclusterbasis', None, [PTR(CStructDClusterBasis), PTR(CStructDClusterBasis), PTR(CStructDClusterOperator), PTR(CStructDClusterOperator), PTR(CStructTruncMode), real])
