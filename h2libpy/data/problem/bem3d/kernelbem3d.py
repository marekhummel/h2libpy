import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper


class KernelBem3d(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        super().__init__(cobj, libbem3d.CStructKernelBem3d)

    def __del__(self):
        pass

    # ***** Properties *****

    # ***** Methods ******
