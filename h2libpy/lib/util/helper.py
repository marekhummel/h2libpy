import ctypes
from ctypes import c_int, c_char, POINTER as PTR


def get_func(name: str, returntype, argtypes):
    f = lib.__getattr__(name)
    f.restype = returntype
    f.argtypes = argtypes
    return f


def init():
    global lib
    # lib = ctypes.CDLL('./lib/libh2.so')
    lib = ctypes.CDLL('../H2Lib/libh2.so')
    init_h2lib = get_func('init_h2lib', None,
                          [PTR(c_int), PTR(PTR(PTR(c_char)))])
    init_h2lib(c_int(0), None)


def uninit():
    uninit_h2lib = get_func('uninit_h2lib', None, [])
    uninit_h2lib()


init()
