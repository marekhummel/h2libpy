import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.cutil import try_wrap
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.matrix.amatrix import AMatrix
from h2libpy.data.tree.cluster import Cluster


class GreenCluster3d(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        super().__init__(cobj, libbem3d.CStructGreenCluster3d)

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_V(self) -> 'AMatrix':
        return try_wrap(self.cobj().V, AMatrix)

    def __getter_t(self) -> 'Cluster':
        return try_wrap(self.cobj().t, Cluster)

    def __getter_sons(self) -> int:
        return self.cobj().sons

    # ***** Methods ******
