from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.lib.util.helper import get_func


# ------------------------


class LibClusterBasis(Struct): pass


# ------------------------

from h2libpy.lib.amatrix import LibAMatrix
from h2libpy.lib.cluster import LibCluster
from h2libpy.lib.uniform import LibUniform


LibClusterBasis._fields_ = [
    ('t', PTR(LibCluster)),
    ('k', c_uint),
    ('ktree', c_uint),
    ('kbranch', c_uint),
    ('V', LibAMatrix),
    ('E', LibAMatrix),
    ('sons', c_uint),
    ('son', PTR(PTR(LibClusterBasis))),
    ('Z', PTR(LibAMatrix)),
    ('refs', c_uint),
    ('rlist', PTR(LibUniform)),
    ('clist', PTR(LibUniform))
]


# ------------------------
