
import h2libpy.data.matrix as mat
import h2libpy.data.misc as misc
import h2libpy.lib.uniform as libuniform
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import try_wrap


class Uniform(StructWrapper, cstruct=libuniform.CStructUniform):

    # ***** Properties *****

    def __getter_rb(self) -> 'misc.ClusterBasis':
        from h2libpy.data.misc.clusterbasis import ClusterBasis
        return try_wrap(self.cobj().rb, ClusterBasis)

    def __getter_cb(self) -> 'misc.ClusterBasis':
        from h2libpy.data.misc.clusterbasis import ClusterBasis
        return try_wrap(self.cobj().cb, ClusterBasis)

    def __getter_S(self) -> 'mat.AMatrix':
        return try_wrap(self.cobj().S, mat.AMatrix)

    def __getter_rnext(self) -> 'Uniform':
        return try_wrap(self.cobj().rnext, Uniform)

    def __getter_rprev(self) -> 'Uniform':
        return try_wrap(self.cobj().rprev, Uniform)

    def __getter_cnext(self) -> 'Uniform':
        return try_wrap(self.cobj().cnext, Uniform)

    def __getter_cprev(self) -> 'Uniform':
        return try_wrap(self.cobj().cprev, Uniform)

    # ***** Methods ******
