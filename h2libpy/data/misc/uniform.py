from ctypes import POINTER

import h2libpy.lib.uniform as libuniform
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.matrix.amatrix import AMatrix


class Uniform(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libuniform.CStructUniform))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_rb(self) -> 'ClusterBasis':
        from h2libpy.data.basis.clusterbasis import ClusterBasis
        return ClusterBasis(self.cobj().rb)

    def __getter_cb(self) -> 'ClusterBasis':
        from h2libpy.data.basis.clusterbasis import ClusterBasis
        return ClusterBasis(self.cobj().cb)

    def __getter_S(self) -> 'AMatrix':
        return AMatrix(self.cobj().S)

    def __getter_rnext(self) -> 'Uniform':
        return Uniform(self.cobj().rnext)

    def __getter_rprev(self) -> 'Uniform':
        return Uniform(self.cobj().rprev)

    def __getter_cnext(self) -> 'Uniform':
        return Uniform(self.cobj().cnext)

    def __getter_cprev(self) -> 'Uniform':
        return Uniform(self.cobj().cprev)

    # ***** Methods ******
