from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.lib.util.helper import get_func
from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.dclusterbasis import CStructDClusterBasis
from h2libpy.lib.duniform import CStructDUniform

# ------------------------


class CStructDH2Matrix(Struct): pass


# ------------------------


CStructDH2Matrix._fields_ = [
    ('rb', PTR(CStructDClusterBasis)),
    ('cb', PTR(CStructDClusterBasis)),
    ('u', PTR(CStructDUniform)),
    ('f', PTR(CStructAMatrix)),
    ('son', PTR(PTR(CStructDH2Matrix))),
    ('rsons', c_uint),
    ('csons', c_uint),
    ('desc', c_uint),
]


# ------------------------
