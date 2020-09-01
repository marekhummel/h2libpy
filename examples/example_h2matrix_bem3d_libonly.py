import ctypes
import time

import init  # noqa
from h2libpy.base.util import get_address
from h2libpy.lib.avector import (clear_avector, del_avector, getsize_avector,
                                 new_avector)
from h2libpy.lib.bem3d import (CEnumBasisFunctionBem3d, CFuncBoundaryFunc3d,
                               assemble_bem3d_h2matrix,
                               assemble_bem3d_h2matrix_col_clusterbasis,
                               assemble_bem3d_h2matrix_row_clusterbasis,
                               build_bem3d_cluster, del_bem3d, normL2_bem3d,
                               normL2diff_c_bem3d, projectL2_bem3d_c_avector,
                               setup_h2matrix_aprx_inter_bem3d)
from h2libpy.lib.block import (CFuncAdmissible, admissible_2_cluster,
                               build_strict_block, del_block)
from h2libpy.lib.cluster import del_cluster
from h2libpy.lib.clusterbasis import (build_from_cluster_clusterbasis,
                                      getsize_clusterbasis)
from h2libpy.lib.h2matrix import (addeval_h2matrix_avector,
                                  build_from_block_h2matrix, del_h2matrix,
                                  getsize_h2matrix)
from h2libpy.lib.krylovsolvers import solve_cg_h2matrix_avector
from h2libpy.lib.laplacebem3d import (eval_dirichlet_fundamental_laplacebem3d,
                                      eval_neumann_fundamental_laplacebem3d,
                                      new_dlp_laplace_bem3d,
                                      new_slp_laplace_bem3d)
from h2libpy.lib.macrosurface3d import (build_from_macrosurface3d_surface3d,
                                        del_macrosurface3d,
                                        new_sphere_macrosurface3d)
from h2libpy.lib.surface3d import del_surface3d
from h2libpy.lib.util.helper import uninit


