import ctypes
import time


from h2libpy.lib.amatrix import (addeval_amatrix_avector, del_amatrix,
                                 getsize_amatrix, new_amatrix)
from h2libpy.lib.avector import (clear_avector, del_avector, getsize_avector,
                                 new_avector)
from h2libpy.lib.bem3d import (CFuncBoundaryFunc3d, CEnumBasisFunctionBem3d,
                               assemble_bem3d_amatrix, del_bem3d, normL2_bem3d,
                               normL2diff_c_bem3d, projectL2_bem3d_c_avector)
from h2libpy.lib.krylovsolvers import solve_cg_amatrix_avector
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
    # Basic params
    tt = time.time()
    q_reg = ctypes.c_uint(2)
    q_sing = ctypes.c_uint(q_reg.value + 2)
    basis = CEnumBasisFunctionBem3d.BASIS_CONSTANT_BEM3D
    eps_solve = ctypes.c_double(1.0E-10)
    maxiter = ctypes.c_uint(500)


    # Geometry
    mg = new_sphere_macrosurface3d()
    gr = build_from_macrosurface3d_surface3d(mg,  ctypes.c_uint(8))
    print(f'Created geometry with {gr.contents.vertices} vertices, {gr.contents.edges} edges and {gr.contents.triangles} triangles')


    # bem objects
    bem_slp = new_slp_laplace_bem3d(gr, q_reg, q_sing, basis, basis)
    bem_dlp = new_dlp_laplace_bem3d(gr, q_reg, q_sing, basis, basis, ctypes.c_double(0.5))


    # Assemble H-matrix SLP
    print('Assemble dense matrix V:')
    V = new_amatrix(gr.contents.triangles, gr.contents.triangles)

    start = time.time()
    assemble_bem3d_amatrix(bem_slp, V)
    t = time.time() - start
    size = getsize_amatrix(V) / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')


    # hmatrix 0.5I + K
    print('Assemble dense matrix 0.5M + K:')
    KM = new_amatrix(gr.contents.triangles, gr.contents.triangles)
    start = time.time()
    assemble_bem3d_amatrix(bem_dlp, KM)
    t = time.time() - start
    size = getsize_amatrix(KM) / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')


    # Dirichlet data
    gd = new_avector(gr.contents.triangles)
    print('Compute L2-projection of Dirichlet data:')
    start = time.time()
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
    addeval_amatrix_avector(ctypes.c_double(1.0), KM, gd, b)
    t = time.time() - start
    size = getsize_avector(b) / 1024 / 1024
    print(f'  {t:.2f} s')
    print(f'  {size:.3f} MB')


    # Solve linear system V x = b using CG-method.
    x = new_avector(gr.contents.triangles)
    print('Solve linear system:')
    start = time.time()
    solve_cg_amatrix_avector(V, b, x, eps_solve, maxiter)
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
    del_amatrix(V)
    del_amatrix(KM)
    del_bem3d(bem_slp)
    del_bem3d(bem_dlp)
    del_macrosurface3d(mg)
    del_surface3d(gr)
    uninit()

    print(f'TOTAL TIME: {time.time() - tt:.5f} s')


if __name__ == '__main__':
    main()
