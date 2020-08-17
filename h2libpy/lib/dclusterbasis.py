from ctypes import CFUNCTYPE
from ctypes import POINTER as PTR
from ctypes import c_size_t, c_uint, c_void_p

from h2libpy.lib.settings import field, real
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import (CStructAMatrix, CStructAVector,
                                      CStructDBlock, CStructDCluster,
                                      CStructDClusterBasis,
                                      CStructDClusterOperator)

# ------------------------


CFuncDClusterBasisCallbackT = CFUNCTYPE(None, *(PTR(CStructDClusterBasis), c_uint, c_uint, c_void_p))


# ------------------------


CStructDClusterBasis._fields_ = [
    ('t', PTR(CStructDCluster)),
    ('directions', c_uint),
    ('k', PTR(c_uint)),
    ('koff', PTR(c_uint)),
    ('ktree', c_uint),
    ('kbranch', c_uint),
    ('V', PTR(CStructAMatrix)),
    ('E', PTR(PTR(CStructAMatrix))),
    ('sons', c_uint),
    ('son', PTR(PTR(CStructDClusterBasis))),
    ('dirson', PTR(PTR(c_uint))),
]


# ------------------------


init_dclusterbasis = get_func('init_dclusterbasis', PTR(CStructDClusterBasis), [PTR(CStructDClusterBasis), PTR(CStructDCluster)])
uninit_dclusterbasis = get_func('uninit_dclusterbasis', None, [PTR(CStructDClusterBasis)])
new_dclusterbasis = get_func('new_dclusterbasis', PTR(CStructDClusterBasis), [PTR(CStructDCluster)])
del_dclusterbasis = get_func('del_dclusterbasis', None, [PTR(CStructDClusterBasis)])
update_dclusterbasis = get_func('update_dclusterbasis', None, [PTR(CStructDClusterBasis)])
setrank_dclusterbasis = get_func('setrank_dclusterbasis', None, [PTR(CStructDClusterBasis), c_uint, c_uint])
initmatrices_dclusterbasis = get_func('initmatrices_dclusterbasis', None, [PTR(CStructDClusterBasis)])
findranks_dclusterbasis = get_func('findranks_dclusterbasis', None, [c_uint, PTR(CStructDBlock), PTR(CStructDClusterBasis), PTR(CStructDClusterBasis)])
getactives_dclusterbasis = get_func('getactives_dclusterbasis', c_uint, [])
getsize_dclusterbasis = get_func('getsize_dclusterbasis', c_size_t, [PTR(CStructDClusterBasis)])
getsize_nonrecursive_dclusterbasis = get_func('getsize_nonrecursive_dclusterbasis', c_size_t, [PTR(CStructDClusterBasis)])
getmaxrank_dclusterbasis = get_func('getmaxrank_dclusterbasis', c_uint, [PTR(CStructDClusterBasis)])
getactivedirections_dclusterbasis = get_func('getactivedirections_dclusterbasis', c_uint, [PTR(CStructDClusterBasis)])
print_tree_dclusterbasis = get_func('print_tree_dclusterbasis', None, [PTR(CStructDClusterBasis)])
buildfromdcluster_dclusterbasis = get_func('buildfromdcluster_dclusterbasis', PTR(CStructDClusterBasis), [PTR(CStructDCluster)])
newcoeffs_dclusterbasis = get_func('newcoeffs_dclusterbasis', PTR(CStructAVector), [PTR(CStructDClusterBasis)])
forward_dclusterbasis = get_func('forward_dclusterbasis', None, [PTR(CStructDClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
backward_dclusterbasis = get_func('backward_dclusterbasis', None, [PTR(CStructDClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
slowforward_dclusterbasis = get_func('slowforward_dclusterbasis', None, [PTR(CStructDClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
slowbackward_dclusterbasis = get_func('slowbackward_dclusterbasis', None, [PTR(CStructDClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
compress_dclusterbasis = get_func('compress_dclusterbasis', None, [PTR(CStructDClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
expand_dclusterbasis = get_func('expand_dclusterbasis', None, [field, PTR(CStructDClusterBasis), PTR(CStructAVector), PTR(CStructAVector)])
blockcompress_dclusterbasis = get_func('blockcompress_dclusterbasis', None, [PTR(CStructDClusterBasis), PTR(CStructAMatrix), PTR(CStructAMatrix)])
blockexpand_dclusterbasis = get_func('blockexpand_dclusterbasis', None, [field, PTR(CStructDClusterBasis), PTR(CStructAMatrix), PTR(CStructAMatrix)])
enumerate_dclusterbasis = get_func('enumerate_dclusterbasis', PTR(PTR(CStructDClusterBasis)), [PTR(CStructDCluster), PTR(CStructDClusterBasis)])
iterate_dclusterbasis = get_func('iterate_dclusterbasis', None, [PTR(CStructDClusterBasis), c_uint, c_uint, CFuncDClusterBasisCallbackT, CFuncDClusterBasisCallbackT, c_void_p])
ortho_dclusterbasis = get_func('ortho_dclusterbasis', None, [PTR(CStructDClusterBasis), PTR(CStructDClusterOperator)])
weight_dclusterbasis_dclusteroperator = get_func('weight_dclusterbasis_dclusteroperator', None, [PTR(CStructDClusterBasis), PTR(CStructDClusterOperator)])
check_ortho_dclusterbasis = get_func('check_ortho_dclusterbasis', real, [PTR(CStructDClusterBasis)])
clone_structure_dclusterbasis = get_func('clone_structure_dclusterbasis', PTR(CStructDClusterBasis), [PTR(CStructDClusterBasis)])
duplicate_dclusterbasis = get_func('duplicate_dclusterbasis', PTR(CStructDClusterBasis), [PTR(CStructDClusterBasis)])
