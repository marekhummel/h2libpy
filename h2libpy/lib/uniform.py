from ctypes import POINTER as PTR
from ctypes import Structure as Struct

# from h2libpy.lib.util.helper import get_func

# ------------------------


class CStructUniform(Struct): pass


# ------------------------


from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.clusterbasis import CStructClusterBasis


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
