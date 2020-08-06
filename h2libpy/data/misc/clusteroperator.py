
from ctypes import pointer
from typing import List

import h2libpy.data.matrix as mat
import h2libpy.data.misc as misc
import h2libpy.lib.clusteroperator as libclusteroperator
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import cptr_to_list, try_wrap


class ClusterOperator(StructWrapper,
                      cstruct=libclusteroperator.CStructClusterOperator):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, t: 'misc.Cluster', *, leaf: bool = False) \
            -> 'ClusterOperator':
        if leaf:
            return cls(libclusteroperator.new_leaf_clusteroperator(t))
        else:
            return cls(libclusteroperator.new_clusteroperator(t))

    @classmethod
    def from_cluster(cls, t: 'misc.Cluster'):
        return cls(libclusteroperator.build_from_cluster_clusteroperator(t))

    @classmethod
    def from_clusterbasis(cls, cb: 'misc.ClusterBasis'):
        obj = libclusteroperator.build_from_clusterbasis_clusteroperator(cb)
        return cls(obj)

    # ***** Properties *****

    def __getter_t(self) -> 'misc.Cluster':
        return try_wrap(self.cobj().t, misc.Cluster)

    def __getter_krow(self) -> int:
        return self.cobj().krow

    def __getter_kcol(self) -> int:
        return self.cobj().kcol

    def __getter_C(self) -> 'mat.AMatrix':
        return try_wrap(pointer(self.cobj().C), mat.AMatrix)

    def __getter_sons(self) -> int:
        return self.cobj().sons

    def __getter_son(self) -> List['ClusterOperator']:
        lst = cptr_to_list(self.cobj().son, self.sons)
        return [try_wrap(co, ClusterOperator) for co in lst]

    def __getter_refs(self) -> int:
        return self.cobj().refs

    # ***** Methods ******

    def remove_sons(self):
        libclusteroperator.removesons_clusteroperator(self)

    def ref(self, ptr: 'ClusterOperator'):
        libclusteroperator.ref_clusteroperator(pointer(ptr), self)

    def unref(self):
        libclusteroperator.unref_clusteroperator(self)

    def update(self):
        libclusteroperator.update_clusteroperator(self)

    def resize(self, krow: int, kcol: int):
        libclusteroperator.resize_clusteroperator(self, krow, kcol)

    def identify_son_clusterweight(self, t: 'misc.Cluster') \
            -> 'ClusterOperator':
        f = libclusteroperator.identify_son_clusterweight_clusteroperator
        return try_wrap(f(self, t), ClusterOperator)

    def size(self) -> int:
        return libclusteroperator.getsize_clusteroperator(self)

    def print_tree(self):
        libclusteroperator.print_tree_clusteroperator(self)

    def norm2diff(self, other: 'ClusterOperator'):
        libclusteroperator.norm2diff_clusteroperator(self, other)

    def compare_weights(self, other: 'ClusterOperator') -> float:
        return libclusteroperator.compareweights_clusteroperator(self, other)

    def enumerate(self, t: 'misc.Cluster') -> List['ClusterOperator']:
        ptr = libclusteroperator.enumerate_clusteroperator(self)
        lst = cptr_to_list(ptr, t.desc)
        return [try_wrap(co, ClusterOperator) for co in lst]

    def basis_product(self, cb1: 'misc.ClusterBasis',
                      cb2: 'misc.ClusterBasis'):
        libclusteroperator.basisproduct_clusteroperator(cb1, cb2, self)
