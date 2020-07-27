import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.cutil import try_wrap
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.problem.bem3d.bem3d import Bem3d


class CompData(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        super().__init__(cobj, libbem3d.CStructCompData)

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_bem(self) -> 'Bem3d':
        return try_wrap(self.cobj().bem, Bem3d)

    def __getter_rows(self) -> bool:
        return self.cobj().rows

    # ***** Methods ******
