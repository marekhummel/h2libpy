from typing import List

import h2libpy.lib.dcluster as libdcluster
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import pylist_to_ptr
from h2libpy.lib.settings import real


class LevelDir(StructWrapper, cstruct=libdcluster.CStructLevelDir):
    # ***** Fields *****
    depth: int
    dim: int

    # ***** Constructors *****

    @classmethod
    def new(cls, depth: int, dim: int) -> 'LevelDir':
        return cls(libdcluster.new_leveldir(depth, dim))

    # ***** Properties *****

    def __getter_depth(self) -> int:
        return self.cobj().depth

    def __getter_dim(self) -> int:
        return self.cobj().dim

    # ***** Methods ******

    def delete(self) -> None:
        libdcluster.del_leveldir(self)

    def find_direction(self, l: int, alpha: float, d: List[float]) -> int:
        cd = pylist_to_ptr(d, real)
        return libdcluster.finddirection_leveldir(self, l, alpha, cd)
