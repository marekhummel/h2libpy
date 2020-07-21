from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.lib.util.helper import get_func
from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.dcluster import CStructDCluster


# ------------------------


class CStructDClusterBasis(Struct): pass


# ------------------------


CStructDClusterBasis._fields_ = [
    ('t', PTR(CStructDCluster)),
    ('directions', c_uint),
    ('k', PTR(c_uint)),
    ('koff', PTR(c_uint)),
    ('ktree', c_uint),
    ('kbranch', c_uint),
    ('V', PTR(CStructAMatrix)),
    ('E', PTR(PTR(CStructAMatrix))),
    ('sons', c_uint),
    ('son', PTR(PTR(CStructDClusterBasis))),
    ('dirson', PTR(PTR(c_uint))),
]


# ------------------------
