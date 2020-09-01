import h2libpy.lib.sparsepattern as libsparsepattern
from h2libpy.base.structwrapper import StructWrapper


class SparsePattern(StructWrapper,
                    cstruct=libsparsepattern.CStructSparsePattern):
    # ***** Fields *****
    rows: int
    cols: int

    # ***** Constructors *****

    @classmethod
    def new(cls, rows: int, cols: int) -> 'SparsePattern':
        return cls(libsparsepattern.new_sparsepattern(rows, cols))

    # ***** Properties *****

    def __getter_rows(self) -> int:
        return self.cobj().rows

    def __getter_cols(self) -> int:
        return self.cobj().cols

    # def __getter_row(self):
    #     pass

    # ***** Methods ******

    def clear(self) -> None:
        libsparsepattern.clear_sparsepattern(self)

    def add_nz(self, row: int, col: int) -> None:
        libsparsepattern.addnz_sparsepattern(self, row, col)

    def print(self) -> None:
        libsparsepattern.print_sparsepattern(self)

    def delete(self) -> None:
        super().delete(libsparsepattern.del_sparsepattern)
