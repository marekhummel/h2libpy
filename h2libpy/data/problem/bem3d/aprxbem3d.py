import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.cutil import try_wrap
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.algorithm.truncmode import TruncMode
from h2libpy.data.problem.bem3d.greencluster3d import GreenCluster3d
from h2libpy.data.problem.bem3d.greenclusterbasis3d import GreenClusterBasis3d


class AprxBem3d(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        super().__init__(cobj, libbem3d.CStructAprxBem3d)

    def __del__(self):
        pass

    # ***** Properties *****

    def __getter_m_inter(self) -> int:
        return self.cobj().m_inter

    def __getter_k_inter(self) -> int:
        return self.cobj().k_inter

    def __getter_l_green(self) -> int:
        return self.cobj().l_green

    def __getter_m_green(self) -> int:
        return self.cobj().m_green

    def __getter_ml_green(self) -> int:
        return self.cobj().ml_green

    def __getter_k_green(self) -> int:
        return self.cobj().k_green

    def __getter_delta_green(self) -> float:
        return self.cobj().delta_green

    def __getter_grc_green(self) -> 'GreenCluster3d':
        return try_wrap(self.cobj().grc_green, GreenCluster3d)

    def __getter_gcc_green(self) -> 'GreenCluster3d':
        return try_wrap(self.cobj().gcc_green, GreenCluster3d)

    def __getter_grb_green(self) -> 'GreenClusterBasis3d':
        return try_wrap(self.cobj().grb_green, GreenClusterBasis3d)

    def __getter_gcb_green(self) -> 'GreenClusterBasis3d':
        return try_wrap(self.cobj().gcb_green, GreenClusterBasis3d)

    def __getter_accur_aca(self) -> float:
        return self.cobj().delta_green

    def __getter_recomp(self) -> bool:
        return self.cobj().recomp

    def __getter_accur_recomp(self) -> float:
        return self.cobj().accur_recomp

    def __getter_coarsen(self) -> bool:
        return self.cobj().coarsen

    def __getter_accur_coarsen(self) -> float:
        return self.cobj().accur_coarsen

    def __getter_hiercomp(self) -> bool:
        return self.cobj().hiercomp

    def __getter_accur_hiercomp(self) -> float:
        return self.cobj().accur_hiercomp

    def __getter_tm(self) -> 'TruncMode':
        return try_wrap(self.cobj().tm, TruncMode)

    # ***** Methods ******
