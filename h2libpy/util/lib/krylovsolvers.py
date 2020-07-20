from ctypes import POINTER as PTR
from ctypes import c_uint

from h2libpy.util.helper import get_func
from h2libpy.util.lib.amatrix import LibAMatrix
from h2libpy.util.lib.avector import LibAVector
from h2libpy.util.lib.settings import real

# ------------------------


solve_cg_amatrix_avector = get_func('solve_cg_amatrix_avector', c_uint, [PTR(LibAMatrix), PTR(LibAVector), PTR(LibAVector), real, c_uint])
