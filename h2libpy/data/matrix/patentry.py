import h2libpy.lib.sparsepattern as libsparsepattern
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import try_wrap


class PatEntry(StructWrapper, cstruct=libsparsepattern.CStructPatEntry):

    # ***** Properties *****

    def __getter_row(self) -> int:
        return self.cobj().row

    def __getter_col(self) -> int:
        return self.cobj().col

    def __getter_next(self) -> 'PatEntry':
        return try_wrap(self.cobj().next, PatEntry)
