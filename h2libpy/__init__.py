import ctypes
from ctypes import POINTER as PTR
from ctypes import c_char, c_int

# Init h2lib and load library instance
lib = ctypes.CDLL('../H2Lib/libh2.so')  # './lib/libh2.so'
init_h2lib = lib.init_h2lib
init_h2lib.restype = None
init_h2lib.argtypes = [PTR(c_int), PTR(PTR(PTR(c_char)))]
init_h2lib(c_int(0), None)
