import ctypes


def get_func(name: str, returntype, argtypes):
    f = lib.__getattr__(name)
    f.restype = returntype
    f.argtypes = argtypes
    return f


def init():
    global lib
    lib = ctypes.CDLL('lib/libh2.so')


lib = None
init()
