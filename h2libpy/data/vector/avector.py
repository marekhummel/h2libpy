from ctypes import c_uint, c_void_p, c_double, Structure, POINTER
import ctypes
import h2libpy.util.lib_helper as lh

lib = ctypes.CDLL('./lib/libh2.so')


class AVector(Structure):
    _fields_ = [
        ('v', POINTER(c_double)),
        ('dim', c_uint),
        ('owner', c_void_p)
    ]

    def __init__(self, dim):
        new_avector = lh.func('new_avector', POINTER(AVector), [c_uint])
        self.obj = new_avector(c_uint(dim))

    def fill(self, value):
        fill_avector = lh.func('fill_avector', None,
                               [POINTER(AVector), c_double])
        fill_avector(self.obj, c_double(value))

    def rand(self):
        random_avector = lh.func('random_avector', None, [POINTER(AVector)])
        random_avector(self.obj)

    def get_dim(self):
        return self.obj.contents.dim

    def norm(self):
        norm2_avector = lh.func('norm2_avector', c_double, [POINTER(AVector)])
        return norm2_avector(self.obj)
