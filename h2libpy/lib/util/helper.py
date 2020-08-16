from h2libpy import lib


def get_func(name: str, returntype, argtypes):
    f = lib.__getattr__(name)
    f.restype = returntype
    f.argtypes = argtypes
    return f


def uninit():
    uninit_h2lib = get_func('uninit_h2lib', None, [])
    uninit_h2lib()
