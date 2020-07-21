from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.lib.util.helper import get_func
from h2libpy.lib.amatrix import CStructAMatrix

# ------------------------


class CStructRKMatrix(Struct): pass


# ------------------------


CStructRKMatrix._fields_ = [
    ('A', CStructAMatrix),
    ('B', CStructAMatrix),
    ('k', c_uint),
]


# ------------------------
