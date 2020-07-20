from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.util.helper import get_func
from h2libpy.util.lib.amatrix import LibAMatrix
from h2libpy.util.lib.dcluster import LibDCluster


# ------------------------


class LibDClusterOperator(Struct): pass


# ------------------------


LibDClusterOperator._fields_ = [
    ('t', PTR(LibDCluster)),
    ('krow', PTR(c_uint)),
    ('kcol', PTR(c_uint)),
    ('dir', c_uint),
    ('C', PTR(LibAMatrix)),
    ('sons', c_uint),
    ('son', PTR(PTR(LibDClusterOperator))),
    ('refs', c_uint),
]


# ------------------------
