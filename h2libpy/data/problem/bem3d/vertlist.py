import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.cutil import try_wrap
from h2libpy.base.structwrapper import StructWrapper


class VertList(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        super().__init__(cobj, libbem3d.CStructVertList)

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_v(self) -> int:
        return self.cobj().v

    def __getter_next(self) -> 'VertList':
        return try_wrap(self.cobj().next, VertList)

    # ***** Methods ******
