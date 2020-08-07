from ctypes import POINTER as PTR
from ctypes import c_uint

from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import CStructPatEntry, CStructSparsePattern

# ------------------------


CStructSparsePattern._fields_ = [
    ('rows', c_uint),
    ('cols', c_uint),
    ('row', PTR(PTR(CStructPatEntry))),
]

CStructPatEntry._fields_ = [
    ('row', c_uint),
    ('col', c_uint),
    ('next', PTR(CStructPatEntry))
]


# ------------------------


new_sparsepattern = get_func('new_sparsepattern', PTR(CStructSparsePattern), [c_uint, c_uint])
del_sparsepattern = get_func('del_sparsepattern', None, [PTR(CStructSparsePattern)])
clear_sparsepattern = get_func('clear_sparsepattern', None, [PTR(CStructSparsePattern)])
addnz_sparsepattern = get_func('addnz_sparsepattern', None, [PTR(CStructSparsePattern), c_uint, c_uint])
print_sparsepattern = get_func('print_sparsepattern', None, [PTR(CStructSparsePattern)])
