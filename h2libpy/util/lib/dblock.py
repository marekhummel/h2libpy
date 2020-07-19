from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_bool, c_uint

# from h2libpy.util.helper import get_func
from h2libpy.util.lib.dcluster import LibDCluster

# ------------------------


class LibDBlock(Struct): pass


# ------------------------


LibDBlock._fields_ = [
    ('rc', PTR(LibDCluster)),
    ('cc', PTR(LibDCluster)),
    ('rd', c_uint),
    ('cd', c_uint),
    ('adm', c_bool),
    ('rsons', c_uint),
    ('csons', c_uint),
    ('son', PTR(PTR(LibDBlock))),
    ('desc', c_uint),
]


# ------------------------
