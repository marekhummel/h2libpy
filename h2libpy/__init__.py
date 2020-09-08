import ctypes
import os
from ctypes import POINTER as PTR
from ctypes import c_char, c_int

# Root folder of this module
root = os.path.join(os.path.dirname(__file__), '..')

# Init h2lib and load library instance
lib = ctypes.CDLL(os.path.join(root, 'h2libpy/libh2.so'))
init_h2lib = lib.init_h2lib
init_h2lib.restype = None
init_h2lib.argtypes = [PTR(c_int), PTR(PTR(PTR(c_char)))]
init_h2lib(c_int(0), None)
