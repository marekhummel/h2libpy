from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.lib.util.helper import get_func
from h2libpy.lib.amatrix import LibAMatrix
from h2libpy.lib.dclusterbasis import LibDClusterBasis

# ------------------------


class LibDUniform(Struct): pass


# ------------------------


LibDUniform._fields_ = [
    ('rb', PTR(LibDClusterBasis)),
    ('cb', PTR(LibDClusterBasis)),
    ('rd', c_uint),
    ('cd', c_uint),
    ('S', LibAMatrix),
    ]


# ------------------------
