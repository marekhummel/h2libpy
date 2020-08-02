import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.cutil import try_wrap
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.problem.bem3d.bem3d import Bem3d


class CompData(StructWrapper, cstruct=libbem3d.CStructCompData):

    # ***** Properties *****

    def __getter_bem(self) -> 'Bem3d':
        return try_wrap(self.cobj().bem, Bem3d)

    def __getter_rows(self) -> bool:
        return self.cobj().rows

    # ***** Methods ******
