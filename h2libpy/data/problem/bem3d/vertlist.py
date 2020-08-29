import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.util import try_wrap
from h2libpy.base.structwrapper import StructWrapper


class VertList(StructWrapper, cstruct=libbem3d.CStructVertList):
    # ***** Fields *****
    v: int
    next: 'VertList'

    # ***** Constructors *****

    @classmethod
    def new(cls, nxt: 'VertList') -> 'VertList':
        return cls(libbem3d.new_vert_list(nxt))

    # ***** Properties *****

    def __getter_v(self) -> int:
        return self.cobj().v

    def __getter_next(self) -> 'VertList':
        return try_wrap(self.cobj().next, VertList)

    # ***** Methods ******

    def delete(self) -> None:
        libbem3d.del_vert_list(self)
