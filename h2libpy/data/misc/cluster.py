from ctypes import c_uint, c_void_p, cast
from typing import List

import h2libpy.data.misc as misc
import h2libpy.lib.cluster as libcluster
import h2libpy.lib.clustergeometry as libclustergeometry
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import cptr_to_list, pylist_to_ptr, try_wrap


class Cluster(StructWrapper, cstruct=libcluster.CStructCluster):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, size: int, idx: List[int], sons: int, dim: int) -> 'Cluster':
        cidx = pylist_to_ptr(idx, c_uint)
        return cls(libcluster.new_cluster(size, cidx, sons, dim))

    @classmethod
    def build_adaptive(cls, cf: 'misc.ClusterGeometry', size: int,
                       idx: List[int], clf: int) -> 'Cluster':
        cidx = pylist_to_ptr(idx, c_uint)
        return cls(libcluster.build_adaptive_cluster(cf, size, cidx, clf))

    @classmethod
    def build_regular(cls, cf: 'misc.ClusterGeometry', size: int,
                      idx: List[int], clf: int, direction: int) -> 'Cluster':
        cidx = pylist_to_ptr(idx, c_uint)
        obj = libcluster.build_regular_cluster(cf, size, cidx, clf, direction)
        return cls(obj)

    @classmethod
    def build_simsub(cls, cf: 'misc.ClusterGeometry', size: int,
                     idx: List[int], clf: int) -> 'Cluster':
        cidx = pylist_to_ptr(idx, c_uint)
        return cls(libcluster.build_simsub_cluster(cf, size, cidx, clf))

    @classmethod
    def build_pca(cls, cf: 'misc.ClusterGeometry', size: int, idx: List[int],
                  clf: int) -> 'Cluster':
        cidx = pylist_to_ptr(idx, c_uint)
        return cls(libcluster.build_pca_cluster(cf, size, cidx, clf))

    @classmethod
    def build(cls, cf: 'misc.ClusterGeometry', size: int, idx: List[int],
              clf: int, mode: 'misc.ClusterMode') -> 'Cluster':
        cidx = pylist_to_ptr(idx, c_uint)
        return cls(libcluster.build_cluster(cf, size, cidx, clf, mode.value))

    # ***** Properties *****

    def __getter_size(self) -> int:
        return self.cobj().size

    # def __getter_idx(self) -> List[int]:
    #     return self.cobj().idx

    def __getter_sons(self) -> int:
        return self.cobj().sons

    # def __getter_son(self) -> List['Cluster']:
    #     return self.cobj().son

    def __getter_dim(self) -> int:
        return self.cobj().dim

    # def __getter_bmin(self) -> List[float]:
    #     return self.cobj().bmin

    # def __getter_bmax(self) -> List[float]:
    #     return self.cobj().bmax

    def __getter_desc(self) -> int:
        return self.cobj().desc

    def __getter_type(self) -> int:
        return self.cobj().type

    # ***** Methods ******

    def update(self) -> None:
        libcluster.update_cluster(self)

    def depth(self, *, minlvl: bool = True) -> int:
        if minlvl:
            return libcluster.getmindepth_cluster(self)
        else:
            return libcluster.getdepth_cluster(self)

    def extend(self, depth: int) -> None:
        libcluster.extend_cluster(self, depth)

    def cut(self, depth: int) -> None:
        libcluster.cut_cluster(self, depth)

    def balance(self, depth: int) -> None:
        libcluster.balance_cluster(self, depth)

    def coarsen(self, minsize: int) -> None:
        libcluster.coarsen_cluster(self, minsize)

    def setsons(self, sons: int) -> None:
        libcluster.setsons_cluster(self, sons)

    def diam2(self) -> float:
        return libcluster.getdiam_2_cluster(self)

    def dist2(self, other: 'Cluster') -> float:
        return libcluster.getdist_2_cluster(self, other)

    def diam_max(self) -> float:
        return libcluster.getdiam_max_cluster(self)

    def dist_max(self, other: 'Cluster') -> float:
        return libcluster.getdist_max_cluster(self, other)

    def iterate(self, tname: int, pre, post, data) -> None:
        cpre = libcluster.CFuncClusterCallbackT(pre)
        cpost = libcluster.CFuncClusterCallbackT(post)
        cdata = cast(data, c_void_p)
        libcluster.iterate_cluster(self, tname, cpre, cpost, cdata)

    def iterate_parallel(self, tname: int, pardepth: int, pre, post, data) \
            -> None:
        cpre = libcluster.CFuncClusterCallbackT(pre)
        cpost = libcluster.CFuncClusterCallbackT(post)
        cdata = cast(data, c_void_p)
        libcluster.iterate_parallel_cluster(self, tname, pardepth,
                                            cpre, cpost, cdata)

    def enumerate(self) -> List['Cluster']:
        ptr = libcluster.enumerate_cluster(self)
        lst = cptr_to_list(ptr, self.desc)
        return [try_wrap(c, Cluster) for c in lst]

    # -------

    def update_bbox(self) -> None:
        libclustergeometry.update_bbox_cluster(self)
