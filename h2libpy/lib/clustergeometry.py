from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

from h2libpy.lib.settings import real
from h2libpy.lib.util.helper import get_func

# ------------------------


class CStructClusterGeometry(Struct): pass


# ------------------------


from h2libpy.lib.cluster import CStructCluster


CStructClusterGeometry._fields_ = [
    ('dim', c_uint),
    ('nidx', c_uint),
    ('x', PTR(PTR(real))),
    ('smin', PTR(PTR(real))),
    ('smax', PTR(PTR(real))),
    ('w', PTR(real)),
    ('hmin', PTR(real)),
    ('hmax', PTR(real)),
    ('buf', PTR(real)),
]


# ------------------------


new_clustergeometry = get_func('new_clustergeometry', PTR(CStructClusterGeometry), [c_uint, c_uint])
del_clustergeometry = get_func('del_clustergeometry', None, [PTR(CStructClusterGeometry)])
update_point_bbox_clustergeometry = get_func('update_point_bbox_clustergeometry', None, [PTR(CStructClusterGeometry), c_uint, PTR(c_uint)])
update_support_bbox_cluster = get_func('update_support_bbox_cluster', None, [PTR(CStructClusterGeometry), PTR(CStructCluster)])
update_bbox_cluster = get_func('update_bbox_cluster', None, [PTR(CStructCluster)])
