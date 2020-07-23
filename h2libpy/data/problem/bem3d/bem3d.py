from ctypes import POINTER, c_double
from typing import Tuple

import h2libpy.lib.bem3d as libbem3d
import h2libpy.lib.laplacebem3d as liblaplacebem3d
from h2libpy.base.cutil import cptr_to_list, deref
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.geometry.surface3d import Surface3d
from h2libpy.data.problem.bem3d.aprxbem3d import AprxBem3d
from h2libpy.data.problem.bem3d.kernelbem3d import KernelBem3d
from h2libpy.data.problem.bem3d.parbem3d import ParBem3d
from h2libpy.data.problem.bem3d.singquad2d import SingQuad2d


class Bem3d(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libbem3d.CStructBem3d))
        self._as_parameter_ = cobj

    def __del__(self):
        pass
        # libbem3d.del_bem3d(self)

    @classmethod
    def new(cls, gr: Surface3d, row_basis: int, col_basis: int) -> 'Bem3d':
        return cls(liblaplacebem3d.new_bem3d(gr, row_basis, col_basis))

    @classmethod
    def new_slp_laplace(cls, gr: Surface3d,
                        q_regular: int, q_singular: int,
                        row_basis: int, col_basis: int) -> 'Bem3d':
        func = liblaplacebem3d.new_slp_laplace_bem3d
        instance = func(gr, q_regular, q_singular, row_basis, col_basis)
        return cls(instance)

    @classmethod
    def new_dlp_laplace(cls, gr: Surface3d,
                        q_regular: int, q_singular: int,
                        row_basis: int, col_basis: int,
                        alpha: float) -> 'Bem3d':
        func = liblaplacebem3d.new_dlp_laplace_bem3d
        instance = func(gr, q_regular, q_singular, row_basis, col_basis, alpha)
        return cls(instance)

    # ***** Properties *****

    def __getter_gr(self) -> Surface3d:
        return Surface3d(self.cobj().gr)

    def __getter_sq(self) -> SingQuad2d:
        return SingQuad2d(self.cobj().sq)

    def __getter_row_basis(self) -> int:
        return self.cobj().row_basis

    def __getter_col_basis(self) -> int:
        return self.cobj().col_basis

    # def __getter_mass(self) -> int:
    #     return deref(self.cobj().mass)

    def __getter_alpha(self) -> float:
        return self.cobj().alpha

    def __getter_k(self) -> float:
        return self.cobj().k

    def __getter_kernel_const(self) -> float:
        return self.cobj().kernel_const

    def __getter_aprx(self) -> AprxBem3d:
        return AprxBem3d(self.cobj().aprx)

    def __getter_par(self) -> ParBem3d:
        return ParBem3d(self.cobj().par)

    def __getter_kernel(self) -> KernelBem3d:
        return KernelBem3d(self.cobj().kernels)

    # ***** Methods ******
