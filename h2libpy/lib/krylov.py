from ctypes import CFUNCTYPE
from ctypes import POINTER as PTR
from ctypes import c_bool, c_uint, c_void_p

from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.avector import CStructAVector
from h2libpy.lib.settings import field, real
from h2libpy.lib.util.helper import get_func

# ------------------------------------


CFuncAddevalT = CFUNCTYPE(None, *[field, c_void_p, CStructAVector, CStructAVector])
CFuncPrcdT = CFUNCTYPE(None, *[c_void_p, CStructAVector])
CFuncMvmT = CFUNCTYPE(None, *[field, c_bool, c_void_p, CStructAVector, CStructAVector])


# ------------------------------------


norm2_matrix = get_func('norm2_matrix', real, [CFuncMvmT, c_void_p, c_uint, c_uint])
norm2diff_matrix = get_func('norm2diff_matrix', real, [CFuncMvmT, c_void_p, CFuncMvmT, c_void_p, c_uint, c_uint])
norm2diff_pre_matrix = get_func('norm2diff_pre_matrix', real, [CFuncMvmT, c_void_p, CFuncPrcdT, CFuncPrcdT, c_void_p, c_uint, c_uint])
norm2diff_id_pre_matrix = get_func('norm2diff_id_pre_matrix', real, [CFuncMvmT, c_void_p, CFuncPrcdT, CFuncPrcdT, c_void_p, c_uint, c_uint])
init_cg = get_func('init_cg', None, [CFuncAddevalT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector)])
step_cg = get_func('step_cg', None, [CFuncAddevalT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector)])
evalfunctional_cg = get_func('evalfunctional_cg', real, [CFuncAddevalT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector)])
init_pcg = get_func('init_pcg', None, [CFuncAddevalT, c_void_p, CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector)])
step_pcg = get_func('step_pcg', None, [CFuncAddevalT, c_void_p, CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector)])
init_uzawa = get_func('init_uzawa', None, [CFuncPrcdT, c_void_p, CFuncMvmT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector)])
step_uzawa = get_func('step_uzawa', None, [CFuncPrcdT, c_void_p, CFuncMvmT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector)])
init_puzawa = get_func('init_puzawa', None, [CFuncPrcdT, c_void_p, CFuncMvmT, c_void_p, CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector)])
step_puzawa = get_func('step_puzawa', None, [CFuncPrcdT, c_void_p, CFuncMvmT, c_void_p, CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector)])
init_bicg = get_func('init_bicg', None, [CFuncAddevalT, CFuncAddevalT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector)])
step_bicg = get_func('step_bicg', None, [CFuncAddevalT, CFuncAddevalT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector)])
init_bicgstab = get_func('init_bicgstab', None, [CFuncAddevalT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector)])
step_bicgstab = get_func('step_bicgstab', None, [CFuncAddevalT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector)])
init_gmres = get_func('init_gmres', None, [CFuncAddevalT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(c_uint), PTR(CStructAMatrix), PTR(CStructAVector)])
step_gmres = get_func('step_gmres', None, [CFuncAddevalT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(c_uint), PTR(CStructAMatrix), PTR(CStructAVector)])
finish_gmres = get_func('finish_gmres', None, [CFuncAddevalT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(c_uint), PTR(CStructAMatrix), PTR(CStructAVector)])
residualnorm_gmres = get_func('residualnorm_gmres', real, [PTR(CStructAVector), c_uint])
init_pgmres = get_func('init_pgmres', None, [CFuncAddevalT, c_void_p, CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(c_uint), PTR(CStructAMatrix), PTR(CStructAVector)])
step_pgmres = get_func('step_pgmres', None, [CFuncAddevalT, c_void_p, CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(c_uint), PTR(CStructAMatrix), PTR(CStructAVector)])
finish_pgmres = get_func('finish_pgmres', None, [CFuncAddevalT, c_void_p, CFuncPrcdT, c_void_p, PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(CStructAVector), PTR(c_uint), PTR(CStructAMatrix), PTR(CStructAVector)])
residualnorm_pgmres = get_func('residualnorm_pgmres', real, [PTR(CStructAVector), c_uint])
