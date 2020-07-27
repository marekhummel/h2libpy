import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.cutil import try_wrap
from h2libpy.base.structwrapper import StructWrapper


class ListNode(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        super().__init__(cobj, libbem3d.CStructListNode)

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_data(self) -> int:
        return self.cobj().data

    def __getter_next(self) -> 'ListNode':
        return try_wrap(self.cobj().next, ListNode)

    # ***** Methods ******
