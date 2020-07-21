from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.lib.util.helper import get_func
from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.dclusterbasis import CStructDClusterBasis

# ------------------------


class CStructDUniform(Struct): pass


# ------------------------


CStructDUniform._fields_ = [
    ('rb', PTR(CStructDClusterBasis)),
    ('cb', PTR(CStructDClusterBasis)),
    ('rd', c_uint),
    ('cd', c_uint),
    ('S', CStructAMatrix),
    ]


# ------------------------
