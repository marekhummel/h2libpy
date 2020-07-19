from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.util.helper import get_func
from h2libpy.util.lib.settings import real

# ------------------------


class LibCluster(Struct): pass


# ------------------------


LibCluster._fields_ = [
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
