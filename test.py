from ctypes import POINTER as PTR
from ctypes import Structure, c_double, c_uint, c_void_p, pointer

from h2libpy.base.util import cptr_to_list
from h2libpy.lib.util.helper import get_func


class CStructAVector(Structure):
    _fields_ = [
        ('v', PTR(c_double)),
        ('dim', c_uint),
        ('owner', c_void_p)
    ]


class StructWrapper:
    def __getattribute__(self, name):
        val = super().__getattribute__(name)
        if (name == 'v'):
            return cptr_to_list(val, self.dim)
        return val


class AVector(CStructAVector, StructWrapper):
    @classmethod
    def new(cls, dim: int) -> 'AVector':
        new_avector = get_func('new_avector', PTR(AVector), [c_uint])
        return new_avector(dim).contents

    def print(self) -> None:
        print_avector = get_func('print_avector', None, [PTR(AVector)])
        print_avector(pointer(self))

    def rand(self) -> None:
        random_avector = get_func('random_avector', None, [PTR(AVector)])
        random_avector(pointer(self))

    def norm(self) -> float:
        norm2_avector = get_func('norm2_avector', c_double, [PTR(AVector)])
        return norm2_avector(pointer(self))


x = AVector.new(3)
x.rand()
print(x.norm())
x.print()
print(x.dim)
print(x.v)
