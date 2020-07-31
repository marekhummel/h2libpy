from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_bool, c_uint

from h2libpy.lib.settings import real
from h2libpy.lib.util.helper import get_func

# ------------------------


class CStructTruncmode(Struct): pass


# ------------------------


from h2libpy.lib.realavector import CStructRealAVector


CStructTruncmode._fields_ = [
    ('frobenius', c_bool),
    ('absolute', c_bool),
    ('blocks', c_bool),
    ('zeta_level', real),
    ('zeta_age', real)
]


# ------------------------


new_truncmode = get_func('new_truncmode', PTR(CStructTruncmode), [])
del_truncmode = get_func('del_truncmode', None, [PTR(CStructTruncmode)])
new_releucl_truncmode = get_func('new_releucl_truncmode', PTR(CStructTruncmode), [])
new_relfrob_truncmode = get_func('new_relfrob_truncmode', PTR(CStructTruncmode), [])
new_blockreleucl_truncmode = get_func('new_blockreleucl_truncmode', PTR(CStructTruncmode), [])
new_blockrelfrob_truncmode = get_func('new_blockrelfrob_truncmode', PTR(CStructTruncmode), [])
new_abseucl_truncmode = get_func('new_abseucl_truncmode', PTR(CStructTruncmode), [])
findrank_truncmode = get_func('findrank_truncmode', c_uint, [PTR(CStructTruncmode), real, PTR(CStructRealAVector)])
