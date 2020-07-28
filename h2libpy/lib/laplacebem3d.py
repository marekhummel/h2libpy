from ctypes import POINTER as PTR
from ctypes import c_uint, c_void_p

from h2libpy.lib.util.helper import get_func
from h2libpy.lib.bem3d import CEnumBasisFunctionBem3d, CStructBem3d
from h2libpy.lib.settings import field, real
from h2libpy.lib.surface3d import CStructSurface3d

# ------------------------


new_slp_laplace_bem3d = get_func('new_slp_laplace_bem3d', PTR(CStructBem3d), [PTR(CStructSurface3d), c_uint, c_uint, CEnumBasisFunctionBem3d, CEnumBasisFunctionBem3d])
new_dlp_laplace_bem3d = get_func('new_dlp_laplace_bem3d', PTR(CStructBem3d), [PTR(CStructSurface3d), c_uint, c_uint, CEnumBasisFunctionBem3d, CEnumBasisFunctionBem3d, field])
new_adlp_laplace_bem3d = get_func('new_adlp_laplace_bem3d', PTR(CStructBem3d), [PTR(CStructSurface3d), c_uint, c_uint, CEnumBasisFunctionBem3d, CEnumBasisFunctionBem3d, field])
del_laplace_bem3d = get_func('del_laplace_bem3d', None, [PTR(CStructBem3d)])
eval_dirichlet_linear_laplacebem3d = get_func('eval_dirichlet_linear_laplacebem3d', field, [PTR(real), PTR(real), c_void_p])
eval_neumann_linear_laplacebem3d = get_func('eval_neumann_linear_laplacebem3d', field, [PTR(real), PTR(real), c_void_p])
eval_dirichlet_quadratic_laplacebem3d = get_func('eval_dirichlet_quadratic_laplacebem3d', field, [PTR(real), PTR(real), c_void_p])
eval_neumann_quadratic_laplacebem3d = get_func('eval_neumann_quadratic_laplacebem3d', field, [PTR(real), PTR(real), c_void_p])
eval_dirichlet_fundamental_laplacebem3d = get_func('eval_dirichlet_fundamental_laplacebem3d', field, [PTR(real), PTR(real), c_void_p])
eval_neumann_fundamental_laplacebem3d = get_func('eval_neumann_fundamental_laplacebem3d', field, [PTR(real), PTR(real), c_void_p])
eval_dirichlet_fundamental2_laplacebem3d = get_func('eval_dirichlet_fundamental2_laplacebem3d', field, [PTR(real), PTR(real), c_void_p])
eval_neumann_fundamental2_laplacebem3d = get_func('eval_neumann_fundamental2_laplacebem3d', field, [PTR(real), PTR(real), c_void_p])
