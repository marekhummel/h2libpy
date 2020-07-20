from ctypes import POINTER as PTR
from ctypes import Structure as Struct

# from h2libpy.lib.util.helper import get_func

# ------------------------


class LibUniform(Struct): pass


# ------------------------


from h2libpy.lib.amatrix import LibAMatrix
from h2libpy.lib.clusterbasis import LibClusterBasis


LibUniform._fields_ = [
    ('rb', PTR(LibClusterBasis)),
    ('cb', PTR(LibClusterBasis)),
    ('S', LibAMatrix),
    ('rnext', PTR(LibUniform)),
    ('rprev', PTR(LibUniform)),
    ('cnext', PTR(LibUniform)),
    ('cprev', PTR(LibUniform)),
]


# ------------------------
