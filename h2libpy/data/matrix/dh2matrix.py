import h2libpy.lib.dh2matrix as libdh2matrix
from h2libpy.base.structwrapper import StructWrapper


class DH2Matrix(StructWrapper, cstruct=libdh2matrix.CStructDH2Matrix):
    pass
