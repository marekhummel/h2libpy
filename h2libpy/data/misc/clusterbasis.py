from ctypes import pointer, cast, c_void_p
from typing import List

import h2libpy.lib.clusterbasis as libclusterbasis
from h2libpy.base.util import try_wrap, cptr_to_list
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.matrix.amatrix import AMatrix
from h2libpy.data.vector.avector import AVector
from h2libpy.data.misc.cluster import Cluster
from h2libpy.data.misc.clusteroperator import ClusterOperator


class ClusterBasis(StructWrapper, cstruct=libclusterbasis.CStructClusterBasis):

    @classmethod
    def new(cls, t: 'Cluster', *, leaf: bool) -> 'ClusterBasis':
        if leaf:
            return cls(libclusterbasis.new_leaf_clusterbasis(t))
        else:
            return cls(libclusterbasis.new_clusterbasis(t))

    @classmethod
    def from_cluster(cls, t: 'Cluster') -> 'ClusterBasis':
        return cls(libclusterbasis.build_from_cluster_clusterbasis(t))

    # ***** Properties *****

    def __getter_t(self) -> 'Cluster':
        return try_wrap(self.cobj().t, Cluster)

    def __getter_k(self) -> int:
        return self.cobj().t

    def __getter_ktree(self) -> int:
        return self.cobj().ktree

    def __getter_kbranch(self) -> int:
        return self.cobj().kbranch

    def __getter_V(self) -> 'AMatrix':
        return try_wrap(pointer(self.cobj().V), AMatrix)

    def __getter_E(self) -> 'AMatrix':
        return try_wrap(pointer(self.cobj().E), AMatrix)

    def __getter_sons(self) -> int:
        return self.cobj().sons

    # def __getter_son(self) -> List['ClusterBasis']:
    #     pass

    def __getter_Z(self) -> 'AMatrix':
        return try_wrap(self.cobj().Z, AMatrix)

    def __getter_refs(self) -> int:
        return self.cobj().refs

    def __getter_rlist(self) -> 'Uniform':
        from h2libpy.data.misc.uniform import Uniform
        return try_wrap(self.cobj().rlist, Uniform)

    def __getter_rclist(self) -> 'Uniform':
        from h2libpy.data.misc.uniform import Uniform
        return try_wrap(self.cobj().clist, Uniform)

    # ***** Methods ******

    def ref(self, ptr: 'ClusterBasis'):
        libclusterbasis.ref_clusterbasis(pointer(ptr), self)

    def unref(self):
        libclusterbasis.unref_clusterbasis(self)

    def update(self):
        libclusterbasis.update_clusterbasis(self)

    def update_tree(self):
        libclusterbasis.update_tree_clusterbasis(self)

    def resize(self, k: int):
        libclusterbasis.resize_clusterbasis(self, k)

    def setrank(self, k: int):
        libclusterbasis.setrank_clusterbasis(self, k)

    def clone(self, *, structure_only: bool = False) -> 'ClusterBasis':
        if structure_only:
            obj = libclusterbasis.clonestructure_clusterbasis(self)
            return try_wrap(obj, ClusterBasis)
        else:
            obj = libclusterbasis.clone_clusterbasis(self)
            return try_wrap(obj, ClusterBasis)

    def size(self) -> int:
        return libclusterbasis.getsize_clusterbasis(self)

    def clear_weight(self):
        libclusterbasis.clear_weight_clusterbasis(self)

    def iterate(self, cbname: int, pre, post, data):
        cpre = libclusterbasis.CFuncClusterBasisCallbackT(pre)
        cpost = libclusterbasis.CFuncClusterBasisCallbackT(post)
        cdata = cast(data, c_void_p)
        libclusterbasis.iterate_clusterbasis(self, cbname, cpre, cpost, cdata)

    def iterate_parallel(self, cbname: int, pardepth: int, pre, post, data):
        cpre = libclusterbasis.CFuncClusterBasisCallbackT(pre)
        cpost = libclusterbasis.CFuncClusterBasisCallbackT(post)
        cdata = cast(data, c_void_p)
        libclusterbasis.iterate_parallel_clusterbasis(self, cbname, pardepth,
                                                      cpre, cpost, cdata)

    def enumerate(self, t: 'Cluster') -> List['ClusterBasis']:
        ptr = libclusterbasis.enumerate_cluster(t, self)
        lst = cptr_to_list(ptr, t.desc)
        return [try_wrap(c, ClusterBasis) for c in lst]

    def new_coeffs(self) -> 'AVector':
        obj = libclusterbasis.new_coeffs_clusterbasis_avector(self)
        return try_wrap(obj, AVector)

    def ortho(self, co: 'ClusterOperator'):
        libclusterbasis.ortho_clusterbasis(self, co)

    def check_ortho(self) -> float:
        return libclusterbasis.check_ortho_clusterbasis(self)

    def weight(self, co: 'ClusterOperator') -> 'ClusterOperator':
        obj = libclusterbasis.weight_clusterbasis_clusteroperator(self, co)
        return try_wrap(obj, ClusterOperator)

    def weight_enum(self) -> 'AMatrix':
        obj = libclusterbasis.weight_enum_clusterbasis_clusteroperator(self)
        return try_wrap(obj, AMatrix)
