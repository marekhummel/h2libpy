from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint, c_void_p

from h2libpy.lib.settings import real
# from h2libpy.lib.util.helper import get_func

# ------------------------


class CStructRealAVector(Struct): pass


# ------------------------


CStructRealAVector._fields_ = [
    ('v', PTR(real)),
    ('dim', c_uint),
    ('owner', c_void_p)
]
