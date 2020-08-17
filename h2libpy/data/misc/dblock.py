from ctypes import c_void_p, cast
from typing import List

import h2libpy.data.misc as misc
import h2libpy.lib.dblock as libdblock
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import cptr_to_list, try_wrap


class DBlock(StructWrapper, cstruct=libdblock.CStructDBlock):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, rc: 'misc.DCluster', cc: 'misc.DCluster', rd: int, cd: int,
            rsons: int, csons: int) -> 'DBlock':
        return cls(libdblock.new_dblock(rc, cc, rd, cd, rsons, csons))

    @classmethod
    def build(cls, rc: 'misc.DCluster', cc: 'misc.DCluster', l: int,
              admissible, data) -> 'DBlock':
        cadmissible = libdblock.CFuncAdmissible(admissible)
        cdata = cast(data, c_void_p)
        return cls(libdblock.build_dblock(rc, cc, l, cadmissible, cdata))

    # ***** Properties *****

    def __gettter_rc(self) -> 'misc.DCluster':
        return try_wrap(self.cobj().rc, misc.DCluster)

    def __gettter_cc(self) -> 'misc.DCluster':
        return try_wrap(self.cobj().cc, misc.DCluster)

    def __getter_rd(self) -> int:
        return self.cobj().rd

    def __getter_cd(self) -> int:
        return self.cobj().cd

    def __getter_adm(self) -> bool:
        return self.cobj().a

    def __getter_rsons(self) -> int:
        return self.cobj().rsons

    def __getter_csons(self) -> int:
        return self.cobj().csons

    # def __getter_son(self) -> List['DBlock']:
    #     return self.cobj().son

    def __getter_desc(self) -> int:
        return self.cobj().desc

    # ***** Methods ******

    def update(self) -> None:
        libdblock.update_dblock(self)

    def size(self) -> int:
        return libdblock.getsize_dblock(self)

    def depth(self) -> int:
        return libdblock.getdepth_dblock(self)

    def max_eta(self) -> float:
        return libdblock.getmaxeta_dblock(self)

    def remove_unused_direction(self, t: 'misc.DCluster',
                                lold: 'misc.LevelDir') -> 'misc.LevelDir':
        obj = libdblock.remove_unused_direction(self, t, lold)
        return try_wrap(obj, misc.LevelDir)

    def enumerate(self) -> List['DBlock']:
        ptr = libdblock.enumerate_dblock(self)
        lst = cptr_to_list(ptr, self.desc)
        return [try_wrap(cs, DBlock) for cs in lst]
