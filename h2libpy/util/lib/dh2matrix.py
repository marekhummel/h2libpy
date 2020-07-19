from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.util.helper import get_func
from h2libpy.util.lib.amatrix import LibAMatrix
from h2libpy.util.lib.dclusterbasis import LibDClusterBasis
from h2libpy.util.lib.duniform import LibDUniform

# ------------------------


class LibDH2Matrix(Struct): pass


# ------------------------


LibDH2Matrix._fields_ = [
    ('rb', PTR(LibDClusterBasis)),
    ('cb', PTR(LibDClusterBasis)),
    ('u', PTR(LibDUniform)),
    ('f', PTR(LibAMatrix)),
    ('son', PTR(PTR(LibDH2Matrix))),
    ('rsons', c_uint),
    ('csons', c_uint),
    ('desc', c_uint),
]


# ------------------------
