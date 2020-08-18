import h2libpy.data.misc as misc
import h2libpy.data.problem.bem3d as pbem3d
import h2libpy.lib.bem3d as libbem3d
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import try_wrap


class AprxBem3d(StructWrapper, cstruct=libbem3d.CStructAprxBem3d):
    # ***** Fields *****
    m_inter: int
    k_inter: int
    l_green: int
    m_green: int
    ml_green: int
    k_green: int
    delta_green: float
    grc_green: 'pbem3d.GreenCluster3d'
    gcc_green: 'pbem3d.GreenCluster3d'
    grb_green: 'pbem3d.GreenClusterBasis3d'
    gcb_green: 'pbem3d.GreenClusterBasis3d'
    accur_aca: float
    recomp: bool
    accur_recomp: float
    coarsen: bool
    accur_coarsen: float
    hiercomp: bool
    accur_hiercomp: float
    tm: 'misc.TruncMode'

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

    def __getter_grc_green(self) -> 'pbem3d.GreenCluster3d':
        return try_wrap(self.cobj().grc_green, pbem3d.GreenCluster3d)

    def __getter_gcc_green(self) -> 'pbem3d.GreenCluster3d':
        return try_wrap(self.cobj().gcc_green, pbem3d.GreenCluster3d)

    def __getter_grb_green(self) -> 'pbem3d.GreenClusterBasis3d':
        return try_wrap(self.cobj().grb_green, pbem3d.GreenClusterBasis3d)

    def __getter_gcb_green(self) -> 'pbem3d.GreenClusterBasis3d':
        return try_wrap(self.cobj().gcb_green, pbem3d.GreenClusterBasis3d)

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

    def __getter_tm(self) -> 'misc.TruncMode':
        return try_wrap(self.cobj().tm, misc.TruncMode)

    # ***** Methods ******
