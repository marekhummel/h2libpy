
from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint

# from h2libpy.util.helper import get_func
from h2libpy.util.lib.settings import real

# ------------------------


class LibDCluster(Struct): pass


# ------------------------


LibDCluster._fields_ = [
    ('size', c_uint),
    ('idx', PTR(c_uint)),
    ('sons', c_uint),
    ('son', PTR(PTR(LibDCluster))),
    ('dim', c_uint),
    ('bmin', PTR(real)),
    ('bmax', PTR(real)),
    ('directions', c_uint),
    ('dir', PTR(PTR(real))),
    ('dirson', PTR(PTR(c_uint))),
    ('desc', c_uint),
]


# ------------------------
