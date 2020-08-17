import h2libpy.lib.dcluster as libdcluster
from h2libpy.base.structwrapper import StructWrapper


class DCluster(StructWrapper, cstruct=libdcluster.CStructDCluster):
    pass
    # ***** Constructors / destructor *****

    # ***** Properties *****

    # ***** Methods ******
