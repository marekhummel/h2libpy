import h2libpy.data.matrix as mat
import h2libpy.data.misc as misc
import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import try_wrap


class GreenClusterBasis3d(StructWrapper,
                          cstruct=libbem3d.CStructGreenClusterBasis3d):
    # ***** Fields *****
    Qinv: 'mat.AMatrix'
    cb: 'misc.ClusterBasis'
    sons: int
    m: int

    # ***** Properties *****

    def __getter_Qinv(self) -> 'mat.AMatrix':
        return try_wrap(self.cobj().Qinv, mat.AMatrix)

    def __getter_cb(self) -> 'misc.ClusterBasis':
        return try_wrap(self.cobj().cb, misc.ClusterBasis)

    def __getter_sons(self) -> int:
        return self.cobj().sons

    def __getter_m(self) -> int:
        return self.cobj().m

    # ***** Methods ******
