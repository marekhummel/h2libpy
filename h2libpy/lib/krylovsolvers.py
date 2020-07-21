from ctypes import POINTER as PTR
from ctypes import c_uint

from h2libpy.lib.util.helper import get_func
from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.avector import CStructAVector
from h2libpy.lib.settings import real

# ------------------------


solve_cg_amatrix_avector = get_func('solve_cg_amatrix_avector', c_uint, [PTR(CStructAMatrix), PTR(CStructAVector), PTR(CStructAVector), real, c_uint])