def main():
    # Set up basic parameters
    tt = time.time()
    q_reg = 2
    q_sing = q_reg + 2
    basis = CEnumBasisFunctionBem3d.BASIS_CONSTANT_BEM3D
    m = 4
    clf = 2 * m * m * m
    eta = 1.4
    eps_solve = 1.0e-10
    maxiter = 500

    # Create geometry
    mg = new_sphere_macrosurface3d()
    gr = build_from_macrosurface3d_surface3d(mg, 8)
    print(f'Created geometry with {gr.contents.vertices} vertices, {gr.contents.vertices} edges and {gr.contents.vertices} triangles')

    # Set up basis data structures for H2-matrix approximations
    bem_slp = new_slp_laplace_bem3d(gr, q_reg, q_sing, basis, basis)

    # Create a new BEM-object, that can compute entries of DLP operator and 0.5*I.
    bem_dlp = new_dlp_laplace_bem3d(gr, q_reg, q_sing, basis, basis, 0.5)
    root = build_bem3d_cluster(bem_slp, clf, basis)
    broot = build_strict_block(root, root, get_address(eta), CFuncAdmissible(admissible_2_cluster))

    # Create structure for row clusterbases
    rbV = build_from_cluster_clusterbasis(root)
    cbV = build_from_cluster_clusterbasis(root)
    rbKM = build_from_cluster_clusterbasis(root)
    cbKM = build_from_cluster_clusterbasis(root)

    # Init H2-matrix approximation scheme by interpolation
    setup_h2matrix_aprx_inter_bem3d(bem_dlp, rbKM, cbKM, broot, m)
    setup_h2matrix_aprx_inter_bem3d(bem_slp, rbV, cbV, broot, m)

    # Assemble row clusterbasis for SLP
    print('Assemble row basis for H2-matrix V:')
    start = time.time()
    assemble_bem3d_h2matrix_row_clusterbasis(bem_slp, rbV)
    t = time.time() - start
    size = getsize_clusterbasis(rbV) / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Assemble column clusterbasis for SLP
    print('Assemble column basis for H2-matrix V:')
    start = time.time()
    assemble_bem3d_h2matrix_col_clusterbasis(bem_slp, cbV)
    t = time.time() - start
    size = getsize_clusterbasis(cbV) / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Assemble H-matrix SLP
    print('Assemble H2-matrix V:')
    V = build_from_block_h2matrix(broot, rbV, cbV)
    start = time.time()
    assemble_bem3d_h2matrix(bem_slp, V)
    t = time.time() - start
    size = getsize_h2matrix(V) / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Assemble row clusterbasis for DLP
    print('Assemble row basis for H2-matrix 0.5M + K:')
    start = time.time()
    assemble_bem3d_h2matrix_row_clusterbasis(bem_dlp, rbKM)
    t = time.time() - start
    size = getsize_clusterbasis(rbKM) / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Assemble column clusterbasis for DLP
    print('Assemble column basis for H2-matrix 0.5M + K:')
    start = time.time()
    assemble_bem3d_h2matrix_col_clusterbasis(bem_dlp, cbKM)
    t = time.time() - start
    size = getsize_clusterbasis(cbKM) / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Assemble H-matrix 0.5I + K
    print('Assemble H2-matrix 0.5M + K:')
    KM = build_from_block_h2matrix(broot, rbKM, cbKM)
    start = time.time()
    assemble_bem3d_h2matrix(bem_dlp, KM)
    t = time.time() - start
    size = getsize_h2matrix(KM) / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Create Dirichlet data
    gd = new_avector(gr.contents.triangles)
    print('Compute L2-projection of Dirichlet data:')
    start = time.time()

    # L2-projection onto the space of piecewise constant function on the boundary.
    projectL2_bem3d_c_avector(bem_dlp, CFuncBoundaryFunc3d(eval_dirichlet_fundamental_laplacebem3d), gd, ctypes.cast(bem_dlp, ctypes.c_void_p))
    t = time.time() - start
    size = getsize_avector(gd) / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Compute right-hand-side b = (0.5M + K)*gd
    b = new_avector(gr.contents.triangles)
    print('Compute right-hand-side:')
    start = time.time()
    clear_avector(b)
    addeval_h2matrix_avector(1.0, KM, gd, b)
    t = time.time() - start
    size = getsize_avector(b) / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Solve linear system V x = b using CG-method.
    x = new_avector(gr.contents.triangles)
    print('Solve linear system:')
    start = time.time()
    solve_cg_h2matrix_avector(V, b, x, eps_solve, maxiter)
    t = time.time() - start
    size = getsize_avector(x) / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')

    # Compute L2-error compared to analytical solution of the Neumann data.
    print('Compute L2-error against analytical solution of the Neumann data:')
    start = time.time()
    norm = normL2diff_c_bem3d(bem_slp, x, CFuncBoundaryFunc3d(eval_neumann_fundamental_laplacebem3d), None)
    t = time.time() - start
    print('Abs. L2-error:')
    print(f'  {t:.2f} s')
    print(f'  {norm:.5e}')
    print('Rel. L2-error:')
    start = time.time()
    norm /= normL2_bem3d(bem_slp, CFuncBoundaryFunc3d(eval_neumann_fundamental_laplacebem3d), None)
    t = time.time() - start
    print(f'  {t:.2f} s')
    print(f'  {norm:.5e}')

    # cleanup
    del_avector(x)
    del_avector(b)
    del_avector(gd)
    del_h2matrix(V)
    del_h2matrix(KM)
    del_block(broot)
    del_cluster(root)
    del_bem3d(bem_slp)
    del_bem3d(bem_dlp)
    del_macrosurface3d(mg)
    del_surface3d(gr)

    uninit()
    t = time.time() - tt
    print(f'TOTAL TIME:  {t:.5f} s')


if __name__ == '__main__':
    main()
