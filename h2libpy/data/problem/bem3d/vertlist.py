import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.util import try_wrap
from h2libpy.base.structwrapper import StructWrapper


class VertList(StructWrapper, cstruct=libbem3d.CStructVertList):

    # ***** Properties *****

    def __getter_v(self) -> int:
        return self.cobj().v

    def __getter_next(self) -> 'VertList':
        return try_wrap(self.cobj().next, VertList)

    # ***** Methods ******
