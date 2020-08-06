from ctypes import POINTER as PTR
from ctypes import c_bool, c_uint

from h2libpy.lib.settings import real
from h2libpy.lib.util.helper import get_func
from h2libpy.lib.util.structs import CStructRealAVector, CStructTruncMode

# ------------------------


CStructTruncMode._fields_ = [
    ('frobenius', c_bool),
    ('absolute', c_bool),
    ('blocks', c_bool),
    ('zeta_level', real),
    ('zeta_age', real)
]


# ------------------------


new_truncmode = get_func('new_truncmode', PTR(CStructTruncMode), [])
del_truncmode = get_func('del_truncmode', None, [PTR(CStructTruncMode)])
new_releucl_truncmode = get_func('new_releucl_truncmode', PTR(CStructTruncMode), [])
new_relfrob_truncmode = get_func('new_relfrob_truncmode', PTR(CStructTruncMode), [])
new_blockreleucl_truncmode = get_func('new_blockreleucl_truncmode', PTR(CStructTruncMode), [])
new_blockrelfrob_truncmode = get_func('new_blockrelfrob_truncmode', PTR(CStructTruncMode), [])
new_abseucl_truncmode = get_func('new_abseucl_truncmode', PTR(CStructTruncMode), [])
findrank_truncmode = get_func('findrank_truncmode', c_uint, [PTR(CStructTruncMode), real, PTR(CStructRealAVector)])
