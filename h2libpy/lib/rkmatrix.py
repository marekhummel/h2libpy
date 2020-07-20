from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.util.helper import get_func
from h2libpy.lib.amatrix import LibAMatrix

# ------------------------


class LibRKMatrix(Struct): pass


# ------------------------


LibRKMatrix._fields_ = [
    ('A', LibAMatrix),
    ('B', LibAMatrix),
    ('k', c_uint),
]


# ------------------------
