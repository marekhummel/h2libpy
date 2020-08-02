from ctypes import pointer

import h2libpy.lib.clusterbasis as libclusterbasis
from h2libpy.base.cutil import try_wrap
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.matrix.amatrix import AMatrix
from h2libpy.data.tree.cluster import Cluster


class ClusterBasis(StructWrapper, cstruct=libclusterbasis.CStructClusterBasis):

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
