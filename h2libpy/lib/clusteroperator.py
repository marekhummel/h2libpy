from ctypes import POINTER as PTR
from ctypes import c_size_t, c_uint

from h2libpy.lib.settings import real
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import (CStructAMatrix, CStructCluster,
                                      CStructClusterBasis,
                                      CStructClusterOperator)

# ------------------------


CStructClusterOperator._fields_ = [
    ('t', PTR(CStructCluster)),
    ('krow', c_uint),
    ('kcol', c_uint),
    ('C', CStructAMatrix),
    ('sons', c_uint),
    ('son', PTR(PTR(CStructClusterOperator))),
    ('refs', c_uint),
]


# ------------------------


init_clusteroperator = get_func('init_clusteroperator', PTR(CStructClusterOperator), [PTR(CStructClusterOperator), PTR(CStructCluster)])
init_leaf_clusteroperator = get_func('init_leaf_clusteroperator', PTR(CStructClusterOperator), [PTR(CStructClusterOperator), PTR(CStructCluster)])
uninit_clusteroperator = get_func('uninit_clusteroperator', None, [PTR(CStructClusterOperator)])
new_clusteroperator = get_func('new_clusteroperator', PTR(CStructClusterOperator), [PTR(CStructCluster)])
new_leaf_clusteroperator = get_func('new_leaf_clusteroperator', PTR(CStructClusterOperator), [PTR(CStructCluster)])
del_clusteroperator = get_func('del_clusteroperator', None, [PTR(CStructClusterOperator)])
removesons_clusteroperator = get_func('removesons_clusteroperator', None, [PTR(CStructClusterOperator)])
ref_clusteroperator = get_func('ref_clusteroperator', None, [PTR(PTR(CStructClusterOperator)), PTR(CStructClusterOperator)])
unref_clusteroperator = get_func('unref_clusteroperator', None, [PTR(CStructClusterOperator)])
update_clusteroperator = get_func('update_clusteroperator', None, [PTR(CStructClusterOperator)])
resize_clusteroperator = get_func('resize_clusteroperator', None, [PTR(CStructClusterOperator), c_uint, c_uint])
identify_son_clusterweight_clusteroperator = get_func('identify_son_clusterweight_clusteroperator', PTR(CStructClusterOperator), [PTR(CStructClusterOperator), PTR(CStructCluster)])
build_from_cluster_clusteroperator = get_func('build_from_cluster_clusteroperator', PTR(CStructClusterOperator), [PTR(CStructCluster)])
build_from_clusterbasis_clusteroperator = get_func('build_from_clusterbasis_clusteroperator', PTR(CStructClusterOperator), [PTR(CStructClusterBasis)])
getactives_clusteroperator = get_func('getactives_clusteroperator', c_uint, [])
getsize_clusteroperator = get_func('getsize_clusteroperator', c_size_t, [PTR(CStructClusterOperator)])
print_tree_clusteroperator = get_func('print_tree_clusteroperator', None, [PTR(CStructClusterOperator)])
norm2diff_clusteroperator = get_func('norm2diff_clusteroperator', None, [PTR(CStructClusterOperator), PTR(CStructClusterOperator)])
compareweights_clusteroperator = get_func('compareweights_clusteroperator', real, [PTR(CStructClusterOperator), PTR(CStructClusterOperator)])
enumerate_clusteroperator = get_func('enumerate_clusteroperator', PTR(PTR(CStructClusterOperator)), [PTR(CStructCluster), PTR(CStructClusterOperator)])
basisproduct_clusteroperator = get_func('basisproduct_clusteroperator', None, [PTR(CStructClusterBasis), PTR(CStructClusterBasis), PTR(CStructClusterOperator)])
