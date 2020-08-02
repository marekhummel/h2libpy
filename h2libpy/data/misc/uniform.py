
import h2libpy.lib.uniform as libuniform
from h2libpy.base.cutil import try_wrap
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.matrix.amatrix import AMatrix


class Uniform(StructWrapper, cstruct=libuniform.CStructUniform):

    # ***** Properties *****

    def __getter_rb(self) -> 'ClusterBasis':
        from h2libpy.data.basis.clusterbasis import ClusterBasis
        return try_wrap(self.cobj().rb, ClusterBasis)

    def __getter_cb(self) -> 'ClusterBasis':
        from h2libpy.data.basis.clusterbasis import ClusterBasis
        return try_wrap(self.cobj().cb, ClusterBasis)

    def __getter_S(self) -> 'AMatrix':
        return try_wrap(self.cobj().S, AMatrix)

    def __getter_rnext(self) -> 'Uniform':
        return try_wrap(self.cobj().rnext, Uniform)

    def __getter_rprev(self) -> 'Uniform':
        return try_wrap(self.cobj().rprev, Uniform)

    def __getter_cnext(self) -> 'Uniform':
        return try_wrap(self.cobj().cnext, Uniform)

    def __getter_cprev(self) -> 'Uniform':
        return try_wrap(self.cobj().cprev, Uniform)

    # ***** Methods ******
