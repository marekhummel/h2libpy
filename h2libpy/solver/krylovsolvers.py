import h2libpy.lib.krylovsolvers as libkrylovsolvers
from h2libpy.data.matrix.amatrix import AMatrix
from h2libpy.data.vector.avector import AVector


def solve_cg_amatrix_avector(a: 'AMatrix', b: 'AVector', x: 'AVector',
                             eps: float, maxiter: int) -> int:
    return libkrylovsolvers.solve_cg_amatrix_avector(a, b, x, eps, maxiter)
