from ctypes import POINTER

import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.matrix.amatrix import AMatrix
from h2libpy.data.tree.cluster import Cluster


class GreenCluster3d(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libbem3d.CStructGreenCluster3d))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_V(self) -> 'AMatrix':
        return AMatrix(self.cobj().V)

    def __getter_t(self) -> 'Cluster':
        return Cluster(self.cobj().t)

    def __getter_sons(self) -> int:
        return self.cobj().sons

    # ***** Methods ******
