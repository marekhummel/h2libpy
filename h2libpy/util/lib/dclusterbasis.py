from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.util.helper import get_func
from h2libpy.util.lib.amatrix import LibAMatrix
from h2libpy.util.lib.dcluster import LibDCluster


# ------------------------


class LibDClusterBasis(Struct): pass


# ------------------------


LibDClusterBasis._fields_ = [
    ('t', PTR(LibDCluster)),
    ('directions', c_uint),
    ('k', PTR(c_uint)),
    ('koff', PTR(c_uint)),
    ('ktree', c_uint),
    ('kbranch', c_uint),
    ('V', PTR(LibAMatrix)),
    ('E', PTR(PTR(LibAMatrix))),
    ('sons', c_uint),
    ('son', PTR(PTR(LibDClusterBasis))),
    ('dirson', PTR(PTR(c_uint))),
]


# ------------------------
