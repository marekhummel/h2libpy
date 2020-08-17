from ctypes import CFUNCTYPE
from ctypes import POINTER as PTR
from ctypes import c_bool, c_uint, c_void_p

from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import (CStructBlock, CStructBlockEntry, CStructCluster)

# ------------------------


CFuncAdmissible = CFUNCTYPE(c_bool, *(PTR(CStructCluster), PTR(CStructCluster), c_void_p))
CFuncBlockCallbackT = CFUNCTYPE(None, *(PTR(CStructBlock), c_uint, c_uint, c_uint, c_uint, c_void_p))
CFuncBlockEntryCallbackT = CFUNCTYPE(None, *(PTR(CStructBlockEntry), c_uint, c_void_p))


# ------------------------


CStructBlock._fields_ = [
    ('rc', PTR(CStructCluster)),
    ('cc', PTR(CStructCluster)),
    ('a', c_bool),
    ('son', PTR(PTR(CStructBlock))),
    ('rsons', c_uint),
    ('csons', c_uint),
    ('desc', c_uint)
]


CStructBlockEntry._fields_ = [
    ('b', PTR(CStructBlock)),
    ('bname', c_uint),
    ('rname', c_uint),
    ('cname', c_uint),
    ('father', PTR(CStructBlockEntry)),
    ('next', PTR(CStructBlockEntry)),
]

# ------------------------


admissible_2_cluster = get_func('admissible_2_cluster', c_bool, [PTR(CStructCluster), PTR(CStructCluster), c_void_p])
admissible_max_cluster = get_func('admissible_max_cluster', c_bool, [PTR(CStructCluster), PTR(CStructCluster), c_void_p])
admissible_sphere_cluster = get_func('admissible_sphere_cluster', c_bool, [PTR(CStructCluster), PTR(CStructCluster), c_void_p])
admissible_2_min_cluster = get_func('admissible_2_min_cluster', c_bool, [PTR(CStructCluster), PTR(CStructCluster), c_void_p])
new_block = get_func('new_block', PTR(CStructBlock), [PTR(CStructCluster), PTR(CStructCluster), c_bool, c_uint, c_uint])
del_block = get_func('del_block', None, [PTR(CStructBlock)])
update_block = get_func('update_block', None, [PTR(CStructBlock)])
build_nonstrict_block = get_func('build_nonstrict_block', PTR(CStructBlock), [PTR(CStructCluster), PTR(CStructCluster), c_void_p, CFuncAdmissible])
build_nonstrict_lower_block = get_func('build_nonstrict_lower_block', PTR(CStructBlock), [PTR(CStructCluster), PTR(CStructCluster), c_void_p, CFuncAdmissible])
build_strict_block = get_func('build_strict_block', PTR(CStructBlock), [PTR(CStructCluster), PTR(CStructCluster), c_void_p, CFuncAdmissible])
build_strict_lower_block = get_func('build_strict_lower_block', PTR(CStructBlock), [PTR(CStructCluster), PTR(CStructCluster), c_void_p, CFuncAdmissible])
# draw_cairo_block
view_block = get_func('view_block', None, [PTR(CStructBlock)])
iterate_block = get_func('iterate_block', None, [PTR(CStructBlock), c_uint, c_uint, c_uint, CFuncBlockCallbackT, CFuncBlockCallbackT, c_void_p])
iterate_rowlist_block = get_func('iterate_rowlist_block', None, [PTR(CStructBlock), c_uint, c_uint, c_uint, c_uint, CFuncBlockEntryCallbackT, CFuncBlockEntryCallbackT, c_void_p])
iterate_collist_block = get_func('iterate_collist_block', None, [PTR(CStructBlock), c_uint, c_uint, c_uint, c_uint, CFuncBlockEntryCallbackT, CFuncBlockEntryCallbackT, c_void_p])
iterate_byrow_block = get_func('iterate_byrow_block', None, [PTR(CStructBlock), c_uint, c_uint, c_uint, c_uint, CFuncBlockCallbackT, CFuncBlockCallbackT, c_void_p])
iterate_bycol_block = get_func('iterate_bycol_block', None, [PTR(CStructBlock), c_uint, c_uint, c_uint, c_uint, CFuncBlockCallbackT, CFuncBlockCallbackT, c_void_p])
enumerate_block = get_func('enumerate_block', PTR(PTR(CStructBlock)), [PTR(CStructBlock)])
enumerate_level_block = get_func('enumerate_level_block', PTR(c_uint), [PTR(CStructBlock)])
getdepth_block = get_func('getdepth_block', c_uint, [PTR(CStructBlock)])
compute_csp_block = get_func('compute_csp_block', c_uint, [PTR(CStructBlock)])
