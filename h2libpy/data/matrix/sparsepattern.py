import h2libpy.lib.sparsepattern as libsparsepattern
from h2libpy.base.structwrapper import StructWrapper


class SparsePattern(StructWrapper,
                    cstruct=libsparsepattern.CStructSparsePattern):
    pass
