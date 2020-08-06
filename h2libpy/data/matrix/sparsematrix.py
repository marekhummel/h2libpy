from typing import List

import h2libpy.data.matrix as mat
import h2libpy.lib.hmatrix as libhmatrix
import h2libpy.lib.sparsematrix as libsparsematrix
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import cptr_to_list
from h2libpy.data.matrix.sparsepattern import SparsePattern


class SparseMatrix(StructWrapper, cstruct=libsparsematrix.CStructSparseMatrix):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, rows: int, cols: int, nz: int):
        return cls(libsparsematrix.new_raw_sparsematrix(rows, cols, nz))

    @classmethod
    def new_identity(cls, rows: int, cols: int):
        return cls(libsparsematrix.new_identity_sparsematrix(rows, cols))

    @classmethod
    def new_zero(cls, sp: 'SparsePattern'):
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

    def setentry(self, row: int, col: int, x: float):
        libsparsematrix.setentry_sparsematrix(self, row, col, x)

    def size(self) -> int:
        return libsparsematrix.getsize_sparsematrix(self)

    def sort(self):
        libsparsematrix.sort_sparsematrix(self)

    def clear(self):
        libsparsematrix.clear_sparsematrix(self)

    def print(self):
        libsparsematrix.print_sparsematrix(self)

    def print_eps(self, file: str, offset: int):
        libsparsematrix.print_eps_sparsematrix(self, file, offset)

    def norm(self) -> float:
        return libsparsematrix.norm2_sparsematrix(self)

    def norm2_diff(self, other: 'SparseMatrix') -> float:
        return libsparsematrix.norm2diff_sparsematrix(self, other)

    # -------

    def copy_sparsematrix_hmatrix(self, target: 'mat.HMatrix'):
        libhmatrix.copy_sparsematrix_hmatrix(self, target)
