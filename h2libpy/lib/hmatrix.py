from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.util.helper import get_func
from h2libpy.lib.amatrix import LibAMatrix
from h2libpy.lib.cluster import LibCluster
from h2libpy.lib.rkmatrix import LibRKMatrix

# ------------------------


class LibHMatrix(Struct): pass


# ------------------------


LibHMatrix._fields_ = [
    ('rc', PTR(LibCluster)),
    ('cc', PTR(LibCluster)),
    ('r', PTR(LibRKMatrix)),
    ('f', PTR(LibAMatrix)),
    ('son', PTR(PTR(LibHMatrix))),
    ('rsons', c_uint),
    ('csons', c_uint),
    ('refs', c_uint),
    ('desc', c_uint),
]


# ------------------------
