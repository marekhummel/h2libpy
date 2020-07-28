from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.lib.util.helper import get_func
from h2libpy.lib.settings import field

# ------------------------


class CStructSparseMatrix(Struct): pass


# ------------------------


CStructSparseMatrix._fields_ = [
    ('rows', c_uint),
    ('cols', c_uint),
    ('nz', c_uint),
    ('row', PTR(c_uint)),
    ('col', PTR(c_uint)),
    ('coeff', PTR(field))
]


# ------------------------
