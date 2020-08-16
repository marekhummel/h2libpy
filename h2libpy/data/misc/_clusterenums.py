from enum import Enum
from h2libpy.lib.cluster import CEnumClusterMode


class ClusterMode(Enum):
    Adaptive = CEnumClusterMode.H2_ADAPTIVE
    Regular = CEnumClusterMode.H2_REGULAR
    SimSub = CEnumClusterMode.H2_SIMSUB
    PCA = CEnumClusterMode.H2_PCA
