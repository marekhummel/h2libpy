import h2libpy.data.problem.bem3d as pbem3d
import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import try_wrap


class CompData(StructWrapper, cstruct=libbem3d.CStructCompData):
    # ***** Fields *****
    bem: 'pbem3d.Bem3d'
    rows: bool

    # ***** Properties *****

    def __getter_bem(self) -> 'pbem3d.Bem3d':
        return try_wrap(self.cobj().bem, pbem3d.Bem3d)

    def __getter_rows(self) -> bool:
        return self.cobj().rows

    # ***** Methods ******
