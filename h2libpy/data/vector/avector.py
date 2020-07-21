import h2libpy.lib.avector as lib
from ctypes import c_double, POINTER
from h2libpy.base.structwrapper import StructWrapper


class AVector(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert(isinstance(cobj, POINTER(lib.LibAVector)))
        self._as_parameter_ = cobj

    def __del__(self):
        lib.del_avector(self)

    @classmethod
    def new(cls, dim: int):
        return cls(lib.new_avector(dim))

    @classmethod
    def from_subvector(cls, src: 'lib.LibAVector', dim: int, off: int):
        v = lib.new_avector(dim)
        lib.init_sub_avector(v, src, dim, off)
        return cls(v)

    # ***** Properties *****

    def _getter_dim(self):
        return self._as_parameter_.contents.dim

    def _getter_v(self):
        return self._as_parameter_.contents.v[:self.dim]

    # ***** Methods ******

    def fill(self, value):
        lib.fill_avector(self, c_double(value))

    def rand(self):
        lib.random_avector(self)

    def norm(self):
        return lib.norm2_avector(self)
