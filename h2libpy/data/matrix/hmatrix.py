from ctypes import pointer
from typing import List

import h2libpy.lib.hmatrix as libhmatrix
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import cptr_to_list, try_wrap
from h2libpy.data.matrix.amatrix import AMatrix
from h2libpy.data.matrix.enums import ClearType, SizePart
from h2libpy.data.misc.cluster import Cluster


class HMatrix(StructWrapper, cstruct=libhmatrix.CStructHMatrix):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, rc: 'Cluster', cc: 'Cluster') -> 'HMatrix':
        return cls(libhmatrix.new_hmatrix(rc, cc))

    @classmethod
    def new_rk(cls, rc: 'Cluster', cc: 'Cluster', k: int) -> 'HMatrix':
        return cls(libhmatrix.new_rk_hmatrix(rc, cc, k))

    @classmethod
    def new_full(cls, rc: 'Cluster', cc: 'Cluster') -> 'HMatrix':
        return cls(libhmatrix.new_full_hmatrix(rc, cc))

    @classmethod
    def new_super(cls, rc: 'Cluster', cc: 'Cluster',
                  rsons: int, csons: int) -> 'HMatrix':
        return cls(libhmatrix.new_super_hmatrix(rc, cc, rsons, csons))

    @classmethod
    def from_block(cls, b: 'Block', k: int) -> 'HMatrix':
        return cls(libhmatrix.build_from_block_hmatrix(b, k))

    @classmethod
    def from_file(cls, file: str, is_symmetric: bool):
        if is_symmetric:
            return cls(libhmatrix.read_hlibsymm_hmatrix(file))
        else:
            return cls(libhmatrix.read_hlib_hmatrix(file))

    # ***** Properties *****

    def __getter_rc(self) -> 'Cluster':
        return try_wrap(self.cobj().rc, Cluster)

    def __getter_cc(self) -> 'Cluster':
        return try_wrap(self.cobj().cc, Cluster)

    def __getter_r(self) -> 'RkMatrix':
        return try_wrap(self.cobj().r, RkMatrix)

    def __getter_f(self) -> 'AMatrix':
        return try_wrap(self.cobj().f, AMatrix)

    # def __getter_sons(self) -> List['HMatrix']:
    #     lst = cptr_to_list(self.cobj().son, self.rsons * self.csons??)
    #     return [try_wrap(cs, HMatrix) for cs in lst]

    def __getter_rsons(self) -> int:
        return self.cobj().rsons

    def __getter_csons(self) -> int:
        return self.cobj().csons

    def __getter_refs(self) -> int:
        return self.cobj().refs

    def __getter_desc(self) -> int:
        return self.cobj().desc

    # ***** Methods ******

    def clone(self, *, structure_only: bool = False) -> 'HMatrix':
        if structure_only:
            return try_wrap(libhmatrix.clonestructure_hmatrix(self), HMatrix)
        else:
            return try_wrap(libhmatrix.clone_hmatrix(self), HMatrix)

    def update(self):
        libhmatrix.update_hmatrix(self)

    def ref(self, ptr: 'HMatrix'):
        libhmatrix.ref_hmatrix(pointer(ptr), self)

    def unref(self):
        libhmatrix.unref_hmatrix(self)

    def size(self, *, part: 'SizePart' = SizePart.All):
        if part == SizePart.Near:
            return libhmatrix.getnearsize_hmatrix(self)
        elif part == SizePart.Far:
            return libhmatrix.getfarsize_hmatrix(self)
        else:  # part == SizePart.All
            return libhmatrix.getsize_hmatrix(self)

    def clear(self, *, clear_type: 'ClearType' = ClearType.All):
        if clear_type == ClearType.Upper:
            libhmatrix.clear_upper_hmatrix(self, False)
        elif clear_type == ClearType.UpperStrict:
            libhmatrix.clear_upper_hmatrix(self, True)
        elif clear_type == ClearType.All:
            libhmatrix.clear_hmatrix(self)
        else:
            raise ValueError('Clearing lower part not supported.')

    def copy(self, target: 'HMatrix'):
        libhmatrix.copy_hmatrix(self, target)

    def identity(self):
        libhmatrix.identity_hmatrix(self)

    def rand(self, k: int):
        libhmatrix.random_hmatrix(self, k)

    def enumerate(self, b: 'Block') -> List['HMatrix']:
        ptr = libhmatrix.enumerate_hmatrix(b, self)
        return cptr_to_list(ptr, b.desc)

    def norm(self):
        return libhmatrix.norm2_hmatrix(self)

    def norm2_diff(self, other: 'HMatrix') -> float:
        return libhmatrix.norm2diff_hmatrix(self, other)

    def write_file(self, file: str):
        libhmatrix.write_hlib_hmatrix(self, file)
