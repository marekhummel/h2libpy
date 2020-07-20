from ctypes import POINTER as PTR
from ctypes import c_uint, c_void_p

from h2libpy.util.helper import get_func
from h2libpy.util.lib.bem3d import LibBasisFunctionBem3d, LibBem3d
from h2libpy.util.lib.settings import field, real
from h2libpy.util.lib.surface3d import LibSurface3d

# ------------------------


new_slp_laplace_bem3d = get_func('new_slp_laplace_bem3d', PTR(LibBem3d), [PTR(LibSurface3d), c_uint, c_uint, LibBasisFunctionBem3d, LibBasisFunctionBem3d])
new_dlp_laplace_bem3d = get_func('new_dlp_laplace_bem3d', PTR(LibBem3d), [PTR(LibSurface3d), c_uint, c_uint, LibBasisFunctionBem3d, LibBasisFunctionBem3d, field])
eval_dirichlet_fundamental_laplacebem3d = get_func('eval_dirichlet_fundamental_laplacebem3d', field, [PTR(real), PTR(real), c_void_p])
eval_neumann_fundamental_laplacebem3d = get_func('eval_neumann_fundamental_laplacebem3d', field, [PTR(real), PTR(real), c_void_p])
