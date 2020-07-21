from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_uint, c_void_p, c_size_t

from h2libpy.lib.util.helper import get_func
from h2libpy.lib.settings import field
from h2libpy.lib.avector import CStructAVector


# ------------------------


class CStructAMatrix(Struct): pass


# ------------------------


CStructAMatrix._fields_ = [
    ('a', PTR(field)),
    ('ld', c_uint),
    ('rows', c_uint),
    ('cols', c_uint),
    ('owner', c_void_p)
]

# ------------------------

new_amatrix = get_func('new_amatrix', PTR(CStructAMatrix), [c_uint, c_uint])
getsize_amatrix = get_func('getsize_amatrix', c_size_t, [PTR(CStructAMatrix)])
addeval_amatrix_avector = get_func('addeval_amatrix_avector', None, [field, PTR(CStructAMatrix), PTR(CStructAVector), PTR(CStructAVector)])
del_amatrix = get_func('del_amatrix', None, [PTR(CStructAMatrix)])
