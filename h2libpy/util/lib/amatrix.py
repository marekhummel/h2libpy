from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint, c_void_p

# from h2libpy.util.helper import get_func
from h2libpy.util.lib.settings import field

# ------------------------


class LibAMatrix(Struct): pass


# ------------------------


LibAMatrix._fields_ = [
    ('a', PTR(field)),
    ('ld', c_uint),
    ('rows', c_uint),
    ('cols', c_uint),
    ('owner', c_void_p)
]

# ------------------------
