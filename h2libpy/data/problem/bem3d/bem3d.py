from ctypes import c_void_p, cast, c_uint
from typing import List

import h2libpy.data.geometry.surface3d as geo
import h2libpy.data.matrix as mat
import h2libpy.data.misc as misc
import h2libpy.data.problem.bem3d as pbem3d
import h2libpy.data.vector as vec
import h2libpy.lib.bem3d as libbem3d
import h2libpy.lib.laplacebem3d as liblaplacebem3d
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import pylist_to_ptr, try_wrap


class Bem3d(StructWrapper, cstruct=libbem3d.CStructBem3d):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, gr: geo.Surface3d, row_basis: int, col_basis: int) -> 'Bem3d':
        return cls(liblaplacebem3d.new_bem3d(gr, row_basis, col_basis))

    @classmethod
    def new_slp_laplace(cls, gr: 'geo.Surface3d',
                        q_regular: int, q_singular: int,
                        row_basis: int, col_basis: int) -> 'Bem3d':
        func = liblaplacebem3d.new_slp_laplace_bem3d
        instance = func(gr, q_regular, q_singular, row_basis, col_basis)
        return cls(instance)

    @classmethod
    def new_dlp_laplace(cls, gr: 'geo.Surface3d',
                        q_regular: int, q_singular: int,
                        row_basis: int, col_basis: int,
                        alpha: float) -> 'Bem3d':
        func = liblaplacebem3d.new_dlp_laplace_bem3d
        instance = func(gr, q_regular, q_singular, row_basis, col_basis, alpha)
        return cls(instance)

    # ***** Properties *****

    def __getter_gr(self) -> 'geo.Surface3d':
        return try_wrap(self.cobj().gr, geo.Surface3d)

    def __getter_sq(self) -> 'pbem3d.SingQuad2d':
        return try_wrap(self.cobj().sq, pbem3d.SingQuad2d)

    def __getter_row_basis(self) -> int:
        return self.cobj().row_basis

    def __getter_col_basis(self) -> int:
        return self.cobj().col_basis

    def __getter_alpha(self) -> float:
        return self.cobj().alpha

    def __getter_k(self) -> float:
        return self.cobj().k

    def __getter_kernel_const(self) -> float:
        return self.cobj().kernel_const

    def __getter_aprx(self) -> 'pbem3d.AprxBem3d':
        return try_wrap(self.cobj().aprx, pbem3d.AprxBem3d)

    def __getter_par(self) -> 'pbem3d.ParBem3d':
        return try_wrap(self.cobj().par, pbem3d.ParBem3d)

    def __getter_kernels(self) -> 'pbem3d.KernelBem3d':
        return try_wrap(self.cobj().kernels, pbem3d.KernelBem3d)

    # ***** Methods ******

    def build_const_clustergeometry(self, idx: List[List[int]]) \
            -> 'misc.ClusterGeometry':
        csubs = [pylist_to_ptr(sub, c_uint) for sub in idx]
        cidx = pylist_to_ptr(csubs, c_uint)
        obj = libbem3d.build_bem3d_const_clustergeometry(self, cidx)
        return try_wrap(obj, misc.ClusterGeometry)

    def build_linear_clustergeometry(self, idx: List[List[int]]) \
            -> 'misc.ClusterGeometry':
        csubs = [pylist_to_ptr(sub, c_uint) for sub in idx]
        cidx = pylist_to_ptr(csubs, c_uint)
        obj = libbem3d.build_bem3d_linear_clustergeometry(self, cidx)
        return try_wrap(obj, misc.ClusterGeometry)

    def build_clustergeometry(self, idx: List[List[int]], basis: int) \
            -> 'misc.ClusterGeometry':
        csubs = [pylist_to_ptr(sub, c_uint) for sub in idx]
        cidx = pylist_to_ptr(csubs, c_uint)
        obj = libbem3d.build_bem3d_clustergeometry(self, cidx, basis)
        return try_wrap(obj, misc.ClusterGeometry)

    def build_cluster(self, clf: int, basis: int) \
            -> 'misc.Cluster':
        obj = libbem3d.build_bem3d_cluster(self, clf, basis)
        return try_wrap(obj, misc.Cluster)

    def assemble_amatrix(self, g: 'mat.AMatrix'):
        libbem3d.assemble_bem3d_amatrix(self, g)

    def project_l2_c(self, f, w: 'vec.AVector', data):
        cf = libbem3d.CFuncBoundaryFunc3d(f)
        cdata = cast(data, c_void_p)
        libbem3d.projectL2_bem3d_c_avector(self, cf, w, cdata)

    def norm_l2_diff_c(self, x: 'vec.AVector', rhs, data) -> float:
        crhs = libbem3d.CFuncBoundaryFunc3d(rhs)
        cdata = cast(data, c_void_p)
        return libbem3d.normL2diff_c_bem3d(self, x, crhs, cdata)

    def norm_l2(self, rhs, data) -> float:
        crhs = libbem3d.CFuncBoundaryFunc3d(rhs)
        cdata = cast(data, c_void_p)
        return libbem3d.normL2_bem3d(self, crhs, cdata)
