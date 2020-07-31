from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

from h2libpy.lib.util.helper import get_func

# ------------------------


class CStructDClusterOperator(Struct): pass


# ------------------------

from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.dcluster import CStructDCluster
from h2libpy.lib.dclusterbasis import CStructDClusterBasis


CStructDClusterOperator._fields_ = [
    ('t', PTR(CStructDCluster)),
    ('krow', PTR(c_uint)),
    ('kcol', PTR(c_uint)),
    ('dir', c_uint),
    ('C', PTR(CStructAMatrix)),
    ('sons', c_uint),
    ('son', PTR(PTR(CStructDClusterOperator))),
    ('refs', c_uint),
]


# ------------------------


init_dclusteroperator = get_func('init_dclusteroperator', PTR(CStructDClusterOperator), [PTR(CStructDClusterOperator), PTR(CStructDCluster)])
init_leaf_dclusteroperator = get_func('init_leaf_dclusteroperator', PTR(CStructDClusterOperator), [PTR(CStructDClusterOperator), PTR(CStructDCluster)])
uninit_dclusteroperator = get_func('uninit_dclusteroperator', None, [PTR(CStructDClusterOperator)])
new_dclusteroperator = get_func('new_dclusteroperator', PTR(CStructDClusterOperator), [PTR(CStructDCluster)])
ref_dclusteroperator = get_func('ref_dclusteroperator', None, [PTR(PTR(CStructDClusterOperator)), PTR(CStructDClusterOperator)])
unref_dclusteroperator = get_func('unref_dclusteroperator', None, [PTR(CStructDClusterOperator)])
new_leaf_dclusteroperator = get_func('new_leaf_dclusteroperator', PTR(CStructDClusterOperator), [PTR(CStructDCluster)])
del_dclusteroperator = get_func('del_dclusteroperator', None, [PTR(CStructDClusterOperator)])
getactives_dclusteroperator = get_func('getactives_dclusteroperator', c_uint, [])
resize_dclusteroperator = get_func('resize_dclusteroperator', None, [PTR(CStructDClusterOperator), c_uint, c_uint, c_uint])
build_from_dcluster_dclusteroperator = get_func('build_from_dcluster_dclusteroperator', PTR(CStructDClusterOperator), [PTR(CStructDCluster)])
build_from_dclusterbasis_dclusteroperator = get_func('build_from_dclusterbasis_dclusteroperator', PTR(CStructDClusterOperator), [PTR(CStructDClusterBasis)])
merge_dclusteropertator = get_func('merge_dclusteropertator', None, [PTR(CStructDClusterOperator), PTR(CStructDClusterOperator)])
print_tree_dclusteroperator = get_func('print_tree_dclusteroperator', None, [PTR(CStructDClusterOperator)])
enumerate_dclusteroperator = get_func('enumerate_dclusteroperator', PTR(PTR(CStructDClusterOperator)), [PTR(CStructDCluster), PTR(CStructDClusterOperator)])
