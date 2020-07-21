from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# nfrom h2libpy.lib.util.helper import get_func
from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.clusterbasis import CStructClusterBasis
from h2libpy.lib.uniform import CStructUniform

# ------------------------


class CStructH2Matrix(Struct): pass


# ------------------------


CStructH2Matrix._fields_ = [
    ('rb', PTR(CStructClusterBasis)),
    ('cb', PTR(CStructClusterBasis)),
    ('u', PTR(CStructUniform)),
    ('f', PTR(CStructAMatrix)),
    ('son', PTR(PTR(CStructH2Matrix))),
    ('rsons', c_uint),
    ('csons', c_uint),
    ('refs', c_uint),
    ('desc', c_uint),
]


# ------------------------
