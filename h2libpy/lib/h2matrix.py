from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# nfrom h2libpy.lib.util.helper import get_func
from h2libpy.lib.amatrix import LibAMatrix
from h2libpy.lib.clusterbasis import LibClusterBasis
from h2libpy.lib.uniform import LibUniform

# ------------------------


class LibH2Matrix(Struct): pass


# ------------------------


LibH2Matrix._fields_ = [
    ('rb', PTR(LibClusterBasis)),
    ('cb', PTR(LibClusterBasis)),
    ('u', PTR(LibUniform)),
    ('f', PTR(LibAMatrix)),
    ('son', PTR(PTR(LibH2Matrix))),
    ('rsons', c_uint),
    ('csons', c_uint),
    ('refs', c_uint),
    ('desc', c_uint),
]


# ------------------------
