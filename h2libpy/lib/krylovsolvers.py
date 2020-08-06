from ctypes import POINTER as PTR
from ctypes import c_uint, c_void_p

from h2libpy.lib.krylov import CFuncAddevalT, CFuncPrcdT
from h2libpy.lib.settings import real
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import (CStructAMatrix, CStructAVector,
                                      CStructDH2Matrix, CStructH2Matrix,
                                      CStructHMatrix, CStructSparseMatrix)

# ------------------------


solve_cg_avector = get_func('solve_cg_avector', c_uint, [c_void_p, CFuncAddevalT, PTR(CStructAVector), PTR(CStructAVector), real, c_uint])
solve_cg_amatrix_avector = get_func('solve_cg_amatrix_avector', c_uint, [PTR(CStructAMatrix), PTR(CStructAVector), PTR(CStructAVector), real, c_uint])
solve_cg_sparsematrix_avector = get_func('solve_cg_sparsematrix_avector', c_uint, [PTR(CStructSparseMatrix), PTR(CStructAVector), PTR(CStructAVector), real, c_uint])
solve_cg_hmatrix_avector = get_func('solve_cg_hmatrix_avector', c_uint, [PTR(CStructHMatrix), PTR(CStructAVector), PTR(CStructAVector), real, c_uint])
solve_cg_h2matrix_avector = get_func('solve_cg_h2matrix_avector', c_uint, [PTR(CStructH2Matrix), PTR(CStructAVector), PTR(CStructAVector), real, c_uint])
solve_cg_dh2matrix_avector = get_func('solve_cg_dh2matrix_avector', c_uint, [PTR(CStructDH2Matrix), PTR(CStructAVector), PTR(CStructAVector), real, c_uint])

solve_pcg_avector = get_func('solve_pcg_avector', c_uint, [c_void_p, CFuncAddevalT, CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), real, c_uint])
solve_pcg_amatrix_avector = get_func('solve_pcg_amatrix_avector', c_uint, [PTR(CStructAMatrix), CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), real, c_uint])
solve_pcg_sparsematrix_avector = get_func('solve_pcg_sparsematrix_avector', c_uint, [PTR(CStructSparseMatrix), CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), real, c_uint])
solve_pcg_hmatrix_avector = get_func('solve_pcg_hmatrix_avector', c_uint, [PTR(CStructHMatrix), CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), real, c_uint])
solve_pcg_h2matrix_avector = get_func('solve_pcg_h2matrix_avector', c_uint, [PTR(CStructH2Matrix), CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), real, c_uint])
solve_pcg_dh2matrix_avector = get_func('solve_pcg_dh2matrix_avector', c_uint, [PTR(CStructDH2Matrix), CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), real, c_uint])

solve_gmres_avector = get_func('solve_gmres_avector', c_uint, [c_void_p, CFuncAddevalT, PTR(CStructAVector), PTR(CStructAVector), real, c_uint, c_uint])
solve_gmres_amatrix_avector = get_func('solve_gmres_amatrix_avector', c_uint, [PTR(CStructAMatrix), PTR(CStructAVector), PTR(CStructAVector), real, c_uint, c_uint])
solve_gmres_sparsematrix_avector = get_func('solve_gmres_sparsematrix_avector', c_uint, [PTR(CStructSparseMatrix), PTR(CStructAVector), PTR(CStructAVector), real, c_uint, c_uint])
solve_gmres_hmatrix_avector = get_func('solve_gmres_hmatrix_avector', c_uint, [PTR(CStructHMatrix), PTR(CStructAVector), PTR(CStructAVector), real, c_uint, c_uint])
solve_gmres_h2matrix_avector = get_func('solve_gmres_h2matrix_avector', c_uint, [PTR(CStructH2Matrix), PTR(CStructAVector), PTR(CStructAVector), real, c_uint, c_uint])
solve_gmres_dh2matrix_avector = get_func('solve_gmres_dh2matrix_avector', c_uint, [PTR(CStructDH2Matrix), PTR(CStructAVector), PTR(CStructAVector), real, c_uint, c_uint])

solve_pgmres_avector = get_func('solve_pgmres_avector', c_uint, [c_void_p, CFuncAddevalT, CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), real, c_uint, c_uint])
solve_pgmres_amatrix_avector = get_func('solve_pgmres_amatrix_avector', c_uint, [PTR(CStructAMatrix), CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), real, c_uint, c_uint])
solve_pgmres_sparsematrix_avector = get_func('solve_pgmres_sparsematrix_avector', c_uint, [PTR(CStructSparseMatrix), CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), real, c_uint, c_uint])
solve_pgmres_hmatrix_avector = get_func('solve_pgmres_hmatrix_avector', c_uint, [PTR(CStructHMatrix), CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), real, c_uint, c_uint])
solve_pgmres_h2matrix_avector = get_func('solve_pgmres_h2matrix_avector', c_uint, [PTR(CStructH2Matrix), CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), real, c_uint, c_uint])
solve_pgmres_dh2matrix_avector = get_func('solve_pgmres_dh2matrix_avector', c_uint, [PTR(CStructDH2Matrix), CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), real, c_uint, c_uint])
