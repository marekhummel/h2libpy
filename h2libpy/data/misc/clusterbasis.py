from ctypes import c_void_p, cast, pointer
from typing import List

import h2libpy.data.matrix as mat
import h2libpy.data.misc as misc
import h2libpy.data.vector as vec
import h2libpy.lib.clusterbasis as libclusterbasis
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import cptr_to_list, try_wrap


class ClusterBasis(StructWrapper, cstruct=libclusterbasis.CStructClusterBasis):
    # ***** Fields *****
    t: 'misc.Cluster'
    k: int
    ktree: int
    kbranch: int
    V: 'mat.AMatrix'
    E: 'mat.AMatrix'
    sons: int
    Z: 'mat.AMatrix'
    refs: int
    rlist: 'misc.Uniform'
    rclist: 'misc.Uniform'

    # ***** Constructors *****

    def __init__(self):
        self.cobj().refs += 1

    @classmethod
    def new(cls, t: 'misc.Cluster', *, leaf: bool) -> 'ClusterBasis':
        if leaf:
            return cls(libclusterbasis.new_leaf_clusterbasis(t))
        else:
            return cls(libclusterbasis.new_clusterbasis(t))

    @classmethod
    def from_cluster(cls, t: 'misc.Cluster') -> 'ClusterBasis':
        return cls(libclusterbasis.build_from_cluster_clusterbasis(t))

    # ***** Properties *****

    def __getter_t(self) -> 'misc.Cluster':
        return try_wrap(self.cobj().t, misc.Cluster)

    def __getter_k(self) -> int:
        return self.cobj().t

    def __getter_ktree(self) -> int:
        return self.cobj().ktree

    def __getter_kbranch(self) -> int:
        return self.cobj().kbranch

    def __getter_V(self) -> 'mat.AMatrix':
        return try_wrap(pointer(self.cobj().V), mat.AMatrix)

    def __getter_E(self) -> 'mat.AMatrix':
        return try_wrap(pointer(self.cobj().E), mat.AMatrix)

    def __getter_sons(self) -> int:
        return self.cobj().sons

    # def __getter_son(self) -> List['ClusterBasis']:
    #     pass

    def __getter_Z(self) -> 'mat.AMatrix':
        return try_wrap(self.cobj().Z, mat.AMatrix)

    def __getter_refs(self) -> int:
        return self.cobj().refs

    def __getter_rlist(self) -> 'misc.Uniform':
        return try_wrap(self.cobj().rlist, misc.Uniform)

    def __getter_rclist(self) -> 'misc.Uniform':
        return try_wrap(self.cobj().clist, misc.Uniform)

    # ***** Methods ******

    def ref(self, ptr: 'ClusterBasis') -> None:
        libclusterbasis.ref_clusterbasis(pointer(ptr.cobj()), self)

    def unref(self) -> None:
        libclusterbasis.unref_clusterbasis(self)

    def update(self) -> None:
        libclusterbasis.update_clusterbasis(self)

    def update_tree(self) -> None:
        libclusterbasis.update_tree_clusterbasis(self)

    def resize(self, k: int) -> None:
        libclusterbasis.resize_clusterbasis(self, k)

    def setrank(self, k: int) -> None:
        libclusterbasis.setrank_clusterbasis(self, k)

    def clone(self, *, structure_only: bool = False) -> 'ClusterBasis':
        if structure_only:
            obj = libclusterbasis.clonestructure_clusterbasis(self)
            return try_wrap(obj, ClusterBasis)
        else:
            obj = libclusterbasis.clone_clusterbasis(self)
            return try_wrap(obj, ClusterBasis)

    def memsize(self) -> int:
        return libclusterbasis.getsize_clusterbasis(self)

    def clear_weight(self) -> None:
        libclusterbasis.clear_weight_clusterbasis(self)

    def iterate(self, cbname: int, pre, post, data) -> None:
        cpre = libclusterbasis.CFuncClusterBasisCallbackT(pre)
        cpost = libclusterbasis.CFuncClusterBasisCallbackT(post)
        cdata = cast(data, c_void_p)
        libclusterbasis.iterate_clusterbasis(self, cbname, cpre, cpost, cdata)

    def iterate_parallel(self, cbname: int, pardepth: int, pre, post, data) \
            -> None:
        cpre = libclusterbasis.CFuncClusterBasisCallbackT(pre)
        cpost = libclusterbasis.CFuncClusterBasisCallbackT(post)
        cdata = cast(data, c_void_p)
        libclusterbasis.iterate_parallel_clusterbasis(self, cbname, pardepth,
                                                      cpre, cpost, cdata)

    def enumerate(self, t: 'misc.Cluster') -> List['ClusterBasis']:
        ptr = libclusterbasis.enumerate_clusterbasis(t, self)
        lst = cptr_to_list(ptr, t.desc)
        return [try_wrap(c, ClusterBasis) for c in lst]

    def new_coeffs(self) -> 'vec.AVector':
        obj = libclusterbasis.new_coeffs_clusterbasis_avector(self)
        return try_wrap(obj, vec.AVector)

    def ortho(self, co: 'misc.ClusterOperator') -> None:
        libclusterbasis.ortho_clusterbasis(self, co)

    def check_ortho(self) -> float:
        return libclusterbasis.check_ortho_clusterbasis(self)

    def weight(self, co: 'misc.ClusterOperator') -> 'misc.ClusterOperator':
        obj = libclusterbasis.weight_clusterbasis_clusteroperator(self, co)
        return try_wrap(obj, misc.ClusterOperator)

    def weight_enum(self) -> 'mat.AMatrix':
        obj = libclusterbasis.weight_enum_clusterbasis_clusteroperator(self)
        return try_wrap(obj, mat.AMatrix)

    def delete(self) -> None:
        self.cobj().refs -= 1
        libclusterbasis.del_clusterbasis(self)
