import ctypes


def func(name: str, returntype, argtypes):
    func = lib.__getattr__(name)
    func.restype = returntype
    func.argtypes = argtypes
    return func


def init():
    global lib
    lib = ctypes.CDLL('lib/libh2.so')


lib = None
init()
