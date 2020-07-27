import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.cutil import try_wrap
from h2libpy.base.structwrapper import StructWrapper


class AdmisBlock(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        super().__init__(cobj, libbem3d.CStructAdmisBlock)

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_name(self) -> int:
        return self.cobj().name

    def __getter_rname(self) -> int:
        return self.cobj().rname

    def __getter_cname(self) -> int:
        return self.cobj().cname

    def __getter_father(self) -> int:
        return self.cobj().father

    def __getter_son(self) -> int:
        return self.cobj().son

    def __getter_length(self) -> int:
        return self.cobj().length

    def __getter_next(self) -> 'AdmisBlock':
        return try_wrap(self.cobj().next, AdmisBlock)

    # ***** Methods ******
