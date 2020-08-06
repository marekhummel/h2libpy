import h2libpy.lib.truncation as libtruncation
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.misc.enums import TruncModeInit
import h2libpy.data.vector as vec


class TruncMode(StructWrapper, cstruct=libtruncation.CStructTruncMode):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, inittype: 'TruncModeInit' = TruncModeInit.Nothing) \
            -> 'TruncMode':
        if inittype == TruncModeInit.RelEucl:
            return cls(libtruncation.new_releucl_truncmode())
        elif inittype == TruncModeInit.RelFrob:
            return cls(libtruncation.new_relfrob_truncmode())
        elif inittype == TruncModeInit.BlockRelEucl:
            return cls(libtruncation.new_blockreleucl_truncmode())
        elif inittype == TruncModeInit.BlockRelFrob:
            return cls(libtruncation.new_blockrelfrob_truncmode())
        elif inittype == TruncModeInit.AbsEucl:
            return cls(libtruncation.new_abseucl_truncmode())
        else:  # inittype == TruncModeInit.Nothing:
            return cls(libtruncation.new_truncmode())

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

    def find_rank(self, eps: float, sigma: 'vec.RealAVector') -> int:
        return libtruncation.findrank_truncmode(self, eps, sigma)
