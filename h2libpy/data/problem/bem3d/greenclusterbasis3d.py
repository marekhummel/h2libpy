import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.cutil import try_wrap
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.misc.clusterbasis import ClusterBasis
from h2libpy.data.matrix.amatrix import AMatrix


class GreenClusterBasis3d(StructWrapper,
                          cstruct=libbem3d.CStructGreenClusterBasis3d):

    # ***** Properties *****

    def __getter_Qinv(self) -> AMatrix:
        return try_wrap(self.cobj().Qinv, AMatrix)

    def __getter_cb(self) -> 'ClusterBasis':
        return try_wrap(self.cobj().cb, ClusterBasis)

    def __getter_sons(self) -> int:
        return self.cobj().sons

    def __getter_m(self) -> int:
        return self.cobj().m

    # ***** Methods ******
