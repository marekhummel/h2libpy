from ctypes import CFUNCTYPE
from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_bool, c_size_t, c_uint, c_void_p

from h2libpy.lib.settings import real
from h2libpy.lib.util.helper import get_func

# ------------------------


class CStructDBlock(Struct): pass


# ------------------------

from h2libpy.lib.dcluster import CStructDCluster, CStructLevelDir


CFuncAdmissible = CFUNCTYPE(c_bool, *[PTR(CStructDCluster), PTR(CStructDCluster), c_uint, PTR(c_uint), PTR(c_uint), c_void_p])


# ------------------------


CStructDBlock._fields_ = [
    ('rc', PTR(CStructDCluster)),
    ('cc', PTR(CStructDCluster)),
    ('rd', c_uint),
    ('cd', c_uint),
    ('adm', c_bool),
    ('rsons', c_uint),
    ('csons', c_uint),
    ('son', PTR(PTR(CStructDBlock))),
    ('desc', c_uint),
]


# ------------------------


new_dblock = get_func('new_dblock', PTR(CStructDBlock), [PTR(CStructDCluster), PTR(CStructDCluster), c_uint, c_uint, c_uint, c_uint])
update_dblock = get_func('update_dblock', None, [PTR(CStructDBlock)])
del_dblock = get_func('del_dblock', None, [PTR(CStructDBlock)])
getactives_dblock = get_func('getactives_dblock', c_uint, [])
getsize_dblock = get_func('getsize_dblock', c_size_t, [PTR(CStructDBlock)])
getdepth_dblock = get_func('getdepth_dblock', c_uint, [PTR(CStructDBlock)])
# cairodraw_dblock
build_dblock = get_func('build_dblock', PTR(CStructDBlock), [PTR(CStructDCluster), PTR(CStructDCluster), CFuncAdmissible, c_void_p])
parabolic_admissibility = get_func('parabolic_admissibility', c_bool, [PTR(CStructDCluster), PTR(CStructDCluster), c_uint, PTR(c_uint), PTR(c_uint), c_void_p])
standard_admissibility = get_func('standard_admissibility', c_bool, [PTR(CStructDCluster), PTR(CStructDCluster), c_uint, PTR(c_uint), PTR(c_uint), c_void_p])
getmaxeta_dblock = get_func('getmaxeta_dblock', real, [PTR(CStructDBlock)])
remove_unused_direction = get_func('remove_unused_direction', PTR(CStructLevelDir), [PTR(CStructDBlock), PTR(CStructDCluster), PTR(CStructLevelDir)])
enumerate_dblock = get_func('enumerate_dblock', PTR(PTR(CStructDBlock)), [PTR(CStructDBlock)])
