
import h2libpy.lib.clusteroperator as libclusteroperator
from h2libpy.base.structwrapper import StructWrapper


class ClusterOperator(StructWrapper,
                      cstruct=libclusteroperator.CStructClusterOperator):
    pass
