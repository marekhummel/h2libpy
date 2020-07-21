from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.lib.util.helper import get_func
from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.cluster import CStructCluster
from h2libpy.lib.rkmatrix import CStructRKMatrix

# ------------------------


class CStructHMatrix(Struct): pass


# ------------------------


CStructHMatrix._fields_ = [
    ('rc', PTR(CStructCluster)),
    ('cc', PTR(CStructCluster)),
    ('r', PTR(CStructRKMatrix)),
    ('f', PTR(CStructAMatrix)),
    ('son', PTR(PTR(CStructHMatrix))),
    ('rsons', c_uint),
    ('csons', c_uint),
    ('refs', c_uint),
    ('desc', c_uint),
]


# ------------------------
