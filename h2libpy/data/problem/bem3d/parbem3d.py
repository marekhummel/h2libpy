import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper


class ParBem3d(StructWrapper, cstruct=libbem3d.CStructParBem3d):
    # ***** Fields *****
    grcnn: int
    gccnn: int
    grbnn: int
    gcbnn: int

    # ***** Properties *****

    def __getter_grcnn(self) -> int:
        return self.cobj().grcnn

    def __getter_gccnn(self) -> int:
        return self.cobj().gccnn

    def __getter_grbnn(self) -> int:
        return self.cobj().grbnn

    def __getter_gcbnn(self) -> int:
        return self.cobj().gcbnn

    # ***** Methods ******
