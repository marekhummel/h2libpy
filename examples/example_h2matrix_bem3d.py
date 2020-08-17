import time

import init  # noqa
import h2libpy.solver.krylovsolvers as krylovsolvers
from h2libpy.base.util import get_address
from h2libpy.data.geometry import MacroSurface3d, Surface3d
from h2libpy.data.matrix import H2Matrix
from h2libpy.data.misc import Block, ClusterBasis
from h2libpy.data.problem.bem3d import BasisFunction, Bem3d
from h2libpy.data.vector import AVector
from h2libpy.lib.block import admissible_2_cluster
from h2libpy.lib.laplacebem3d import (eval_dirichlet_fundamental_laplacebem3d,
                                      eval_neumann_fundamental_laplacebem3d)
from h2libpy.lib.util.helper import uninit


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
    print(f'Created geometry with {gr.vertices} vertices, {gr.edges} edges and \
          {gr.triangles} triangles')

    # Set up basis data structures for H-matrix approximations
    bem_slp = Bem3d.new_slp_laplace(gr, q_reg, q_sing, basis, basis)
    bem_dlp = Bem3d.new_dlp_laplace(gr, q_reg, q_sing, basis, basis, 0.5)
    root = bem_slp.build_cluster(clf, basis)
    broot = Block.build(root, root, get_address(eta),
                        admissible_2_cluster, strict=True, lower=False)

    # Create structure for row clusterbases
    rbV = ClusterBasis.from_cluster(root)
    cbV = ClusterBasis.from_cluster(root)
    rbKM = ClusterBasis.from_cluster(root)
    cbKM = ClusterBasis.from_cluster(root)

    # Init H2-matrix approximation scheme by interpolation
    bem_dlp.setup_h2matrix_aprx_inter(rbKM, cbKM, broot, m)
    bem_slp.setup_h2matrix_aprx_inter(rbV, cbV, broot, m)

    # Assemble row clusterbasis for SLP
    print('Assemble row basis for H2-matrix V:')
    start = time.time()
    bem_slp.assemble_h2matrix_row(rbV)
    t = time.time() - start
    size = rbV.size() / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Assemble column clusterbasis for SLP
    print('Assemble column basis for H2-matrix V:')
    start = time.time()
    bem_slp.assemble_h2matrix_col(cbV)
    t = time.time() - start
    size = cbV.size() / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Assemble H-matrix SLP
    print('Assemble H2-matrix V:')
    V = H2Matrix.from_block(broot, rbV, cbV)
    start = time.time()
    bem_slp.assemble_h2matrix(V)
    t = time.time() - start
    size = V.size() / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Assemble row clusterbasis for DLP
    print('Assemble row basis for H2-matrix 0.5M + K:')
    start = time.time()
    bem_dlp.assemble_h2matrix_row(rbKM)
    t = time.time() - start
    size = rbKM.size() / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Assemble column clusterbasis for SLP
    print('Assemble column basis for H2-matrix 0.5M + K:')
    start = time.time()
    bem_dlp.assemble_h2matrix_col(cbKM)
    t = time.time() - start
    size = cbKM.size() / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Assemble H-matrix 0.5M + K
    print('Assemble H2-matrix 0.5M + K:')
    KM = H2Matrix.from_block(broot, rbKM, cbKM)
    start = time.time()
    bem_dlp.assemble_h2matrix(KM)
    t = time.time() - start
    size = KM.size() / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Create Dirichlet data
    gd = AVector.new(gr.triangles)
    print('Compute L2-projection of Dirichlet data:')
    start = time.time()
    bem_dlp.project_l2_c(eval_dirichlet_fundamental_laplacebem3d, gd, bem_dlp)
    t = time.time() - start
    size = gd.size() / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Compute right-hand-side b = (0.5M + K)*gd
    b = AVector.new(gr.triangles)
    print('Compute right-hand-side:')
    start = time.time()
    b.clear()
    b.addeval_h2matrix_avector(1.0, KM, gd)
    t = time.time() - start
    size = b.size() / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Solve linear system V x = b using CG-method.
    x = AVector.new(gr.triangles, zeros=True)
    print('Solve linear system:')
    start = time.time()
    krylovsolvers.solve_cg(V, b, x, eps_solve, maxiter)
    t = time.time() - start
    size = x.size() / 1024 / 1024
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
    uninit()
    print(f'TOTAL TIME: {time.time() - tt:.5f} s')


if __name__ == '__main__':
    main()
