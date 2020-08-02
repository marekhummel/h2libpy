import h2libpy.lib.singquad2d as libsingquad2d
from h2libpy.base.structwrapper import StructWrapper


class SingQuad2d(StructWrapper, cstruct=libsingquad2d.CStructSingquad2d):

    # ***** Properties *****

    def __getter_base_id(self) -> float:
        return self.cobj().base_id

    def __getter_n_id(self) -> int:
        return self.cobj().n_id

    def __getter_base_edge(self) -> float:
        return self.cobj().base_edge

    def __getter_n_edge(self) -> int:
        return self.cobj().n_edge

    def __getter_base_vert(self) -> float:
        return self.cobj().base_vert

    def __getter_n_vert(self) -> int:
        return self.cobj().n_vert

    def __getter_base_dist(self) -> float:
        return self.cobj().base_dist

    def __getter_n_dist(self) -> int:
        return self.cobj().n_dist

    def __getter_base_single(self) -> float:
        return self.cobj().base_single

    def __getter_n_single(self) -> int:
        return self.cobj().n_single

    def __getter_q(self) -> int:
        return self.cobj().q

    def __getter_q2(self) -> int:
        return self.cobj().q2

    def __getter_nmax(self) -> int:
        return self.cobj().nmax

    # ***** Methods ******
