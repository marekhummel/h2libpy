from ctypes import POINTER

import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.matrix.amatrix import AMatrix
from h2libpy.data.basis.clusterbasis import ClusterBasis


class GreenClusterBasis3d(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libbem3d.CStructGreenClusterBasis3d))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_Qinv(self) -> AMatrix:
        return AMatrix(self.cobj().Qinv)

    def __getter_cb(self) -> 'ClusterBasis':
        return ClusterBasis(self.cobj().cb)

    def __getter_sons(self) -> int:
        return self.cobj().sons

    def __getter_m(self) -> int:
        return self.cobj().m

    # ***** Methods ******
