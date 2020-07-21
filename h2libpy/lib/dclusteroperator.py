from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.lib.util.helper import get_func
from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.dcluster import CStructDCluster


# ------------------------


class CStructDClusterOperator(Struct): pass


# ------------------------


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
