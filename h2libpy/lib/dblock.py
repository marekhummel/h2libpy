from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_bool, c_uint

# from h2libpy.lib.util.helper import get_func
from h2libpy.lib.dcluster import CStructDCluster

# ------------------------


class CStructDBlock(Struct): pass


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
