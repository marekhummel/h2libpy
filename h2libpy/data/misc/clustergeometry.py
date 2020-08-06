
from ctypes import c_uint
from typing import List

import h2libpy.data.misc as misc
import h2libpy.lib.clustergeometry as libclustergeometry
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import pylist_to_ptr


class ClusterGeometry(StructWrapper,
                      cstruct=libclustergeometry.CStructClusterGeometry):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, dim: int, nidx: int) -> 'ClusterGeometry':
        return cls(libclustergeometry.new_clustergeometry(dim, nidx))

    # ***** Properties *****

    def __getter_dim(self) -> int:
        return self.cobj().dim

    def __getter_nidx(self) -> int:
        return self.cobj().nidx

    # ***** Methods ******

    def update_point_bbox(self, size: int, idx: List[int]):
        cidx = pylist_to_ptr(idx, c_uint)
        libclustergeometry.update_point_bbox_clustergeometry(self, size, cidx)

    def update_support_bbox(self, t: 'misc.Cluster'):
        libclustergeometry.update_support_bbox_cluster(self, t)
