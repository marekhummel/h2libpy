import time

import init  # noqa
import h2libpy.solver.krylovsolvers as krylovsolvers
from h2libpy.base.util import get_address
from h2libpy.data.geometry import MacroSurface3d, Surface3d
from h2libpy.data.matrix import HMatrix
from h2libpy.data.misc import Block
from h2libpy.data.problem.bem3d import BasisFunction, Bem3d
from h2libpy.data.problem.bem3d import InterpolationDirection as IntDir
from h2libpy.data.vector import AVector
from h2libpy.lib.block import admissible_2_cluster
from h2libpy.lib.laplacebem3d import (eval_dirichlet_fundamental_laplacebem3d,
                                      eval_neumann_fundamental_laplacebem3d)
from h2libpy.lib.util.helper import uninit

# def eval_dirichlet_fundamental(xs, ns, data):
#     from math import sqrt
#     from h2libpy.base.util import cptr_to_list
#     d = [xi - 1.2 for xi in cptr_to_list(xs, 3)]
#     kernel = sum(di * di for di in d)
#     return 1 / sqrt(kernel)


def main():
    # Basic params
    tt = time.time()

    # Set up basic parameters
    q_reg = 2
    q_sing = q_reg + 2
    basis = BasisFunction.Constant
    m = 4
    clf = 2 * m * m * m
    eta = 1.4
    eps_solve = 1.0e-10
    maxiter = 500

    # Create geometry
    mg = MacroSurface3d.new_sphere()
    gr = Surface3d.from_macrosurface3d(mg, 8)
    print(f'Created geometry with {gr.vertices} vertices, {gr.edges} edges and'
          f' {gr.triangles} triangles')

    # Set up basis data structures for H-matrix approximations
    bem_slp = Bem3d.new_slp_laplace(gr, q_reg, q_sing, basis, basis)
    bem_dlp = Bem3d.new_dlp_laplace(gr, q_reg, q_sing, basis, basis, 0.5)
    root = bem_slp.build_cluster(clf, basis)
    broot = Block.build(root, root, get_address(eta),
                        admissible_2_cluster, strict=False, lower=False)
    bem_slp.setup_hmatrix_aprx_inter(IntDir.Row, root, root, broot, m)
    bem_dlp.setup_hmatrix_aprx_inter(IntDir.Row, root, root, broot, m)

    # Assemble H-matrix SLP
    print('Assemble H-matrix V:')
    V = HMatrix.from_block(broot, m * m * m)

    start = time.time()
    bem_slp.assemble_hmatrix(broot, V)
    t = time.time() - start
    size = V.memsize() / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Assemble H-matrix 0.5I + K
    print('Assemble H-matrix 0.5M + K:')
    KM = HMatrix.from_block(broot, m * m * m)
    start = time.time()
    bem_dlp.assemble_hmatrix(broot, KM)
    t = time.time() - start
    size = KM.memsize() / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Create Dirichlet data
    gd = AVector.new(gr.triangles)
    print('Compute L2-projection of Dirichlet data:')
    start = time.time()
    bem_dlp.project_l2_c(eval_dirichlet_fundamental_laplacebem3d, gd, bem_dlp)
    t = time.time() - start
    size = gd.memsize() / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Compute right-hand-side b = (0.5M + K)*gd
    b = AVector.new(gr.triangles)
    print('Compute right-hand-side:')
    start = time.time()
    b.clear()
    b.addeval_hmatrix_avector(1.0, KM, gd)
    t = time.time() - start
    size = b.memsize() / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Solve linear system V x = b using CG-method.
    x = AVector.new(gr.triangles, zeros=True)
    print('Solve linear system:')
    start = time.time()
    krylovsolvers.solve_cg(V, b, x, eps_solve, maxiter)
    t = time.time() - start
    size = x.memsize() / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Compute L2-error compared to analytical solution of the Neumann data.
    print('Compute L2-error against analytical solution of the Neumann data:')
    start = time.time()
    norm = bem_slp.norm_l2_diff_c(x, eval_neumann_fundamental_laplacebem3d,
                                  None)
    t = time.time() - start
    print('Abs. L2-error:')
    print(f'  {t:.2f} s')
    print(f'  {norm:.5e}')

    start = time.time()
    norm /= bem_slp.norm_l2(eval_neumann_fundamental_laplacebem3d, None)
    t = time.time() - start
    print('Rel. L2-error:')
    print(f'  {t:.2f} s')
    print(f'  {norm:.5e}')

    # cleanup
    x.delete()
    b.delete()
    gd.delete()
    V.delete()
    KM.delete()
    broot.delete()
    root.delete()
    bem_slp.delete()
    bem_dlp.delete()
    mg.delete()
    gr.delete()
    uninit()
    print(f'TOTAL TIME: {time.time() - tt:.5f} s')


if __name__ == '__main__':
    main()
