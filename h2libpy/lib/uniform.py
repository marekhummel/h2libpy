from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_bool, c_size_t

from h2libpy.lib.settings import field
from h2libpy.lib.util.helper import get_func

# ------------------------


class CStructUniform(Struct): pass


# ------------------------


from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.avector import CStructAVector
from h2libpy.lib.clusterbasis import CStructClusterBasis
from h2libpy.lib.clusteroperator import CStructClusterOperator
from h2libpy.lib.rkmatrix import CStructRkMatrix


CStructUniform._fields_ = [
    ('rb', PTR(CStructClusterBasis)),
    ('cb', PTR(CStructClusterBasis)),
    ('S', CStructAMatrix),
    ('rnext', PTR(CStructUniform)),
    ('rprev', PTR(CStructUniform)),
    ('cnext', PTR(CStructUniform)),
    ('cprev', PTR(CStructUniform)),
]


# ------------------------

new_uniform = get_func('new_uniform', PTR(CStructUniform), [PTR(CStructClusterBasis), PTR(CStructClusterBasis)])
del_uniform = get_func('new_uniform', None, [PTR(CStructUniform)])
ref_row_uniform = get_func('ref_row_uniform', None, [PTR(CStructUniform), PTR(CStructClusterBasis)])
ref_col_uniform = get_func('ref_col_uniform', None, [PTR(CStructUniform), PTR(CStructClusterBasis)])
unref_row_uniform = get_func('unref_row_uniform', None, [PTR(CStructUniform)])
unref_col_uniform = get_func('unref_col_uniform', None, [PTR(CStructUniform)])
getsize_uniform = get_func('getsize_uniform', c_size_t, [PTR(CStructUniform)])
clear_uniform = get_func('clear_uniform', None, [PTR(CStructUniform)])
copy_uniform = get_func('copy_uniform', None, [c_bool, PTR(CStructUniform), PTR(CStructUniform)])
clone_uniform = get_func('clone_uniform', PTR(CStructUniform), [PTR(CStructUniform)])
scale_uniform = get_func('scale_uniform', None, [field, PTR(CStructUniform)])
random_uniform = get_func('random_uniform', None, [PTR(CStructUniform)])
mvm_uniform_avector = get_func('mvm_uniform_avector', None, [field, c_bool, PTR(CStructUniform), PTR(CStructAVector), PTR(CStructAVector)])
add_projected_uniform = get_func('add_projected_uniform', None, [PTR(CStructUniform), PTR(CStructClusterOperator), PTR(CStructClusterOperator), PTR(CStructUniform)])
project_inplace_uniform = get_func('project_inplace_uniform', None, [PTR(CStructUniform), PTR(CStructClusterBasis), PTR(CStructClusterOperator), PTR(CStructClusterBasis), PTR(CStructClusterOperator)])
add_rkmatrix_uniform = get_func('add_rkmatrix_uniform', None, [PTR(CStructRkMatrix), PTR(CStructUniform)])
