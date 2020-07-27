import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.cutil import try_wrap
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.problem.bem3d.vertlist import VertList


class TriList(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        super().__init__(cobj, libbem3d.CStructTriList)

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_t(self) -> int:
        return self.cobj().t

    def __getter_vt(self) -> 'VertList':
        return try_wrap(self.cobj().vl, VertList)

    def __getter_next(self) -> 'TriList':
        return try_wrap(self.cobj().next, TriList)

    # ***** Methods ******
