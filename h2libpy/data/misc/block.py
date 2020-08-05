import h2libpy.lib.block as libblock
from h2libpy.base.structwrapper import StructWrapper


class Block(StructWrapper, cstruct=libblock.CStructBlock):

    @classmethod
    def from_hmatrix(cls):
        pass
