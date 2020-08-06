
import h2libpy.lib.clustergeometry as libclustergeometry
from h2libpy.base.structwrapper import StructWrapper


class ClusterGeometry(StructWrapper,
                      cstruct=libclustergeometry.CStructClusterGeometry):
    pass
