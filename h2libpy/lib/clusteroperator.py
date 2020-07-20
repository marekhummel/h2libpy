from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.util.helper import get_func
from h2libpy.lib.amatrix import LibAMatrix
from h2libpy.lib.cluster import LibCluster

# ------------------------


class LibClusterOperator(Struct): pass


# ------------------------


LibClusterOperator._fields_ = [
    ('t', PTR(LibCluster)),
    ('krow', c_uint),
    ('kcol', c_uint),
    ('C', LibAMatrix),
    ('sons', c_uint),
    ('son', PTR(PTR(LibClusterOperator))),
    ('refs', c_uint),
]


# ------------------------
