from ctypes import CFUNCTYPE
from ctypes import c_void_p

from h2libpy.lib.avector import CStructAVector
from h2libpy.lib.settings import field

# ------------------------------------


CFuncAddevalT = CFUNCTYPE(None, *[field, c_void_p, CStructAVector, CStructAVector])
CFuncPrcdT = CFUNCTYPE(None, *[c_void_p, CStructAVector])
