
import h2libpy.data.matrix as mat
import h2libpy.data.misc as misc
import h2libpy.lib.uniform as libuniform
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import try_wrap
from ctypes import pointer


class Uniform(StructWrapper, cstruct=libuniform.CStructUniform):
    # ***** Fields *****
    rb: 'misc.ClusterBasis'
    cb: 'misc.ClusterBasis'
    S: 'mat.AMatrix'
    rnext: 'Uniform'
    rprev: 'Uniform'
    cnext: 'Uniform'
    cprev: 'Uniform'

    # ***** Constructors *****

    @classmethod
    def new(cls, rb: 'misc.ClusterBasis', cb: 'misc.ClusterBasis') \
            -> 'Uniform':
        return cls(libuniform.new_uniform(rb, cb))

    # ***** Properties *****

    def __getter_rb(self) -> 'misc.ClusterBasis':
        return try_wrap(self.cobj().rb, misc.ClusterBasis)

    def __getter_cb(self) -> 'misc.ClusterBasis':
        return try_wrap(self.cobj().cb, misc.ClusterBasis)

    def __getter_S(self) -> 'mat.AMatrix':
        return try_wrap(pointer(self.cobj().S), mat.AMatrix)

    def __getter_rnext(self) -> 'Uniform':
        return try_wrap(self.cobj().rnext, Uniform)

    def __getter_rprev(self) -> 'Uniform':
        return try_wrap(self.cobj().rprev, Uniform)

    def __getter_cnext(self) -> 'Uniform':
        return try_wrap(self.cobj().cnext, Uniform)

    def __getter_cprev(self) -> 'Uniform':
        return try_wrap(self.cobj().cprev, Uniform)

    # ***** Methods ******

    def ref_row(self, rb: 'misc.ClusterBasis') -> None:
        libuniform.ref_row_uniform(self, rb)

    def ref_col(self, cb: 'misc.ClusterBasis') -> None:
        libuniform.ref_col_uniform(self, cb)

    def unref_row(self) -> None:
        libuniform.unref_row_uniform(self)

    def unref_col(self) -> None:
        libuniform.unref_col_uniform(self)

    def memsize(self) -> int:
        return libuniform.getsize_uniform(self)

    def clear(self) -> None:
        libuniform.clear_uniform(self)

    def copy(self, trans: bool, target: 'Uniform') -> None:
        libuniform.copy_uniform(self, trans, target)

    def clone(self) -> 'Uniform':
        return try_wrap(libuniform.clone_uniform(self), Uniform)

    def scale(self, alpha: float) -> None:
        libuniform.scale_uniform(alpha, self)

    def rand(self) -> None:
        libuniform.random_uniform(self)

    def add_projected(self, ro: 'misc.ClusterOperator',
                      co: 'misc.ClusterOperator', unew: 'Uniform'):
        libuniform.add_projected_uniform(self, ro, co, unew)

    def project_inplace(self,
                        rb: 'misc.ClusterBasis', ro: 'misc.ClusterOperator',
                        cb: 'misc.ClusterBasis', co: 'misc.ClusterOperator'):
        libuniform.project_inplace_uniform(self, rb, ro, cb, co)

    def add_rkmatrix(self, r: 'mat.RkMatrix') -> None:
        libuniform.add_rkmatrix_uniform(r, self)

    def delete(self) -> None:
        super().delete(libuniform.del_uniform)
