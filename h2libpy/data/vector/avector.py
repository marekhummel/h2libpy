from h2libpy.util.lib.structs import LibAVector
import h2libpy.util.lib.func as lib
from ctypes import c_double, c_uint, c_void_p, POINTER


class AVector():
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert(isinstance(cobj, POINTER(LibAVector)))
        self._as_parameter_ = cobj

    def __del__(self):
        lib.del_avector(self)

    @classmethod
    def new(cls, dim: int):
        return cls(lib.new_avector(dim))

    @classmethod
    def from_subvector(cls, src: 'LibAVector', dim: int, off: int):
        v = lib.new_avector(dim)
        lib.init_sub_avector(v, src, dim, off)
        return cls(v)

    # ***** Properties *****

    def dim(self):
        return self._as_parameter_.contents.dim

    def values(self):
        return self._as_parameter_.contents.v[:self.dim()]

    # ***** Methods ******

    def fill(self, value):
        lib.fill_avector(self, c_double(value))

    def rand(self):
        lib.random_avector(self)

    def norm(self):
        return lib.norm2_avector(self)
