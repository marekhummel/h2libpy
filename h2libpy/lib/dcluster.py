
from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_size_t, c_uint

from h2libpy.lib.settings import real
from h2libpy.lib.util.helper import get_func

# ------------------------


class CStructDCluster(Struct): pass
class CStructLevelDir(Struct): pass


# ------------------------


from h2libpy.lib.cluster import CStructCluster


CStructDCluster._fields_ = [
    ('size', c_uint),
    ('idx', PTR(c_uint)),
    ('sons', c_uint),
    ('son', PTR(PTR(CStructDCluster))),
    ('dim', c_uint),
    ('bmin', PTR(real)),
    ('bmax', PTR(real)),
    ('directions', c_uint),
    ('dir', PTR(PTR(real))),
    ('dirson', PTR(PTR(c_uint))),
    ('desc', c_uint),
]


CStructLevelDir._fields_ = [
    ('depth', c_uint),
    ('dim', c_uint),
    ('maxdiam', PTR(real)),
    ('splits', PTR(c_uint)),
    ('directions', PTR(c_uint)),
    ('dir', PTR(PTR(PTR(real)))),
    ('dirmem', PTR(real))
]

# ------------------------


new_dcluster = get_func('new_dcluster', PTR(CStructDCluster), [c_uint, PTR(c_uint), c_uint, c_uint])
update_dcluster = get_func('update_dcluster', None, [PTR(CStructDCluster)])
del_dcluster = get_func('del_dcluster', None, [PTR(CStructDCluster)])
new_leveldir = get_func('new_leveldir', PTR(CStructLevelDir), [c_uint, c_uint])
del_leveldir = get_func('del_leveldir', None, [PTR(CStructLevelDir)])
buildfromcluster_dcluster = get_func('buildfromcluster_dcluster', PTR(CStructDCluster), [PTR(CStructCluster)])
diam_dcluster = get_func('diam_dcluster', real, [PTR(CStructDCluster)])
dist_dcluster = get_func('dist_dcluster', real, [PTR(CStructDCluster), PTR(CStructDCluster)])
middist_dcluster = get_func('middist_dcluster', real, [PTR(CStructDCluster), PTR(CStructDCluster)])
finddirection_dcluster = get_func('finddirection_dcluster', c_uint, [PTR(CStructDCluster), real, PTR(real)])
getactives_dcluster = get_func('getactives_dcluster', c_uint, [])
getsize_dcluster = get_func('getsize_dcluster', c_size_t, [PTR(CStructDCluster)])
getdepth_dcluster = get_func('getdepth_dcluster', c_uint, [PTR(CStructDCluster)])
getalldirections_dcluster = get_func('getalldirections_dcluster', c_uint, [PTR(CStructDCluster)])
builddirections_box_dcluster = get_func('builddirections_box_dcluster', PTR(CStructLevelDir), [PTR(CStructDCluster), real])
finddirection_leveldir = get_func('finddirection_leveldir', c_uint, [PTR(CStructLevelDir), c_uint, real, PTR(real)])
