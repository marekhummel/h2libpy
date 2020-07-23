from ctypes import POINTER

import h2libpy.lib.truncation as libtruncation
from h2libpy.base.structwrapper import StructWrapper


class TruncMode(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libtruncation.CStructTruncmode))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

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
