from h2libpy.util.lib.structs import LibAVector
import h2libpy.util.lib.func as lib
from ctypes import c_double, c_uint, c_void_p, POINTER


class AVector(LibAVector):
    # ***** Constructors / destructor *****

    def __new__(cls, *args, **kwargs):
        dim = args[0] if len(args) > 0 else 0
        instance = lib.new_avector(dim).contents
        instance.__class__ = AVector
        return instance

    def __init__(self, dim):
        pass
        # lib.resize_avector(self, dim)

    # ***** Properties *****

    # def dim(self):
    #     return self._as_parameter_.contents.dim

    # def values(self):
    #     return self._as_parameter_.contents.v[:self.dim()]

    # ***** Methods ******

    # def fill(self, value):
    #     lib.fill_avector(self, c_double(value))

    def rand(self):
        lib.random_avector(self)

    def norm(self):
        return lib.norm2_avector(self)
