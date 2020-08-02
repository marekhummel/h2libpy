import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper


class KernelBem3d(StructWrapper, cstruct=libbem3d.CStructKernelBem3d):
    pass
