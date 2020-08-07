import h2libpy.lib.krylovsolvers as libkrylovsolvers
import h2libpy.lib.krylov as libkrylov
import h2libpy.data.matrix as mat
import h2libpy.data.vector as vec
from h2libpy.base.util import verify_type
from typing import Union
from ctypes import cast, c_void_p


matrix_types = [mat.AMatrix, mat.SparseMatrix, mat.HMatrix, mat.H2Matrix,
                mat.DH2Matrix]
matrix_union = Union['mat.AMatrix', 'mat.SparseMatrix', 'mat.HMatrix',
                     'mat.H2Matrix', 'mat.DH2Matrix']


def solve_cg_avector(a, addeval, b: 'vec.AVector', x: 'vec.AVector',
                     eps: float, maxiter: int) -> int:
    ca = cast(a, c_void_p)
    caddeval = libkrylov.CFuncAddevalT(addeval)
    libkrylovsolvers.solve_cg_avector(ca, caddeval, b, x, eps, maxiter)


def solve_cg(a: matrix_union, b: 'vec.AVector', x: 'vec.AVector',
             eps: float, maxiter: int) -> int:
    verify_type(a, matrix_types)

    if isinstance(a, mat.AMatrix):
        solve_func = libkrylovsolvers.solve_cg_amatrix_avector
    elif isinstance(a, mat.SparseMatrix):
        solve_func = libkrylovsolvers.solve_cg_sparsematrix_avector
    elif isinstance(a, mat.HMatrix):
        solve_func = libkrylovsolvers.solve_cg_hmatrix_avector
    elif isinstance(a, mat.H2Matrix):
        solve_func = libkrylovsolvers.solve_cg_h2matrix_avector
    elif isinstance(a, mat.DH2Matrix):
        solve_func = libkrylovsolvers.solve_cg_dh2matrix_avector
    return solve_func(a, b, x, eps, maxiter)


def solve_pcg_avector(a, addeval, prcd, pdata, b: 'vec.AVector',
                      x: 'vec.AVector', eps: float, maxiter: int) -> int:
    ca = cast(a, c_void_p)
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cprcd = libkrylov.CFuncPrcdT(prcd)
    cpdata = cast(pdata, c_void_p)
    libkrylovsolvers.solve_pcg_avector(ca, caddeval, cprcd, cpdata, b, x, eps,
                                       maxiter)


def solve_pcg(a: matrix_union, prcd, pdata, b: 'vec.AVector', x: 'vec.AVector',
              eps: float, maxiter: int) -> int:
    verify_type(a, matrix_types)
    cprcd = libkrylov.CFuncPrcdT(prcd)
    cpdata = cast(pdata, c_void_p)

    if isinstance(a, mat.AMatrix):
        solve_func = libkrylovsolvers.solve_pcg_amatrix_avector
    elif isinstance(a, mat.SparseMatrix):
        solve_func = libkrylovsolvers.solve_pcg_sparsematrix_avector
    elif isinstance(a, mat.HMatrix):
        solve_func = libkrylovsolvers.solve_pcg_hmatrix_avector
    elif isinstance(a, mat.H2Matrix):
        solve_func = libkrylovsolvers.solve_pcg_h2matrix_avector
    elif isinstance(a, mat.DH2Matrix):
        solve_func = libkrylovsolvers.solve_pcg_dh2matrix_avector
    return solve_func(a, cprcd, cpdata, b, x, eps, maxiter)


def solve_gmres_avector(a, addeval, b: 'vec.AVector', x: 'vec.AVector',
                        eps: float, maxiter: int, kmax: int) -> int:
    ca = cast(a, c_void_p)
    caddeval = libkrylov.CFuncAddevalT(addeval)
    libkrylovsolvers.solve_gmres_avector(ca, caddeval, b, x, eps, maxiter,
                                         kmax)


def solve_gmres(a: matrix_union, b: 'vec.AVector', x: 'vec.AVector',
                eps: float, maxiter: int, kmax: int) -> int:
    verify_type(a, matrix_types)

    if isinstance(a, mat.AMatrix):
        solve_func = libkrylovsolvers.solve_gmres_amatrix_avector
    elif isinstance(a, mat.SparseMatrix):
        solve_func = libkrylovsolvers.solve_gmres_sparsematrix_avector
    elif isinstance(a, mat.HMatrix):
        solve_func = libkrylovsolvers.solve_gmres_hmatrix_avector
    elif isinstance(a, mat.H2Matrix):
        solve_func = libkrylovsolvers.solve_gmres_h2matrix_avector
    elif isinstance(a, mat.DH2Matrix):
        solve_func = libkrylovsolvers.solve_gmres_dh2matrix_avector
    return solve_func(a, b, x, eps, maxiter, kmax)


def solve_pgmres_avector(a, addeval, prcd, pdata, b: 'vec.AVector',
                         x: 'vec.AVector', eps: float, maxiter: int,
                         kmax: int) -> int:
    ca = cast(a, c_void_p)
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cprcd = libkrylov.CFuncPrcdT(prcd)
    cpdata = cast(pdata, c_void_p)
    libkrylovsolvers.solve_pgmres_avector(ca, caddeval, cprcd, cpdata, b, x,
                                          eps, maxiter, kmax)


def solve_pgmres(a: matrix_union, prcd, pdata, b: 'vec.AVector',
                 x: 'vec.AVector', eps: float, maxiter: int, kmax: int) -> int:
    verify_type(a, matrix_types)
    cprcd = libkrylov.CFuncPrcdT(prcd)
    cpdata = cast(pdata, c_void_p)

    if isinstance(a, mat.AMatrix):
        solve_func = libkrylovsolvers.solve_pgmres_amatrix_avector
    elif isinstance(a, mat.SparseMatrix):
        solve_func = libkrylovsolvers.solve_pgmres_sparsematrix_avector
    elif isinstance(a, mat.HMatrix):
        solve_func = libkrylovsolvers.solve_pgmres_hmatrix_avector
    elif isinstance(a, mat.H2Matrix):
        solve_func = libkrylovsolvers.solve_pgmres_h2matrix_avector
    elif isinstance(a, mat.DH2Matrix):
        solve_func = libkrylovsolvers.solve_pgmres_dh2matrix_avector
    return solve_func(a, cprcd, cpdata, b, x, eps, maxiter, kmax)
