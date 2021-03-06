from typing import List

import h2libpy.data.matrix as mat
import h2libpy.lib.hmatrix as libhmatrix
import h2libpy.lib.sparsematrix as libsparsematrix
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import cptr_to_list
from h2libpy.data.matrix.sparsepattern import SparsePattern


class SparseMatrix(StructWrapper, cstruct=libsparsematrix.CStructSparseMatrix):
    # ***** Fields *****
    rows: int
    cols: int
    nz: int
    coeff: List[float]

    # ***** Constructors *****

    @classmethod
    def new(cls, rows: int, cols: int, nz: int) -> 'SparseMatrix':
        return cls(libsparsematrix.new_raw_sparsematrix(rows, cols, nz))

    @classmethod
    def new_identity(cls, rows: int, cols: int) -> 'SparseMatrix':
        return cls(libsparsematrix.new_identity_sparsematrix(rows, cols))

    @classmethod
    def new_zero(cls, sp: 'SparsePattern') -> 'SparseMatrix':
        return cls(libsparsematrix.new_raw_sparsematrix(sp))

    # ***** Properties *****

    def __getter_rows(self) -> int:
        return self.cobj().rows

    def __getter_cols(self) -> int:
        return self.cobj().cols

    def __getter_nz(self) -> int:
        return self.cobj().nz

    # def __getter_row(self) -> List[int]:
    #     pass

    # def __getter_col(self) -> List[int]:
    #     pass

    def __getter_coeff(self) -> List[float]:
        return cptr_to_list(self.cobj().coeff, self.nz)

    # ***** Methods ******

    def addentry(self, row: int, col: int, x: float) -> float:
        return libsparsematrix.addentry_sparsematrix(self, row, col, x)

    def setentry(self, row: int, col: int, x: float) -> None:
        libsparsematrix.setentry_sparsematrix(self, row, col, x)

    def memsize(self) -> int:
        return libsparsematrix.getsize_sparsematrix(self)

    def sort(self) -> None:
        libsparsematrix.sort_sparsematrix(self)

    def clear(self) -> None:
        libsparsematrix.clear_sparsematrix(self)

    def print(self) -> None:
        libsparsematrix.print_sparsematrix(self)

    def print_eps(self, file: str, offset: int) -> None:
        libsparsematrix.print_eps_sparsematrix(self, file.encode(), offset)

    def norm(self) -> float:
        return libsparsematrix.norm2_sparsematrix(self)

    def norm2_diff(self, other: 'SparseMatrix') -> float:
        return libsparsematrix.norm2diff_sparsematrix(self, other)

    def delete(self) -> None:
        super().delete(libsparsematrix.del_sparsematrix)

    # -------

    def copy_sparsematrix_hmatrix(self, target: 'mat.HMatrix') -> None:
        libhmatrix.copy_sparsematrix_hmatrix(self, target)
