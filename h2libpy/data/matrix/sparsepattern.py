import h2libpy.lib.sparsematrix as libsparsematrix
from h2libpy.base.structwrapper import StructWrapper


class SparsePattern(StructWrapper,
                    cstruct=libsparsematrix.CStructSparsePattern):
    pass
