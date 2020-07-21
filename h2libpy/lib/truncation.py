from ctypes import Structure as Struct
from ctypes import c_bool

from h2libpy.lib.settings import real


class CStructTruncmode(Struct): pass


CStructTruncmode._fields_ = [
    ('frobenius', c_bool),
    ('absolute', c_bool),
    ('blocks', c_bool),
    ('zeta_level', real),
    ('zeta_age', real)
]
