import h2libpy.lib.truncation as libtruncation
from h2libpy.base.structwrapper import StructWrapper


class TruncMode(StructWrapper, cstruct=libtruncation.CStructTruncmode):

    # ***** Properties *****

    def __getter_frobenius(self) -> bool:
        return self.cobj().frobenius

    def __getter_absolute(self) -> bool:
        return self.cobj().absolute

    def __getter_blocks(self) -> bool:
        return self.cobj().blocks

    def __getter_zeta_level(self) -> float:
        return self.cobj().zeta_level

    def __getter_zeta_age(self) -> float:
        return self.cobj().zeta_age

    # ***** Methods ******
