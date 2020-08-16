from ctypes import pointer
from typing import List

import h2libpy.data.matrix as mat
import h2libpy.data.misc as misc
import h2libpy.lib.hmatrix as libhmatrix
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import cptr_to_list, try_wrap


class HMatrix(StructWrapper, cstruct=libhmatrix.CStructHMatrix):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, rc: 'misc.Cluster', cc: 'misc.Cluster') -> 'mat.HMatrix':
        return cls(libhmatrix.new_hmatrix(rc, cc))

    @classmethod
    def new_rk(cls, rc: 'misc.Cluster', cc: 'misc.Cluster', k: int) \
            -> 'mat.HMatrix':
        return cls(libhmatrix.new_rk_hmatrix(rc, cc, k))

    @classmethod
    def new_full(cls, rc: 'misc.Cluster', cc: 'misc.Cluster') -> 'mat.HMatrix':
        return cls(libhmatrix.new_full_hmatrix(rc, cc))

    @classmethod
    def new_super(cls, rc: 'misc.Cluster', cc: 'misc.Cluster',
                  rsons: int, csons: int) -> 'mat.HMatrix':
        return cls(libhmatrix.new_super_hmatrix(rc, cc, rsons, csons))

    @classmethod
    def from_block(cls, b: 'misc.Block', k: int) -> 'mat.HMatrix':
        return cls(libhmatrix.build_from_block_hmatrix(b, k))

    @classmethod
    def from_file(cls, file: str, is_symmetric: bool):
        cfile = file.encode()
        if is_symmetric:
            return cls(libhmatrix.read_hlibsymm_hmatrix(cfile))
        else:
            return cls(libhmatrix.read_hlib_hmatrix(cfile))

    # ***** Properties *****

    def __getter_rc(self) -> 'misc.Cluster':
        return try_wrap(self.cobj().rc, misc.Cluster)

    def __getter_cc(self) -> 'misc.Cluster':
        return try_wrap(self.cobj().cc, misc.Cluster)

    def __getter_r(self) -> 'mat.RkMatrix':
        return try_wrap(self.cobj().r, mat.RkMatrix)

    def __getter_f(self) -> 'mat.AMatrix':
        return try_wrap(self.cobj().f, mat.AMatrix)

    # def __getter_sons(self) -> List['mat.HMatrix']:
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

    def clone(self, *, structure_only: bool = False) -> 'mat.HMatrix':
        if structure_only:
            return try_wrap(libhmatrix.clonestructure_hmatrix(self), HMatrix)
        else:
            return try_wrap(libhmatrix.clone_hmatrix(self), HMatrix)

    def update(self):
        libhmatrix.update_hmatrix(self)

    def ref(self, ptr: 'mat.HMatrix'):
        libhmatrix.ref_hmatrix(pointer(ptr), self)

    def unref(self):
        libhmatrix.unref_hmatrix(self)

    def size(self, *, part: 'mat.SizePart' = mat.SizePart.Total):
        if part == mat.SizePart.Near:
            return libhmatrix.getnearsize_hmatrix(self)
        elif part == mat.SizePart.Far:
            return libhmatrix.getfarsize_hmatrix(self)
        else:  # part == mat.SizePart.Total || part == mat.SizePart.Object:
            return libhmatrix.getsize_hmatrix(self)

    def clear(self, *, clear_type: 'mat.ClearType' = mat.ClearType.All):
        if clear_type == mat.ClearType.Upper:
            libhmatrix.clear_upper_hmatrix(self, False)
        elif clear_type == mat.ClearType.UpperStrict:
            libhmatrix.clear_upper_hmatrix(self, True)
        elif clear_type == mat.ClearType.All:
            libhmatrix.clear_hmatrix(self)
        else:
            raise ValueError('Clearing lower part not supported.')

    def copy(self, target: 'mat.HMatrix'):
        libhmatrix.copy_hmatrix(self, target)

    def identity(self):
        libhmatrix.identity_hmatrix(self)

    def rand(self, k: int):
        libhmatrix.random_hmatrix(self, k)

    def enumerate(self, b: 'misc.Block') -> List['mat.HMatrix']:
        ptr = libhmatrix.enumerate_hmatrix(b, self)
        lst = cptr_to_list(ptr, b.desc)
        return [try_wrap(cs, HMatrix) for cs in lst]

    def norm(self):
        return libhmatrix.norm2_hmatrix(self)

    def norm2_diff(self, other: 'mat.HMatrix') -> float:
        return libhmatrix.norm2diff_hmatrix(self, other)

    def write_file(self, file: str):
        libhmatrix.write_hlib_hmatrix(self, file.encode())
