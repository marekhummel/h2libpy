from ctypes import c_uint, c_void_p, c_double, Structure, POINTER
import ctypes

lib = ctypes.CDLL('./lib/libh2.so')


class AVector(Structure):
    _fields_ = [
        ('v', POINTER(c_double)),
        ('dim', c_uint),
        ('owner', c_void_p)
    ]

    def __init__(self, dim):
        new_avector = lib.new_avector
        new_avector.restype = POINTER(AVector)
        new_avector.argtypes = [c_uint]
        self.obj = new_avector(c_uint(dim))

    def fill(self, value):
        fill_avector = lib.fill_avector
        fill_avector.restype = None
        fill_avector.argtypes = [POINTER(AVector), c_double]
        fill_avector(self.obj, c_double(value))

    def rand(self):
        random_avector = lib.random_avector
        random_avector.restype = None
        random_avector.argtypes = [POINTER(AVector)]
        random_avector(self.obj)

    def get_dim(self):
        return self.obj.contents.dim

    def print(self):
        print_avector = lib.print_avector
        print_avector.restype = None
        print_avector.argtypes = [POINTER(AVector)]
        print_avector(self.obj)

    def norm(self):
        norm2_avector = lib.norm2_avector
        norm2_avector.restype = c_double
        norm2_avector.argtypes = [POINTER(AVector)]
        return norm2_avector(self.obj)
