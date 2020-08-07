from ctypes import POINTER as PTR
from ctypes import c_bool, c_char_p, c_size_t, c_uint

from h2libpy.lib.settings import field, real
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import (CStructAMatrix, CStructAVector,
                                      CStructSparseMatrix,
                                      CStructSparsePattern)

# ------------------------


CStructSparseMatrix._fields_ = [
    ('rows', c_uint),
    ('cols', c_uint),
    ('nz', c_uint),
    ('row', PTR(c_uint)),
    ('col', PTR(c_uint)),
    ('coeff', PTR(field))
]


# ------------------------


new_raw_sparsematrix = get_func('new_raw_sparsematrix', PTR(CStructSparseMatrix), [c_uint, c_uint, c_uint])
new_identity_sparsematrix = get_func('new_identity_sparsematrix', PTR(CStructSparseMatrix), [c_uint, c_uint])
new_zero_sparsematrix = get_func('new_zero_sparsematrix', PTR(CStructSparseMatrix), [PTR(CStructSparsePattern)])
del_sparsematrix = get_func('del_sparsematrix', None, [PTR(CStructSparseMatrix)])
addentry_sparsematrix = get_func('addentry_sparsematrix', field, [PTR(CStructSparseMatrix), c_uint, c_uint, field])
setentry_sparsematrix = get_func('setentry_sparsematrix', None, [PTR(CStructSparseMatrix), c_uint, c_uint, field])
getsize_sparsematrix = get_func('getsize_sparsematrix', c_size_t, [PTR(CStructSparseMatrix)])
sort_sparsematrix = get_func('sort_sparsematrix', None, [PTR(CStructSparseMatrix)])
clear_sparsematrix = get_func('clear_sparsematrix', None, [PTR(CStructSparseMatrix)])
print_sparsematrix = get_func('print_sparsematrix', None, [PTR(CStructSparseMatrix)])
print_eps_sparsematrix = get_func('print_eps_sparsematrix', None, [PTR(CStructSparseMatrix), c_char_p, c_uint])
addeval_sparsematrix_avector = get_func('addeval_sparsematrix_avector', None, [field, PTR(CStructSparseMatrix), PTR(CStructAVector), PTR(CStructAVector)])
addevaltrans_sparsematrix_avector = get_func('addevaltrans_sparsematrix_avector', None, [field, PTR(CStructSparseMatrix), PTR(CStructAVector), PTR(CStructAVector)])
mvm_sparsematrix_avector = get_func('mvm_sparsematrix_avector', None, [field, c_bool, PTR(CStructSparseMatrix), PTR(CStructAVector), PTR(CStructAVector)])
norm2_sparsematrix = get_func('norm2_sparsematrix', real, [PTR(CStructSparseMatrix)])
norm2diff_sparsematrix = get_func('norm2diff_sparsematrix', real, [PTR(CStructSparseMatrix), PTR(CStructSparseMatrix)])
add_sparsematrix_amatrix = get_func('add_sparsematrix_amatrix', None, [field, c_bool, PTR(CStructSparseMatrix), PTR(CStructAMatrix)])
