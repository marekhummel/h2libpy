from ctypes import POINTER as PTR
from ctypes import c_size_t, c_uint

from h2libpy.lib.settings import field, real
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import (CStructAMatrix, CStructAVector,
                                      CStructDClusterBasis,
                                      CStructDClusterOperator, CStructDUniform)

# ------------------------


CStructDUniform._fields_ = [
    ('rb', PTR(CStructDClusterBasis)),
    ('cb', PTR(CStructDClusterBasis)),
    ('rd', c_uint),
    ('cd', c_uint),
    ('S', CStructAMatrix),
]


# ------------------------


new_duniform = get_func('new_duniform', PTR(CStructDUniform), [PTR(CStructDClusterBasis), c_uint, PTR(CStructDClusterBasis), c_uint])
del_duniform = get_func('del_duniform', None, [PTR(CStructDUniform)])
getsize_duniform = get_func('getsize_duniform', c_size_t, [PTR(CStructDUniform)])
clear_duniform = get_func('clear_duniform', None, [PTR(CStructDUniform)])
copy_duniform = get_func('copy_duniform', None, [PTR(CStructDUniform), PTR(CStructDUniform)])
fastaddeval_duniform_avector = get_func('fastaddeval_duniform_avector', None, [field, PTR(CStructDUniform), PTR(CStructAVector), PTR(CStructAVector)])
fastaddevaltrans_duniform_avector = get_func('fastaddevaltrans_duniform_avector', None, [field, PTR(CStructDUniform), PTR(CStructAVector), PTR(CStructAVector)])
slowaddeval_duniform_avector = get_func('slowaddeval_duniform_avector', None, [field, PTR(CStructDUniform), PTR(CStructAVector), PTR(CStructAVector)])
slowaddevaltrans_duniform_avector = get_func('slowaddevaltrans_duniform_avector', None, [field, PTR(CStructDUniform), PTR(CStructAVector), PTR(CStructAVector)])
expand_duniform = get_func('expand_duniform', None, [field, PTR(CStructDUniform), PTR(CStructAMatrix)])
norm2_fast_duniform = get_func('norm2_fast_duniform', real, [PTR(CStructDUniform), PTR(CStructDClusterOperator), PTR(CStructDClusterOperator)])
normfrob_fast_duniform = get_func('normfrob_fast_duniform', real, [PTR(CStructDUniform), PTR(CStructDClusterOperator), PTR(CStructDClusterOperator)])
add_projected_duniform = get_func('add_projected_duniform', None, [PTR(CStructDUniform), PTR(CStructDClusterOperator), PTR(CStructDClusterOperator), PTR(CStructDUniform)])
