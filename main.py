from h2libpy.data.geometry.macrosurface3d import MacroSurface3d
from h2libpy.data.geometry.surface3d import Surface3d
from h2libpy.data.problem.bem3d.bem3d import Bem3d
from h2libpy.lib.bem3d import CEnumBasisFunctionBem3d
# from h2libpy.data.vector.avector import AVector


q_reg = 2
q_sing = q_reg + 2
basis = CEnumBasisFunctionBem3d.BASIS_CONSTANT_BEM3D
eps_solve = 1.0e-10
maxiter = 500

mg = MacroSurface3d.new_sphere()
gr = Surface3d.from_macrosurface3d(mg, 32)

# print('vert', gr.vertices)
# print('edges', gr.edges)
# print('tri', gr.triangles)
# print('x', gr.x[:10])
# print('e', gr.e[:10])
# print('t', gr.t[:10])
# print('s', gr.s[:10])
# print('n', gr.n[:10])
# print('g', gr.g)
# print('hmin', gr.hmin)
# print('hmax', gr.hmax)

bem_slp = Bem3d.new_slp_laplace(gr, q_reg, q_sing, basis, basis)
bem_dlp = Bem3d.new_dlp_laplace(gr, q_reg, q_sing, basis, basis, 0.5)


print(bem_slp.gr.vertices)
print(bem_slp.sq.base_id)
print(bem_slp.sq.n_id)
print(bem_slp.sq.base_edge)
print(bem_slp.sq.n_edge)
print(bem_slp.sq.base_vert)
print(bem_slp.sq.n_vert)
print(bem_slp.sq.base_dist)
print(bem_slp.sq.n_dist)
print(bem_slp.sq.base_single)
print(bem_slp.sq.n_single)
print(bem_slp.sq.q)
print(bem_slp.sq.nmax)
print(bem_slp.alpha)
print(bem_slp.k)
print(bem_slp.kernel_const)
print(bem_slp.aprx.m_inter)
print(bem_slp.aprx.k_inter)
print(bem_slp.aprx.l_green)
print(bem_slp.aprx.m_green)
print(bem_slp.aprx.delta_green)
print(bem_slp.aprx.grc_green)
print(bem_slp.aprx.gcc_green)
print(bem_slp.aprx.grb_green)
print(bem_slp.aprx.gcb_green)
print(bem_slp.aprx.accur_aca)
print(bem_slp.aprx.recomp)
print(bem_slp.aprx.accur_recomp)
print(bem_slp.aprx.coarsen)
print(bem_slp.aprx.accur_coarsen)
print(bem_slp.aprx.hiercomp)
print(bem_slp.aprx.accur_hiercomp)
print(bem_slp.aprx.tm.frobenius)
print(bem_slp.aprx.tm.absolute)
print(bem_slp.aprx.tm.blocks)
print(bem_slp.aprx.tm.zeta_level)
print(bem_slp.aprx.tm.age)
print(bem_slp.par.grcnn)
print(bem_slp.par.gccnn)
print(bem_slp.par.grbnn)
print(bem_slp.par.gcbnn)
print(bem_slp.kernels)
