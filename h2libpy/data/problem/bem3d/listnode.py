import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.util import try_wrap
from h2libpy.base.structwrapper import StructWrapper


class ListNode(StructWrapper, cstruct=libbem3d.CStructListNode):
    # ***** Fields *****
    data: int
    next: 'ListNode'

    # ***** Properties *****

    def __getter_data(self) -> int:
        return self.cobj().data

    def __getter_next(self) -> 'ListNode':
        return try_wrap(self.cobj().next, ListNode)

    # ***** Methods ******
