from ctypes import POINTER

import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper


class ListNode(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libbem3d.CStructListNode))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_data(self) -> int:
        return self.cobj().data

    def __getter_next(self) -> 'ListNode':
        return self.try_wrap(self.cobj().next, ListNode)

    # ***** Methods ******
