from typing import List, Tuple

import h2libpy.lib.realavector as librealavector
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import cptr_to_list, pylist_to_ptr, verify_type
from h2libpy.lib.settings import field


class RealAVector(StructWrapper, cstruct=librealavector.CStructRealAVector):
    @classmethod
    def new(cls, dim: int) -> 'RealAVector':
        return cls(librealavector.new_realavector(dim))

    @classmethod
    def from_subvector(cls, src: 'RealAVector', dim: int,
                       off: int = 0) -> 'RealAVector':
        return cls(librealavector.new_sub_realavector(src, dim, off))

    @classmethod
    def from_list(cls, elems: List[float], *, dim: int = -1):
        cdim = dim if dim != -1 else len(elems)
        celems = pylist_to_ptr(elems, field)
        obj = librealavector.new_pointer_realavector(celems, cdim)
        return cls(obj, refs=[celems])

    # ***** Properties *****

    def __getter_dim(self) -> int:
        return self.cobj().dim

    def __getter_v(self) -> Tuple[float, ...]:
        return tuple(cptr_to_list(self.cobj().v, self.dim))

    # ***** Methods ******

    def resize(self, dim: int):
        librealavector.resize_realavector(self, dim)

    def shrink(self, dim: int):
        librealavector.shrink_realavector(self, dim)

    def size(self, heaponly: bool = False) -> int:
        if heaponly:
            return librealavector.getsize_heap_realavector(self)
        else:
            return librealavector.getsize_realavector(self)

    def clear(self):
        librealavector.clear_realavector(self)

    def fill(self, value: float):
        librealavector.fill_realavector(self, value)

    def rand(self):
        librealavector.random_realavector(self)

    def copy(self, target: 'RealAVector'):
        if self.dim == target.dim:
            librealavector.copy_realavector(self, target)
        else:
            librealavector.copy_sub_realavector(self, target)

    def print(self):
        librealavector.print_realavector(self)

    def scale(self, alpha: float):
        librealavector.scale_realavector(alpha, self)

    def norm(self) -> float:
        return librealavector.norm2_realavector(self)

    def dot(self, other: 'RealAVector') -> float:
        return librealavector.dotprod_realavector(self, other)

    def add(self, other: 'RealAVector', alpha: float = 1.0):
        librealavector.add_realavector(alpha, other, self)

    # ***** Operators ******

    def __add__(self, rhs):
        verify_type(rhs, [RealAVector])
        v = RealAVector.new(self.dim)
        v.clear()
        v.add(self)
        v.add(rhs)
        return v

    def __sub__(self, rhs):
        verify_type(rhs, [RealAVector])
        v = RealAVector.new(self.dim)
        v.clear()
        v.add(self)
        v.add(rhs, -1)
        return v

    def __mul__(self, rhs):
        verify_type(rhs, [RealAVector, int, float])
        if isinstance(rhs, RealAVector):
            return self.dot(rhs)
        elif isinstance(rhs, (int, float)):
            v = RealAVector.new(self.dim)
            v.clear()
            v.add(self, rhs)
            return v

    def __rmul__(self, lhs):
        return self * lhs

    def __neg__(self):
        v = RealAVector.new(self.dim)
        v.clear()
        v.add(self, -1)
        return v

    def __getitem__(self, index):
        if index not in range(self.dim):
            raise ValueError('Index out of range.')
        return self.v[index]

    def __eq__(self, other):
        if self.dim != other.dim:
            return False
        return self.v == other.v

    def __len__(self):
        return self.dim

    def __iadd__(self, rhs):
        verify_type(rhs, [RealAVector])
        self.add(rhs)
        return self

    def __isub__(self, rhs):
        verify_type(rhs, [RealAVector])
        self.add(rhs, -1)
        return self

    def __imul__(self, rhs):
        verify_type(rhs, [int, float])
        self.scale(rhs)
        return self

    def __str__(self):
        return str(self.v)
