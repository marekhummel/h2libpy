from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.lib.util.helper import get_func


# ------------------------


class CStructClusterBasis(Struct): pass


# ------------------------

from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.cluster import CStructCluster
from h2libpy.lib.uniform import CStructUniform


CStructClusterBasis._fields_ = [
    ('t', PTR(CStructCluster)),
    ('k', c_uint),
    ('ktree', c_uint),
    ('kbranch', c_uint),
    ('V', CStructAMatrix),
    ('E', CStructAMatrix),
    ('sons', c_uint),
    ('son', PTR(PTR(CStructClusterBasis))),
    ('Z', PTR(CStructAMatrix)),
    ('refs', c_uint),
    ('rlist', PTR(CStructUniform)),
    ('clist', PTR(CStructUniform))
]


# ------------------------
