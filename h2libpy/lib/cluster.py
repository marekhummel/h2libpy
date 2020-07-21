from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.lib.util.helper import get_func
from h2libpy.lib.settings import real

# ------------------------


class CStructCluster(Struct): pass


# ------------------------


CStructCluster._fields_ = [
    ('size', c_uint),
    ('idx', PTR(c_uint)),
    ('sons', c_uint),
    ('dim', c_uint),
    ('bmin', PTR(real)),
    ('bmax', PTR(real)),
    ('desc', c_uint),
    ('type', c_uint),
]


# ------------------------
