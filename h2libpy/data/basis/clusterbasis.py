from ctypes import POINTER, pointer

import h2libpy.lib.clusterbasis as libclusterbasis
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.matrix.amatrix import AMatrix
from h2libpy.data.tree.cluster import Cluster


class ClusterBasis(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libclusterbasis.CStructClusterBasis))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_t(self) -> 'Cluster':
        return Cluster(self.cobj().t)

    def __getter_k(self) -> int:
        return self.cobj().t

    def __getter_ktree(self) -> int:
        return self.cobj().ktree

    def __getter_kbranch(self) -> int:
        return self.cobj().kbranch

    def __getter_V(self) -> 'AMatrix':
        return AMatrix(pointer(self.cobj().V))

    def __getter_E(self) -> 'AMatrix':
        return AMatrix(pointer(self.cobj().E))

    def __getter_sons(self) -> int:
        return self.cobj().sons

    def __getter_Z(self) -> 'AMatrix':
        return AMatrix(self.cobj().Z)

    def __getter_refs(self) -> int:
        return self.cobj().refs

    def __getter_rlist(self) -> 'Uniform':
        from h2libpy.data.misc.uniform import Uniform
        return Uniform(self.cobj().rlist)

    def __getter_rclist(self) -> 'Uniform':
        from h2libpy.data.misc.uniform import Uniform
        return Uniform(self.cobj().clist)

    # ***** Methods ******
