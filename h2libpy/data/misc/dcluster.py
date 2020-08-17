from ctypes import c_uint
from typing import List

import h2libpy.data.misc as misc
import h2libpy.lib.dcluster as libdcluster
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import pylist_to_ptr, try_wrap, cptr_to_list
from h2libpy.lib.settings import real


class DCluster(StructWrapper, cstruct=libdcluster.CStructDCluster):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, size: int, idx: List[int], sons: int, dim: int) -> 'DCluster':
        cidx = pylist_to_ptr(idx, c_uint)
        return libdcluster.new_dcluster(size, cidx, sons, dim)

    @classmethod
    def from_cluster(cls, t: 'misc.Cluster') -> 'DCluster':
        return cls(libdcluster.buildfromcluster_dcluster(t))

    # ***** Properties *****

    def __getter_size(self) -> int:
        return self.cobj().size

    def __getter_idx(self) -> List[int]:
        return cptr_to_list(self.cobj().idx, self.size)

    def __getter_sons(self) -> int:
        return self.cobj().sons

    def __getter_son(self) -> List['DCluster']:
        clist = cptr_to_list(self.cobj().son, self.sons)
        return [try_wrap(dc, DCluster) for dc in clist]

    def __getter_dim(self) -> int:
        return self.cobj().dim

    def __getter_bmin(self) -> List[float]:
        return cptr_to_list(self.cobj().bmin, self.dim)

    def __getter_bmax(self) -> List[float]:
        return cptr_to_list(self.cobj().bmax, self.dim)

    def __getter_directions(self) -> int:
        return self.cobj().directions

    def __getter_desc(self) -> int:
        return self.cobj().desc

    # ***** Methods ******

    def update(self) -> None:
        libdcluster.update_dcluster(self)

    def delete(self) -> None:
        libdcluster.del_dcluster(self)

    def diam(self) -> float:
        return libdcluster.diam_dcluster(self)

    def dist(self, other: 'DCluster') -> float:
        return libdcluster.dist_dcluster(self, other)

    def middist(self, other: 'DCluster') -> float:
        return libdcluster.middist_dcluster(self, other)

    def find_direction(self, alpha: float, d: List[float]) -> int:
        cd = pylist_to_ptr(d, real)
        return libdcluster.finddirection_dcluster(self, alpha, cd)

    def memsize(self) -> int:
        return libdcluster.getsize_dcluster(self)

    def depth(self) -> int:
        return libdcluster.getdepth_dcluster(self)

    def all_directions(self) -> int:
        return libdcluster.getalldirections_dcluster(self)

    def build_directions_box(self, eta1: float) -> 'misc.LevelDir':
        obj = libdcluster.builddirections_box_dcluster(self, eta1)
        return try_wrap(obj, misc.LevelDir)
