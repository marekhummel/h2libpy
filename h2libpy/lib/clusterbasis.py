from ctypes import CFUNCTYPE
from ctypes import POINTER as PTR
from ctypes import c_size_t, c_uint, c_void_p

from h2libpy.lib.settings import field, real
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import (CStructAMatrix, CStructAVector,
                                      CStructCluster, CStructClusterBasis,
                                      CStructClusterOperator, CStructUniform)

# ------------------------


CFuncClusterBasisCallbackT = CFUNCTYPE(None, *(PTR(CStructClusterBasis), c_uint, c_void_p))


# ------------------------


CStructClusterBasis._fields_ = [
    ('t', PTR(CStructCluster)),
    ('k', c_uint),
    ('ktree', c_uint),
    ('kbranch', c_uint),
    ('V', CStructAMatrix),
    ('E', CStructAMatrix),
    ('sons', c_uint),
    ('son', PTR(PTR(CStructClusterBasis))),
    ('Z', PTR(CStructAMatrix)),
    ('refs', c_uint),
    ('rlist', PTR(CStructUniform)),
    ('clist', PTR(CStructUniform))
]


# ------------------------


init_clusterbasis = get_func('init_clusterbasis', PTR(CStructClusterBasis), [PTR(CStructClusterBasis), PTR(CStructCluster)])
init_leaf_clusterbasis = get_func('init_leaf_clusterbasis', PTR(CStructClusterBasis), [PTR(CStructClusterBasis), PTR(CStructCluster)])
init_sub_clusterbasis = get_func('init_sub_clusterbasis', PTR(CStructClusterBasis), [PTR(CStructClusterBasis), PTR(CStructClusterBasis), PTR(CStructCluster), c_uint])
uninit_clusterbasis = get_func('uninit_clusterbasis', None, [PTR(CStructClusterBasis)])
new_clusterbasis = get_func('new_clusterbasis', PTR(CStructClusterBasis), [PTR(CStructCluster)])
new_leaf_clusterbasis = get_func('new_leaf_clusterbasis', PTR(CStructClusterBasis), [PTR(CStructCluster)])
del_clusterbasis = get_func('del_clusterbasis', None, [PTR(CStructClusterBasis)])
ref_clusterbasis = get_func('ref_clusterbasis', None, [PTR(PTR(CStructClusterBasis)), PTR(CStructClusterBasis)])
unref_clusterbasis = get_func('unref_clusterbasis', None, [PTR(CStructClusterBasis)])
update_clusterbasis = get_func('update_clusterbasis', None, [PTR(CStructClusterBasis)])
update_tree_clusterbasis = get_func('update_tree_clusterbasis', None, [PTR(CStructClusterBasis)])
resize_clusterbasis = get_func('resize_clusterbasis', None, [PTR(CStructClusterBasis), c_uint])
setrank_clusterbasis = get_func('setrank_clusterbasis', None, [PTR(CStructClusterBasis), c_uint])
build_from_cluster_clusterbasis = get_func('build_from_cluster_clusterbasis', PTR(CStructClusterBasis), [PTR(CStructCluster)])
clone_clusterbasis = get_func('clone_clusterbasis', PTR(CStructClusterBasis), [PTR(CStructClusterBasis)])
clonestructure_clusterbasis = get_func('clonestructure_clusterbasis', PTR(CStructClusterBasis), [PTR(CStructClusterBasis)])
getactives_clusterbasis = get_func('getactives_clusterbasis', c_uint, [])
getsize_clusterbasis = get_func('getsize_clusterbasis', c_size_t, [PTR(CStructClusterBasis)])
clear_weight_clusterbasis = get_func('clear_weight_clusterbasis', None, [PTR(CStructClusterBasis)])
iterate_clusterbasis = get_func('iterate_clusterbasis', None, [PTR(CStructClusterBasis), c_uint, CFuncClusterBasisCallbackT, CFuncClusterBasisCallbackT, c_void_p])
iterate_parallel_clusterbasis = get_func('iterate_parallel_clusterbasis', None, [PTR(CStructClusterBasis), c_uint, c_uint, CFuncClusterBasisCallbackT, CFuncClusterBasisCallbackT, c_void_p])
enumerate_clusterbasis = get_func('enumerate_clusterbasis', PTR(PTR(CStructClusterBasis)), [PTR(CStructCluster), PTR(CStructClusterBasis)])
new_coeffs_clusterbasis_avector = get_func('new_coeffs_clusterbasis_avector', PTR(CStructAVector), [PTR(CStructClusterBasis)])
forward_clusterbasis_avector = get_func('forward_clusterbasis_avector', None, [PTR(CStructClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
forward_parallel_clusterbasis_avector = get_func('forward_parallel_clusterbasis_avector', None, [PTR(CStructClusterBasis), PTR(CStructAVector), PTR(CStructAVector), c_uint])
forward_nopermutation_clusterbasis_avector = get_func('forward_nopermutation_clusterbasis_avector', None, [PTR(CStructClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
forward_notransfer_clusterbasis_avector = get_func('forward_notransfer_clusterbasis_avector', None, [PTR(CStructClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
backward_clusterbasis_avector = get_func('backward_clusterbasis_avector', None, [PTR(CStructClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
backward_parallel_clusterbasis_avector = get_func('backward_parallel_clusterbasis_avector', None, [PTR(CStructClusterBasis), PTR(CStructAVector), PTR(CStructAVector), c_uint])
backward_nopermutation_clusterbasis_avector = get_func('backward_nopermutation_clusterbasis_avector', None, [PTR(CStructClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
backward_notransfer_clusterbasis_avector = get_func('backward_notransfer_clusterbasis_avector', None, [PTR(CStructClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
compress_clusterbasis_avector = get_func('compress_clusterbasis_avector', None, [PTR(CStructClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
expand_clusterbasis_avector = get_func('expand_clusterbasis_avector', None, [PTR(CStructClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
compress_clusterbasis_amatrix = get_func('compress_clusterbasis_amatrix', None, [PTR(CStructClusterBasis), PTR(CStructAMatrix), PTR(CStructAMatrix)])
compress_parallel_clusterbasis_amatrix = get_func('compress_parallel_clusterbasis_amatrix', None, [PTR(CStructClusterBasis), PTR(CStructAMatrix), PTR(CStructAMatrix), c_uint])
forward_clusterbasis_amatrix = get_func('forward_clusterbasis_amatrix', None, [PTR(CStructClusterBasis), PTR(CStructAMatrix), PTR(CStructAMatrix)])
forward_clusterbasis_trans_amatrix = get_func('forward_clusterbasis_trans_amatrix', None, [PTR(CStructClusterBasis), PTR(CStructAMatrix), PTR(CStructAMatrix)])
backward_clusterbasis_amatrix = get_func('backward_clusterbasis_amatrix', None, [PTR(CStructClusterBasis), PTR(CStructAMatrix), PTR(CStructAMatrix)])
backward_clusterbasis_trans_amatrix = get_func('backward_clusterbasis_trans_amatrix', None, [PTR(CStructClusterBasis), PTR(CStructAMatrix), PTR(CStructAMatrix)])
addeval_clusterbasis_avector = get_func('addeval_clusterbasis_avector', None, [field, PTR(CStructClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
addevaltrans_clusterbasis_avector = get_func('addevaltrans_clusterbasis_avector', None, [field, PTR(CStructClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
ortho_clusterbasis = get_func('ortho_clusterbasis', None, [PTR(CStructClusterBasis), PTR(CStructClusterOperator)])
check_ortho_clusterbasis = get_func('check_ortho_clusterbasis', real, [PTR(CStructClusterBasis)])
weight_clusterbasis_clusteroperator = get_func('weight_clusterbasis_clusteroperator', PTR(CStructClusterOperator), [PTR(CStructClusterBasis), PTR(CStructClusterOperator)])
weight_enum_clusterbasis_clusteroperator = get_func('weight_enum_clusterbasis_clusteroperator', PTR(CStructAMatrix), [PTR(CStructClusterBasis)])
# write_cdf_clusterbasis = get_func('write_cdf_clusterbasis', None, [PTR(CStructClusterBasis), c_char_p])
# write_cdfpart_clusterbasis = get_func('write_cdfpart_clusterbasis', None, [PTR(CStructClusterBasis), c_int, c_char_p])
# read_cdf_clusterbasis = get_func('read_cdf_clusterbasis', PTR(CStructClusterBasis), [c_char_p, PTR(CStructCluster)])
# read_cdfpart_clusterbasis = get_func('read_cdfpart_clusterbasis', PTR(CStructClusterBasis), [c_int, c_char_p, PTR(CStructCluster)])
