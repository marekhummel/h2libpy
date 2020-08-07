import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.util import try_wrap
from h2libpy.base.structwrapper import StructWrapper
import h2libpy.data.problem.bem3d as pbem3d


class TriList(StructWrapper, cstruct=libbem3d.CStructTriList):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, nxt: 'TriList'):
        return cls(libbem3d.new_tri_list(nxt))
    
    # ***** Properties *****

    def __getter_t(self) -> int:
        return self.cobj().t

    def __getter_vt(self) -> 'pbem3d.VertList':
        return try_wrap(self.cobj().vl, pbem3d.VertList)

    def __getter_next(self) -> 'TriList':
        return try_wrap(self.cobj().next, TriList)

    # ***** Methods ******
