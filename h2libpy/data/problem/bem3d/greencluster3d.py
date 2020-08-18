import h2libpy.data.matrix as mat
import h2libpy.data.misc as misc
import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import try_wrap


class GreenCluster3d(StructWrapper, cstruct=libbem3d.CStructGreenCluster3d):
    # ***** Fields *****
    V: 'mat.AMatrix'
    t: 'misc.Cluster'
    sons: int

    # ***** Properties *****

    def __getter_V(self) -> 'mat.AMatrix':
        return try_wrap(self.cobj().V, mat.AMatrix)

    def __getter_t(self) -> 'misc.Cluster':
        return try_wrap(self.cobj().t, misc.Cluster)

    def __getter_sons(self) -> int:
        return self.cobj().sons

    # ***** Methods ******
