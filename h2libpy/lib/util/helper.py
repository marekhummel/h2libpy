from ctypes import c_char, c_int, c_double, c_bool, pointer
from h2libpy import lib


def get_func(name: str, returntype, argtypes):
    f = lib.__getattr__(name)
    f.restype = returntype
    f.argtypes = argtypes
    return f


def uninit():
    uninit_h2lib = get_func('uninit_h2lib', None, [])
    uninit_h2lib()


def get_address(obj, ctype=None):
    if ctype is None:
        if isinstance(obj, float):
            return pointer(c_double(obj))
        elif isinstance(obj, int):
            return pointer(c_int(obj))
        elif isinstance(obj, bool):
            return pointer(c_bool(obj))
    else:
        return pointer(ctype(obj))
