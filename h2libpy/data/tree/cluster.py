import h2libpy.lib.cluster as libcluster
from h2libpy.base.structwrapper import StructWrapper


class Cluster(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        super().__init__(cobj, libcluster.CStructCluster)

    def __del__(self):
        pass

    # ***** Properties *****

    # ***** Methods ******
