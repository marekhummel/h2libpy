from ctypes import CFUNCTYPE
from ctypes import POINTER as PTR
from ctypes import c_uint, c_void_p

from h2libpy.lib.settings import real
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import (CEnumClusterMode, CStructCluster,
                                      CStructClusterGeometry)

# ------------------------


CFuncClusterCallbackT = CFUNCTYPE(None, *(PTR(CStructCluster), c_uint, c_void_p))

CEnumClusterMode.H2_ADAPTIVE = CEnumClusterMode(0)
CEnumClusterMode.H2_REGULAR = CEnumClusterMode(1)
CEnumClusterMode.H2_SIMSUB = CEnumClusterMode(2)
CEnumClusterMode.H2_PCA = CEnumClusterMode(3)


# ------------------------


CStructCluster._fields_ = [
    ('size', c_uint),
    ('idx', PTR(c_uint)),
    ('sons', c_uint),
    ('dim', c_uint),
    ('bmin', PTR(real)),
    ('bmax', PTR(real)),
    ('desc', c_uint),
    ('type', c_uint),
]


# ------------------------


new_cluster = get_func('new_cluster', PTR(CStructCluster), [c_uint, PTR(c_uint), c_uint, c_uint])
del_cluster = get_func('del_cluster', None, [PTR(CStructCluster)])
update_cluster = get_func('update_cluster', None, [PTR(CStructCluster)])
build_adaptive_cluster = get_func('build_adaptive_cluster', PTR(CStructCluster), [PTR(CStructClusterGeometry), c_uint, PTR(c_uint), c_uint])
build_regular_cluster = get_func('build_regular_cluster', PTR(CStructCluster), [PTR(CStructClusterGeometry), c_uint, PTR(c_uint), c_uint, c_uint])
build_simsub_cluster = get_func('build_simsub_cluster', PTR(CStructCluster), [PTR(CStructClusterGeometry), c_uint, PTR(c_uint), c_uint])
build_pca_cluster = get_func('build_pca_cluster', PTR(CStructCluster), [PTR(CStructClusterGeometry), c_uint, PTR(c_uint), c_uint])
build_cluster = get_func('build_cluster', PTR(CStructCluster), [PTR(CStructClusterGeometry), c_uint, PTR(c_uint), c_uint, CEnumClusterMode])
getdepth_cluster = get_func('getdepth_cluster', c_uint, [PTR(CStructCluster)])
getmindepth_cluster = get_func('getmindepth_cluster', c_uint, [PTR(CStructCluster)])
extend_cluster = get_func('extend_cluster', None, [PTR(CStructCluster), c_uint])
cut_cluster = get_func('cut_cluster', None, [PTR(CStructCluster), c_uint])
balance_cluster = get_func('balance_cluster', None, [PTR(CStructCluster), c_uint])
coarsen_cluster = get_func('coarsen_cluster', None, [PTR(CStructCluster), c_uint])
setsons_cluster = get_func('setsons_cluster', None, [PTR(CStructCluster), c_uint])
getdiam_2_cluster = get_func('getdiam_2_cluster', real, [PTR(CStructCluster)])
getdist_2_cluster = get_func('getdist_2_cluster', real, [PTR(CStructCluster), PTR(CStructCluster)])
getdiam_max_cluster = get_func('getdiam_max_cluster', real, [PTR(CStructCluster)])
getdist_max_cluster = get_func('getdist_max_cluster', real, [PTR(CStructCluster), PTR(CStructCluster)])
iterate_cluster = get_func('iterate_cluster', None, [PTR(CStructCluster), c_uint, CFuncClusterCallbackT, CFuncClusterCallbackT, c_void_p])
iterate_parallel_cluster = get_func('iterate_parallel_cluster', None, [PTR(CStructCluster), c_uint, c_uint, CFuncClusterCallbackT, CFuncClusterCallbackT, c_void_p])
enumerate_cluster = get_func('enumerate_cluster', PTR(PTR(CStructCluster)), [PTR(CStructCluster)])
# write_cdf_cluster = get_func('write_cdf_cluster', None, [PTR(CStructCluster), c_char_p])
# write_cdfpart_cluster = get_func('write_cdfpart_cluster', None, [PTR(CStructCluster), c_int, c_char_p])
# read_cdf_cluster = get_func('read_cdf_cluster', PTR(CStructCluster), [c_char_p])
# read_cdfpart_cluster = get_func('read_cdfpart_cluster', PTR(CStructCluster), [c_int, c_char_p])
