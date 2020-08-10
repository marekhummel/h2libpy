from ctypes import c_uint, c_void_p, cast, pointer
from typing import List, Tuple

import h2libpy.data.geometry.surface3d as geo
import h2libpy.data.matrix as mat
import h2libpy.data.misc as misc
import h2libpy.data.problem.bem3d as pbem3d
import h2libpy.data.vector as vec
import h2libpy.lib.bem3d as libbem3d
import h2libpy.lib.laplacebem3d as liblaplacebem3d
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import pylist_to_ptr, try_wrap
from h2libpy.data.problem.bem3d.enums import (IntegralType,
                                              InterpolationDirection,
                                              LagrangeType, QuadratureType)
from h2libpy.lib.settings import real

VectorListType = List[Tuple[float, float, float]]


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

    def assemble_quad(self, quadtype: 'QuadratureType', ridx: List[int],
                      cidx: List[int], ntrans: bool, n: 'mat.AMatrix', kernel):
        if quadtype == QuadratureType.CCNear:
            func = libbem3d.assemble_cc_near_bem3d
        elif quadtype == QuadratureType.CCFar:
            func = libbem3d.assemble_cc_far_bem3d
        elif quadtype == QuadratureType.CLNear:
            func = libbem3d.assemble_cl_near_bem3d
        elif quadtype == QuadratureType.CLFar:
            func = libbem3d.assemble_cl_far_bem3d
        elif quadtype == QuadratureType.LCNear:
            func = libbem3d.assemble_lc_near_bem3d
        elif quadtype == QuadratureType.LCFar:
            func = libbem3d.assemble_lc_far_bem3d
        elif quadtype == QuadratureType.LLNear:
            func = libbem3d.assemble_ll_near_bem3d
        elif quadtype == QuadratureType.LLFar:
            func = libbem3d.assemble_ll_far_bem3d

        cridx = pylist_to_ptr(ridx, c_uint)
        ccidx = pylist_to_ptr(cidx, c_uint)
        ckernel = libbem3d.CFuncKernelFunc3d(kernel)
        func(cridx, ccidx, self, ntrans, n, ckernel)

    def fill(self, x: VectorListType, y: VectorListType, nx: VectorListType,
             ny: VectorListType, v: 'mat.AMatrix', kernel):
        cx = pylist_to_ptr([pylist_to_ptr(list(v), real) for v in x], real)
        cy = pylist_to_ptr([pylist_to_ptr(list(v), real) for v in y], real)
        cnx = pylist_to_ptr([pylist_to_ptr(list(v), real) for v in nx], real)
        cny = pylist_to_ptr([pylist_to_ptr(list(v), real) for v in ny], real)
        ckernel = libbem3d.CFuncKernelFunc3d(kernel)
        libbem3d.fill_bem3d(self, cx, cy, cnx, cny, v, ckernel)

    def fill_wave(self, x: VectorListType, y: VectorListType,
                  nx: VectorListType, ny: VectorListType, v: 'mat.AMatrix',
                  direc: float, kernel):
        cx = pylist_to_ptr([pylist_to_ptr(list(v), real) for v in x], real)
        cy = pylist_to_ptr([pylist_to_ptr(list(v), real) for v in y], real)
        cnx = pylist_to_ptr([pylist_to_ptr(list(v), real) for v in nx], real)
        cny = pylist_to_ptr([pylist_to_ptr(list(v), real) for v in ny], real)
        cdirec = pointer(direc)
        ckernel = libbem3d.CFuncKernelWaveFunc3d(kernel)
        libbem3d.fill_wave_bem3d(self, cx, cy, cnx, cny, v, cdirec, ckernel)

    def fill_integral(self, integral_type: 'IntegralType', idx: List[int],
                      z: VectorListType, v: 'mat.AMatrix', kernel):
        if integral_type == IntegralType.RowC:
            func = libbem3d.fill_row_c_bem3d
        elif integral_type == IntegralType.ColC:
            func = libbem3d.fill_col_c_bem3d
        elif integral_type == IntegralType.RowL:
            func = libbem3d.fill_row_l_bem3d
        elif integral_type == IntegralType.ColL:
            func = libbem3d.fill_col_l_bem3d

        cidx = pylist_to_ptr(idx, c_uint)
        cz = pylist_to_ptr([pylist_to_ptr(list(v), real) for v in z], real)
        ckernel = libbem3d.CFuncKernelFunc3d(kernel)
        func(cidx, cz, self, v, ckernel)

    def fill_dnz_integral(self, integral_type: 'IntegralType', idx: List[int],
                          z: VectorListType, n: VectorListType,
                          v: 'mat.AMatrix', kernel):
        if integral_type == IntegralType.RowC:
            func = libbem3d.fill_dnz_row_c_bem3d
        elif integral_type == IntegralType.ColC:
            func = libbem3d.fill_dnz_col_c_bem3d
        elif integral_type == IntegralType.RowL:
            func = libbem3d.fill_dnz_row_l_bem3d
        elif integral_type == IntegralType.ColL:
            func = libbem3d.fill_dnz_col_l_bem3d

        cidx = pylist_to_ptr(idx, c_uint)
        cz = pylist_to_ptr([pylist_to_ptr(list(v), real) for v in z], real)
        cn = pylist_to_ptr([pylist_to_ptr(list(v), real) for v in n], real)
        ckernel = libbem3d.CFuncKernelFunc3d(kernel)
        func(cidx, cz, cn, self, v, ckernel)

    def setup_hmatrix_recomp(self, recomb: bool, accur_recomp: float,
                             coarsen: bool, accur_coarsen: float):
        libbem3d.setup_hmatrix_recomp_bem3d(self, recomb, accur_recomp,
                                            coarsen, accur_coarsen)

    def setup_hmatrix_aprx_inter(self, direc: 'InterpolationDirection',
                                 rc: 'misc.Cluster', cc: 'misc.Cluster',
                                 tree: 'misc.Block', m: int):
        if direc == InterpolationDirection.Row:
            func = libbem3d.setup_hmatrix_aprx_inter_row_bem3d
        elif direc == InterpolationDirection.Col:
            func = libbem3d.setup_hmatrix_aprx_inter_col_bem3d
        elif direc == InterpolationDirection.Mixed:
            func = libbem3d.setup_hmatrix_aprx_inter_mixed_bem3d
        func(self, rc, cc, tree, m)

    def setup_hmatrix_aprx_green(self, direc: 'InterpolationDirection',
                                 rc: 'misc.Cluster', cc: 'misc.Cluster',
                                 tree: 'misc.Block', m: int, l: int,
                                 delta: float, quadpoints):
        if direc == InterpolationDirection.Row:
            func = libbem3d.setup_hmatrix_aprx_green_row_bem3d
        elif direc == InterpolationDirection.Col:
            func = libbem3d.setup_hmatrix_aprx_green_col_bem3d
        elif direc == InterpolationDirection.Mixed:
            func = libbem3d.setup_hmatrix_aprx_green_mixed_bem3d

        cquadpoints = libbem3d.CFuncQuadPoints3d(quadpoints)
        func(self, rc, cc, tree, m, l, delta, cquadpoints)

    def setup_hmatrix_aprx_greenhybrid(self, direc: 'InterpolationDirection',
                                       rc: 'misc.Cluster', cc: 'misc.Cluster',
                                       tree: 'misc.Block', m: int, l: int,
                                       delta: float, accur: float, quadpoints):
        if direc == InterpolationDirection.Row:
            func = libbem3d.setup_hmatrix_aprx_greenhybrid_row_bem3d
        elif direc == InterpolationDirection.Col:
            func = libbem3d.setup_hmatrix_aprx_greenhybrid_col_bem3d
        elif direc == InterpolationDirection.Mixed:
            func = libbem3d.setup_hmatrix_aprx_greenhybrid_mixed_bem3d

        cquadpoints = libbem3d.CFuncQuadPoints3d(quadpoints)
        func(self, rc, cc, tree, m, l, delta, accur, cquadpoints)

    def setup_hmatrix_aprx_aca(self, rc: 'misc.Cluster', cc: 'misc.Cluster',
                               tree: 'misc.Block', accur: float,
                               *, partial: bool = False):
        if partial:
            libbem3d.setup_hmatrix_aprx_paca_bem3d(self, rc, cc, tree, accur)
        else:
            libbem3d.setup_hmatrix_aprx_aca_bem3d(self, rc, cc, tree, accur)

    def setup_hmatrix_aprx_hca(self, rc: 'misc.Cluster', cc: 'misc.Cluster',
                               tree: 'misc.Block', m: int, accur: float):
        libbem3d.setup_hmatrix_aprx_hca_bem3d(self, rc, cc, tree, m, accur)

    def setup_h2matrix_recomp(self, hiercomp: bool, accur_hiercomp: float):
        libbem3d.setup_h2matrix_recomp_bem3d(self, hiercomp, accur_hiercomp)

    def setup_h2matrix_aprx_inter(self, rb: 'misc.ClusterBasis',
                                  cb: 'misc.ClusterBasis', tree: 'misc.Block',
                                  m: int):
        libbem3d.setup_h2matrix_aprx_inter_bem3d(self, rb, cb, tree, m)

    def setup_h2matrix_aprx_greenhybrid(self, rb: 'misc.ClusterBasis',
                                        cb: 'misc.ClusterBasis',
                                        tree: 'misc.Block', m: int, l: int,
                                        delta: float, accur: float,
                                        quadpoints, *, ortho: bool = False):
        cquadpoints = libbem3d.CFuncQuadPoints3d(quadpoints)
        if ortho:
            func = libbem3d.setup_h2matrix_aprx_greenhybrid_ortho_bem3d
        else:
            func = libbem3d.setup_h2matrix_aprx_greenhybrid_bem3d
        func(self, rb, cb, tree, m, l, delta, accur, cquadpoints)

    def setup_dh2matrix_aprx_inter(self, rb: 'misc.DClusterBasis',
                                   cb: 'misc.DClusterBasis',
                                   tree: 'misc.DBlock', m: int,
                                   *, ortho: bool = False):
        if ortho:
            func = libbem3d.setup_dh2matrix_aprx_inter_ortho_bem3d
            func(self, rb, cb, tree, m)
        else:
            libbem3d.setup_dh2matrix_aprx_inter_bem3d(self, rb, cb, tree, m)

    def setup_dh2matrix_aprx_inter_recomp(self, rb: 'misc.DClusterBasis',
                                          cb: 'misc.DClusterBasis',
                                          tree: 'misc.DBlock', m: int,
                                          tm: 'misc.TruncMode', eps: float):
        func = libbem3d.setup_dh2matrix_aprx_inter_recomp_bem3d
        func(self, rb, cb, tree, m, tm, eps)

    def assemble_amatrix(self, g: 'mat.AMatrix'):
        libbem3d.assemble_bem3d_amatrix(self, g)

    def assemble_hmatrix(self, b: 'misc.Block', g: 'mat.HMatrix', *,
                         coarsen: bool = False):
        if coarsen:
            libbem3d.assemblecoarsen_bem3d_hmatrix(self, b, g)
        else:
            libbem3d.assemble_bem3d_hmatrix(self, b, g)

    def assemble_hmatrix_near(self, b: 'misc.Block', g: 'mat.HMatrix'):
        libbem3d.assemble_bem3d_nearfield_hmatrix(self, b, g)

    def assemble_hmatrix_far(self, b: 'misc.Block', g: 'mat.HMatrix'):
        libbem3d.assemble_bem3d_farfield_hmatrix(self, b, g)

    def assemble_h2matrix_row(self, rb: 'misc.ClusterBasis'):
        libbem3d.assemble_bem3d_h2matrix_row_clusterbasis(self, rb)

    def assemble_h2matrix_col(self, cb: 'misc.ClusterBasis'):
        libbem3d.assemble_bem3d_h2matrix_col_clusterbasis(self, cb)

    def assemble_h2matrix(self, g: 'mat.H2Matrix'):
        libbem3d.assemble_bem3d_h2matrix(self, g)

    def assemble_h2matrix_near(self, g: 'mat.H2Matrix'):
        libbem3d.assemble_bem3d_nearfield_h2matrix(self, g)

    def assemble_h2matrix_far(self, g: 'mat.H2Matrix'):
        libbem3d.assemble_bem3d_farfield_h2matrix(self, g)

    def assemble_hiercomp_h2matrix(self, b: 'misc.Block', g: 'mat.H2Matrix'):
        libbem3d.assemblehiercomp_bem3d_h2matrix(self, b, g)

    def assemble_dh2matrix_row(self, rb: 'misc.DClusterBasis'):
        libbem3d.assemble_bem3d_dh2matrix_row_dclusterbasis(self, rb)

    def assemble_dh2matrix_col(self, cb: 'misc.DClusterBasis'):
        libbem3d.assemble_bem3d_h2matrix_col_dclusterbasis(self, cb)

    def assemble_dh2matrix_row_ortho(self, rb: 'misc.DClusterBasis',
                                     ro: 'misc.DClusterOperator'):
        libbem3d.assemble_bem3d_dh2matrix_ortho_row_dclusterbasis(self, rb, ro)

    def assemble_dh2matrix_col_ortho(self, cb: 'misc.DClusterBasis',
                                     co: 'misc.DClusterOperator'):
        libbem3d.assemble_bem3d_dh2matrix_ortho_row_dclusterbasis(self, cb, co)

    def assemble_dh2matrix_recomp_both(self, rb: 'misc.DClusterBasis',
                                       ro: 'misc.DClusterOperator',
                                       cb: 'misc.DClusterBasis',
                                       co: 'misc.DClusterOperator',
                                       root: 'misc.DBlock'):
        func = libbem3d.assemble_bem3d_dh2matrix_recomp_both_dclusterbasis
        func(self, rb, ro, cb, co, root)

    def assemble_dh2matrix(self, g: 'mat.DH2Matrix'):
        libbem3d.assemble_bem3d_dh2matrix(self, g)

    def assemble_dh2matrix_near(self, g: 'mat.DH2Matrix'):
        libbem3d.assemble_bem3d_nearfield_dh2matrix(self, g)

    def assemble_dh2matrix_far(self, g: 'mat.DH2Matrix'):
        libbem3d.assemble_bem3d_farfield_dh2matrix(self, g)

    def assemble_lagrange(self, ltype: 'LagrangeType', idx: List[int],
                          px: 'vec.AVector', py: 'vec.AVector',
                          pz: 'vec.AVector', v: 'mat.AMatrix'):
        if ltype == LagrangeType.Const:
            func = libbem3d.assemble_bem3d_lagrange_c_amatrix
        elif ltype == LagrangeType.Linear:
            func = libbem3d.assemble_bem3d_lagrange_l_amatrix
        elif ltype == LagrangeType.DnConst:
            func = libbem3d.assemble_bem3d_dn_lagrange_c_amatrix
        elif ltype == LagrangeType.DnLinear:
            func = libbem3d.assemble_bem3d_dn_lagrange_l_amatrix

        cidx = pylist_to_ptr(idx, c_uint)
        func(cidx, px, py, pz, self, v)

    def assemble_lagrange_wave(self, ltype: 'LagrangeType', idx: List[int],
                               px: 'vec.AVector', py: 'vec.AVector',
                               pz: 'vec.AVector', direc: float,
                               v: 'mat.AMatrix'):
        if ltype == LagrangeType.Const:
            func = libbem3d.assemble_bem3d_dn_lagrange_wave_c_amatrix
        elif ltype == LagrangeType.Linear:
            func = libbem3d.assemble_bem3d_dn_lagrange_wave_l_amatrix
        elif ltype == LagrangeType.DnConst:
            func = libbem3d.assemble_bem3d_dn_lagrange_wave_c_amatrix
        elif ltype == LagrangeType.DnLinear:
            func = libbem3d.assemble_bem3d_dn_lagrange_wave_l_amatrix

        cidx = pylist_to_ptr(idx, c_uint)
        func(cidx, px, py, pz, direc, self, v)

    def eval_lagrange(self, x: Tuple[float, float, float], px: 'vec.AVector',
                      py: 'vec.AVector', pz: 'vec.AVector', v: 'mat.AMatrix'):
        cx = pylist_to_ptr(list(x), real)
        libbem3d.assemble_bem3d_lagrange_amatrix(cx, px, py, pz, self, v)

    def eval_lagrange_wave(self, x: Tuple[float, float, float],
                           px: 'vec.AVector', py: 'vec.AVector',
                           pz: 'vec.AVector', direc: float, v: 'mat.AMatrix'):
        cx = pylist_to_ptr(list(x), real)
        func = libbem3d.assemble_bem3d_lagrange_wave_amatrix
        func(cx, px, py, pz, direc, self, v)

    def norm_l2(self, f, data) -> float:
        cf = libbem3d.CFuncBoundaryFunc3d(f)
        cdata = cast(data, c_void_p)
        return libbem3d.normL2_bem3d(self, cf, cdata)

    def norm_l2_c(self, x: 'vec.AVector') -> float:
        return libbem3d.normL2_c_bem3d(self, x)

    def norm_l2_diff_c(self, x: 'vec.AVector', f, data) -> float:
        cf = libbem3d.CFuncBoundaryFunc3d(f)
        cdata = cast(data, c_void_p)
        return libbem3d.normL2diff_c_bem3d(self, x, cf, cdata)

    def norm_l2_l(self, x: 'vec.AVector') -> float:
        return libbem3d.normL2_l_bem3d(self, x)

    def norm_l2_diff_l(self, x: 'vec.AVector', f, data) -> float:
        cf = libbem3d.CFuncBoundaryFunc3d(f)
        cdata = cast(data, c_void_p)
        return libbem3d.normL2diff_l_bem3d(self, x, cf, cdata)

    def integrate_c(self, f, w: 'vec.AVector', data):
        cf = libbem3d.CFuncBoundaryFunc3d(f)
        cdata = cast(data, c_void_p)
        libbem3d.integrate_bem3d_c_avector(self, cf, w, cdata)

    def integrate_l(self, f, w: 'vec.AVector', data):
        cf = libbem3d.CFuncBoundaryFunc3d(f)
        cdata = cast(data, c_void_p)
        libbem3d.integrate_bem3d_l_avector(self, cf, w, cdata)

    def project_l2_c(self, f, w: 'vec.AVector', data):
        cf = libbem3d.CFuncBoundaryFunc3d(f)
        cdata = cast(data, c_void_p)
        libbem3d.projectL2_bem3d_c_avector(self, cf, w, cdata)

    def project_l2_l(self, f, w: 'vec.AVector', data):
        cf = libbem3d.CFuncBoundaryFunc3d(f)
        cdata = cast(data, c_void_p)
        libbem3d.projectL2_bem3d_l_avector(self, cf, w, cdata)

    def setup_vertex_to_triangle_map(self):
        libbem3d.setup_vertex_to_triangle_map(self)

    # def build_cube_quadpoints(self):
    #     pass

    def build_rkmatrix(self, row: 'misc.Cluster', col: 'misc.Cluster') \
            -> 'mat.RkMatrix':
        cdata = cast(self, c_void_p)
        obj = libbem3d.build_bem3d_rkmatrix(row, col, cdata)
        return try_wrap(obj, mat.RkMatrix)

    def build_amatrix(self, row: 'misc.Cluster', col: 'misc.Cluster') \
            -> 'mat.AMatrix':
        cdata = cast(self, c_void_p)
        obj = libbem3d.build_bem3d_amatrix(row, col, cdata)
        return try_wrap(obj, mat.AMatrix)

    # def build_curl_sparsematrix(self):
    #     pass
