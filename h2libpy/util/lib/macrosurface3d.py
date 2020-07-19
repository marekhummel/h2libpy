from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint, c_void_p

# from h2libpy.util.helper import get_func
from h2libpy.util.lib.settings import real


# ------------------------


class LibMacroSurface3d(Struct): pass


# ------------------------


LibMacroSurface3d._fields_ = [
    ('vertices', c_uint),
    ('edges', c_uint),
    ('triangles', c_uint),
    ('x', PTR(real) * 3),
    ('e', PTR(c_uint) * 2),
    ('t', PTR(c_uint) * 2),
    ('s', PTR(c_uint) * 2),
    ('phidata', c_void_p),
]


# ------------------------
