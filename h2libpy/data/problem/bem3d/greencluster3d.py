import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.util import try_wrap
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.matrix.amatrix import AMatrix
from h2libpy.data.misc.cluster import Cluster


class GreenCluster3d(StructWrapper, cstruct=libbem3d.CStructGreenCluster3d):
    # ***** Properties *****

    def __getter_V(self) -> 'AMatrix':
        return try_wrap(self.cobj().V, AMatrix)

    def __getter_t(self) -> 'Cluster':
        return try_wrap(self.cobj().t, Cluster)

    def __getter_sons(self) -> int:
        return self.cobj().sons

    # ***** Methods ******
