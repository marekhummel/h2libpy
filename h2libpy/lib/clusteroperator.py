from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.lib.util.helper import get_func
from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.cluster import CStructCluster

# ------------------------


class CStructClusterOperator(Struct): pass


# ------------------------


CStructClusterOperator._fields_ = [
    ('t', PTR(CStructCluster)),
    ('krow', c_uint),
    ('kcol', c_uint),
    ('C', CStructAMatrix),
    ('sons', c_uint),
    ('son', PTR(PTR(CStructClusterOperator))),
    ('refs', c_uint),
]


# ------------------------
