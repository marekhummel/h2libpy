import h2libpy.lib.cluster as libcluster
from h2libpy.base.structwrapper import StructWrapper


class Cluster(StructWrapper, cstruct=libcluster.CStructCluster):
    pass
