from ctypes import CFUNCTYPE
from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_bool, c_uint, c_void_p

from h2libpy.lib.settings import field, real
from h2libpy.lib.util.helper import get_func

# ------------------------------------


class CStructBem3d(Struct): pass
class CStructKernelBem3d(Struct): pass
class CStructVertList(Struct): pass
class CStructListNode(Struct): pass
class CStructTriList(Struct): pass
class CStructAprxBem3d(Struct): pass
class CStructParBem3d(Struct): pass
class CStructGreenCluster3d(Struct): pass
class CStructGreenClusterBasis3d(Struct): pass
class CStructAdmisBlock(Struct): pass
class CStructCompData(Struct): pass

class CEnumBasisFunctionBem3d(c_uint): pass


# ------------------------------------


from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.avector import CStructAVector
from h2libpy.lib.block import CStructBlock
from h2libpy.lib.cluster import CStructCluster
from h2libpy.lib.clusterbasis import CStructClusterBasis
from h2libpy.lib.clustergeometry import CStructClusterGeometry
from h2libpy.lib.clusteroperator import CStructClusterOperator
from h2libpy.lib.dblock import CStructDBlock
from h2libpy.lib.dclusterbasis import CStructDClusterBasis
from h2libpy.lib.dclusteroperator import CStructDClusterOperator
from h2libpy.lib.dh2matrix import CStructDH2Matrix
from h2libpy.lib.h2matrix import CStructH2Matrix
from h2libpy.lib.hmatrix import CStructHMatrix
from h2libpy.lib.realavector import CStructRealAVector
from h2libpy.lib.rkmatrix import CStructRkMatrix
from h2libpy.lib.singquad2d import CStructSingquad2d
from h2libpy.lib.sparsematrix import CStructSparseMatrix
from h2libpy.lib.surface3d import CStructSurface3d
from h2libpy.lib.truncation import CStructTruncmode


CFuncQuadPoints3d = CFUNCTYPE(None, *[PTR(CStructBem3d), real*3, real*3, real, PTR(PTR(real))*3, PTR(PTR(real))*3])
CFuncBoundaryFunc3d = CFUNCTYPE(field, *[PTR(real), PTR(real), c_void_p])
CFuncKernelFunc3d = CFUNCTYPE(field, *[PTR(real), PTR(real), PTR(real), PTR(real), c_void_p])
CFuncKernelWaveFunc3d = CFUNCTYPE(field, *[PTR(real), PTR(real), PTR(real), PTR(real), PTR(real), c_void_p])
CFuncNearField = CFUNCTYPE(None, *[PTR(c_uint), PTR(c_uint), PTR(CStructBem3d), c_bool, PTR(CStructAMatrix)])
CFuncFarFieldRk = CFUNCTYPE(None, *[PTR(CStructCluster), c_uint, PTR(CStructCluster), c_uint, PTR(CStructBem3d), PTR(CStructRkMatrix)])
CFuncFarFieldU = CFUNCTYPE(None, *[c_uint, c_uint, c_uint, PTR(CStructBem3d)])
CFuncLeafRowCol = CFUNCTYPE(None, *[c_uint, PTR(CStructBem3d)])
CFuncTransferRowCol = CFuncLeafRowCol

CFuncFundamental = CFUNCTYPE(None, *[PTR(CStructBem3d), PTR(real*3), PTR(real*3), PTR(CStructAMatrix)])
CFuncFundamentalWave = CFUNCTYPE(None, *[PTR(CStructBem3d), PTR(real*3), PTR(real*3), PTR(real), PTR(CStructAMatrix)])
CFuncDnyFundamental = CFUNCTYPE(None, *[PTR(CStructBem3d), PTR(real*3), PTR(real*3), PTR(real*3), PTR(CStructAMatrix)])
CFuncDnxDnyFundamental = CFUNCTYPE(None, *[PTR(CStructBem3d), PTR(real*3), PTR(real*3), PTR(real*3), PTR(real*3), PTR(CStructAMatrix)])
CFuncKernelRowCol = CFUNCTYPE(None, *[PTR(c_uint), PTR(real*3), PTR(CStructBem3d), PTR(CStructAMatrix)])
CFuncDnzKernelRowCol = CFUNCTYPE(None, *[PTR(c_uint), PTR(real*3), PTR(real*3), PTR(CStructBem3d), PTR(CStructAMatrix)])
CFuncFundamentalRowCol = CFuncKernelRowCol
CFuncDnzFundamentalRowCol = CFuncDnzKernelRowCol
CFuncLagrangeRowCol = CFUNCTYPE(None, *[PTR(c_uint), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructBem3d), PTR(CStructAMatrix)])
CFuncLagrangeWaveRowCol = CFUNCTYPE(None, *[PTR(c_uint), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(real), PTR(CStructBem3d), PTR(CStructAMatrix)])

CEnumBasisFunctionBem3d.BASIS_NONE_BEM3D = CEnumBasisFunctionBem3d(0)
CEnumBasisFunctionBem3d.BASIS_CONSTANT_BEM3D = CEnumBasisFunctionBem3d(ord('c'))
CEnumBasisFunctionBem3d.BASIS_LINEAR_BEM3D = CEnumBasisFunctionBem3d(ord('l'))

# ------------------------------------


CStructBem3d._fields_ = [
    ('gr', PTR(CStructSurface3d)),
    ('sq', PTR(CStructSingquad2d)),
    ('row_basis', CEnumBasisFunctionBem3d),
    ('col_basis', CEnumBasisFunctionBem3d),
    ('mass', PTR(real)),
    ('alpha', field),
    ('k', field),
    ('kernel_const', field),
    ('v2t', PTR(PTR(CStructListNode))),
    ('nearfield', CFuncNearField),
    ('nearfield_far', CFuncNearField),
    ('farfield_rk', CFuncFarFieldRk),
    ('farfield_u', CFuncFarFieldU),
    ('farfield_wave_u', CFuncFarFieldU),
    ('leaf_row', CFuncLeafRowCol),
    ('leaf_wave_row', CFuncLeafRowCol),
    ('leaf_col', CFuncLeafRowCol),
    ('leaf_wave_col', CFuncLeafRowCol),
    ('transfer_row', CFuncTransferRowCol),
    ('transfer_wave_row', CFuncTransferRowCol),
    ('transfer_wave_wave_row', CFuncTransferRowCol),
    ('transfer_col', CFuncTransferRowCol),
    ('transfer_wave_col', CFuncTransferRowCol),
    ('transfer_wave_wave_col', CFuncTransferRowCol),
    ('aprx', PTR(CStructAprxBem3d)),
    ('par', PTR(CStructParBem3d)),
    ('kernels', PTR(CStructKernelBem3d)),
]

CStructKernelBem3d._fields_ = [
    ('fundamental', CFuncFundamental),
    ('fundamental_wave', CFuncFundamentalWave),
    ('dny_fundamental', CFuncDnyFundamental),
    ('dnx_dny_fundamental', CFuncDnxDnyFundamental),
    ('kernel_row', CFuncKernelRowCol),
    ('kernel_col', CFuncKernelRowCol),
    ('dnz_kernel_row', CFuncDnzKernelRowCol),
    ('dnz_kernel_col', CFuncDnzKernelRowCol),
    ('fundamental_row', CFuncFundamentalRowCol),
    ('fundamental_col', CFuncFundamentalRowCol),
    ('dnz_fundamental_row', CFuncDnzFundamentalRowCol),
    ('dnz_fundamental_col', CFuncDnzFundamentalRowCol),
    ('lagrange_row', CFuncLagrangeRowCol),
    ('lagrange_wave_row', CFuncLagrangeWaveRowCol),
    ('lagrange_col', CFuncLagrangeRowCol),
    ('lagrange_wave_col', CFuncLagrangeWaveRowCol)
]

CStructListNode._fields_ = [
    ('data', c_uint),
    ('next', PTR(CStructListNode))
]

CStructTriList._fields_ = [
    ('t', c_uint),
    ('vl', PTR(CStructVertList)),
    ('next', PTR(CStructTriList))
]

CStructVertList._fields_ = [
    ('v', c_uint),
    ('next', PTR(CStructVertList))
]

CStructAprxBem3d._fields_ = [
    ('m_inter', c_uint),
    ('x_inter', PTR(real)),
    ('k_inter', c_uint),
    ('l_green', c_uint),
    ('m_green', c_uint),
    ('ml_green', c_uint),
    ('k_green', c_uint),
    ('delta_green', real),
    ('t_green', PTR(real)),
    ('w_green', PTR(real)),
    ('quadpoints', CFuncQuadPoints3d),
    ('grc_green', PTR(CStructGreenCluster3d)),
    ('gcc_green', PTR(CStructGreenCluster3d)),
    ('grb_green', PTR(CStructGreenClusterBasis3d)),
    ('gcb_green', PTR(CStructGreenClusterBasis3d)),
    ('accur_aca', real),
    ('recomp', c_bool),
    ('accur_recomp', real),
    ('coarsen', c_bool),
    ('accur_coarsen', real),
    ('hiercomp', c_bool),
    ('accur_hiercomp', real),
    ('tm', PTR(CStructTruncmode))
]

CStructParBem3d._fields_ = [
    ('hn', PTR(PTR(CStructHMatrix))),
    ('h2n', PTR(PTR(CStructH2Matrix))),
    ('dh2n', PTR(PTR(CStructDH2Matrix))),
    ('rbn', PTR(PTR(CStructClusterBasis))),
    ('cbn', PTR(PTR(CStructClusterBasis))),
    ('drbn', PTR(PTR(CStructDClusterBasis))),
    ('dcbn', PTR(PTR(CStructDClusterBasis))),
    ('rwn', PTR(PTR(CStructClusterOperator))),
    ('cwn', PTR(PTR(CStructClusterOperator))),
    ('ron', PTR(PTR(CStructDClusterOperator))),
    ('con', PTR(PTR(CStructDClusterOperator))),
    ('leveln', PTR(c_uint)),
    ('grcn', PTR(PTR(CStructGreenCluster3d))),
    ('grcnn', c_uint),
    ('gccn', PTR(PTR(CStructGreenCluster3d))),
    ('gccnn', c_uint),
    ('grbn', PTR(PTR(CStructGreenClusterBasis3d))),
    ('grbnn', c_uint),
    ('gcbn', PTR(PTR(CStructGreenClusterBasis3d))),
    ('gcbnn', c_uint),
]

CStructGreenCluster3d._fields_ = [
    ('xi', PTR(c_uint)),
    ('xihat', PTR(c_uint)),
    ('V', PTR(CStructAMatrix)),
    ('t', PTR(CStructCluster)),
    ('sons', c_uint)
]

CStructGreenClusterBasis3d._fields_ = [
    ('xi', PTR(c_uint)),
    ('xihat', PTR(c_uint)),
    ('Qinv', PTR(CStructAMatrix)),
    ('cb', PTR(CStructClusterBasis)),
    ('sons', c_uint),
    ('m', c_uint)
]

CStructAdmisBlock._fields_ = [
    ('name', c_uint),
    ('rname', c_uint),
    ('cname', c_uint),
    ('father', c_uint),
    ('son', c_uint),
    ('length', c_uint),
    ('next', PTR(CStructAdmisBlock))
]

CStructCompData._fields_ = [
    ('nco', PTR(PTR(CStructDClusterOperator))),
    ('nro', PTR(PTR(CStructDClusterOperator))),
    ('noro', PTR(PTR(CStructDClusterOperator))),
    ('noco', PTR(PTR(CStructDClusterOperator))),
    ('ncb', PTR(PTR(CStructDClusterBasis))),
    ('nrb', PTR(PTR(CStructDClusterBasis))),
    ('nb', PTR(PTR(CStructDBlock))),
    ('bem', PTR(CStructBem3d)),
    ('rows', c_bool),
    ('cblock', PTR(PTR(CStructAdmisBlock))),
    ('rblock', PTR(PTR(CStructAdmisBlock))),
]


# ------------------------------------


new_vert_list = get_func('new_vert_list', PTR(CStructVertList), [PTR(CStructVertList)])
del_vert_list = get_func('del_vert_list', None, [PTR(CStructVertList)])
new_tri_list = get_func('new_tri_list', PTR(CStructTriList), [PTR(CStructTriList)])
del_tri_list = get_func('del_tri_list', None, [PTR(CStructTriList)])
new_bem3d = get_func('new_bem3d', PTR(CStructBem3d), [PTR(CStructSurface3d), CEnumBasisFunctionBem3d, CEnumBasisFunctionBem3d])
del_bem3d = get_func('del_bem3d', None, [PTR(CStructBem3d)])

build_bem3d_const_clustergeometry = get_func('build_bem3d_const_clustergeometry', PTR(CStructClusterGeometry), [PTR(CStructBem3d), PTR(PTR(c_uint))])
build_bem3d_linear_clustergeometry = get_func('build_bem3d_linear_clustergeometry', PTR(CStructClusterGeometry), [PTR(CStructBem3d), PTR(PTR(c_uint))])
build_bem3d_clustergeometry = get_func('build_bem3d_clustergeometry', PTR(CStructClusterGeometry), [PTR(CStructBem3d), PTR(PTR(c_uint)), CEnumBasisFunctionBem3d])
build_bem3d_cluster = get_func('build_bem3d_cluster', PTR(CStructCluster), [PTR(CStructBem3d), c_uint, CEnumBasisFunctionBem3d])

assemble_cc_near_bem3d = get_func('assemble_cc_near_bem3d', None, [PTR(c_uint), PTR(c_uint), PTR(CStructBem3d), c_bool, PTR(CStructAMatrix), CFuncKernelFunc3d])
# assemble_cc_simd_near_bem3d
assemble_cc_far_bem3d = get_func('assemble_cc_far_bem3d', None, [PTR(c_uint), PTR(c_uint), PTR(CStructBem3d), c_bool, PTR(CStructAMatrix), CFuncKernelFunc3d])
# assemble_cc_simd_far_bem3d
assemble_cl_near_bem3d = get_func('assemble_cl_near_bem3d', None, [PTR(c_uint), PTR(c_uint), PTR(CStructBem3d), c_bool, PTR(CStructAMatrix), CFuncKernelFunc3d])
# assemble_cl_simd_near_bem3d
assemble_cl_far_bem3d = get_func('assemble_cl_far_bem3d', None, [PTR(c_uint), PTR(c_uint), PTR(CStructBem3d), c_bool, PTR(CStructAMatrix), CFuncKernelFunc3d])
# assemble_cl_simd_far_bem3d
assemble_lc_near_bem3d = get_func('assemble_lc_near_bem3d', None, [PTR(c_uint), PTR(c_uint), PTR(CStructBem3d), c_bool, PTR(CStructAMatrix), CFuncKernelFunc3d])
# assemble_lc_simd_near_bem3d
assemble_lc_far_bem3d = get_func('assemble_lc_far_bem3d', None, [PTR(c_uint), PTR(c_uint), PTR(CStructBem3d), c_bool, PTR(CStructAMatrix), CFuncKernelFunc3d])
# assemble_lc_simd_far_bem3d
assemble_ll_near_bem3d = get_func('assemble_ll_near_bem3d', None, [PTR(c_uint), PTR(c_uint), PTR(CStructBem3d), c_bool, PTR(CStructAMatrix), CFuncKernelFunc3d])
# assemble_ll_simd_near_bem3d
assemble_ll_far_bem3d = get_func('assemble_ll_far_bem3d', None, [PTR(c_uint), PTR(c_uint), PTR(CStructBem3d), c_bool, PTR(CStructAMatrix), CFuncKernelFunc3d])
# assemble_ll_simd_far_bem3d

fill_bem3d = get_func('fill_bem3d', None, [PTR(CStructBem3d), PTR(real * 3), PTR(real * 3), PTR(real * 3), PTR(real * 3), PTR(CStructAMatrix), CFuncKernelFunc3d])
fill_wave_bem3d = get_func('fill_wave_bem3d', None, [PTR(CStructBem3d), PTR(real * 3), PTR(real * 3), PTR(real * 3), PTR(real * 3), PTR(CStructAMatrix), PTR(real), CFuncKernelWaveFunc3d])
fill_row_c_bem3d = get_func('fill_row_c_bem3d', None, [PTR(c_uint), PTR(real * 3), PTR(CStructBem3d), PTR(CStructAMatrix), CFuncKernelFunc3d])
# fill_row_simd_c_bem3d
fill_col_c_bem3d = get_func('fill_col_c_bem3d', None, [PTR(c_uint), PTR(real * 3), PTR(CStructBem3d), PTR(CStructAMatrix), CFuncKernelFunc3d])
# fill_col_simd_c_bem3d
fill_row_l_bem3d = get_func('fill_row_l_bem3d', None, [PTR(c_uint), PTR(real * 3), PTR(CStructBem3d), PTR(CStructAMatrix), CFuncKernelFunc3d])
fill_col_l_bem3d = get_func('fill_col_l_bem3d', None, [PTR(c_uint), PTR(real * 3), PTR(CStructBem3d), PTR(CStructAMatrix), CFuncKernelFunc3d])
fill_dnz_row_c_bem3d = get_func('fill_dnz_row_c_bem3d', None, [PTR(c_uint), PTR(real * 3), PTR(real * 3), PTR(CStructBem3d), PTR(CStructAMatrix), CFuncKernelFunc3d])
# fill_dnz_row_simd_c_bem3d
fill_dnz_col_c_bem3d = get_func('fill_dnz_col_c_bem3d', None, [PTR(c_uint), PTR(real * 3), PTR(real * 3), PTR(CStructBem3d), PTR(CStructAMatrix), CFuncKernelFunc3d])
# fill_dnz_col_simd_c_bem3d
fill_dnz_row_l_bem3d = get_func('fill_dnz_row_l_bem3d', None, [PTR(c_uint), PTR(real * 3), PTR(real * 3), PTR(CStructBem3d), PTR(CStructAMatrix), CFuncKernelFunc3d])
fill_dnz_col_l_bem3d = get_func('fill_dnz_col_l_bem3d', None, [PTR(c_uint), PTR(real * 3), PTR(real * 3), PTR(CStructBem3d), PTR(CStructAMatrix), CFuncKernelFunc3d])

setup_hmatrix_recomp_bem3d = get_func('setup_hmatrix_recomp_bem3d', None, [PTR(CStructBem3d), c_bool, real, c_bool, real])
setup_hmatrix_aprx_inter_row_bem3d = get_func('setup_hmatrix_aprx_inter_row_bem3d', None, [PTR(CStructBem3d), PTR(CStructCluster), PTR(CStructCluster), PTR(CStructBlock), c_uint])
setup_hmatrix_aprx_inter_col_bem3d = get_func('setup_hmatrix_aprx_inter_col_bem3d', None, [PTR(CStructBem3d), PTR(CStructCluster), PTR(CStructCluster), PTR(CStructBlock), c_uint])
setup_hmatrix_aprx_inter_mixed_bem3d = get_func('setup_hmatrix_aprx_inter_mixed_bem3d', None, [PTR(CStructBem3d), PTR(CStructCluster), PTR(CStructCluster), PTR(CStructBlock), c_uint])
setup_hmatrix_aprx_green_row_bem3d = get_func('setup_hmatrix_aprx_green_row_bem3d', None, [PTR(CStructBem3d), PTR(CStructCluster), PTR(CStructCluster), PTR(CStructBlock), c_uint, c_uint, real, CFuncQuadPoints3d])
setup_hmatrix_aprx_green_col_bem3d = get_func('setup_hmatrix_aprx_green_col_bem3d', None, [PTR(CStructBem3d), PTR(CStructCluster), PTR(CStructCluster), PTR(CStructBlock), c_uint, c_uint, real, CFuncQuadPoints3d])
setup_hmatrix_aprx_green_mixed_bem3d = get_func('setup_hmatrix_aprx_green_mixed_bem3d', None, [PTR(CStructBem3d), PTR(CStructCluster), PTR(CStructCluster), PTR(CStructBlock), c_uint, c_uint, real, CFuncQuadPoints3d])
setup_hmatrix_aprx_greenhybrid_row_bem3d = get_func('setup_hmatrix_aprx_greenhybrid_row_bem3d', None, [PTR(CStructBem3d), PTR(CStructCluster), PTR(CStructCluster), PTR(CStructBlock), c_uint, c_uint, real, real, CFuncQuadPoints3d])
setup_hmatrix_aprx_greenhybrid_col_bem3d = get_func('setup_hmatrix_aprx_greenhybrid_col_bem3d', None, [PTR(CStructBem3d), PTR(CStructCluster), PTR(CStructCluster), PTR(CStructBlock), c_uint, c_uint, real, real, CFuncQuadPoints3d])
setup_hmatrix_aprx_greenhybrid_mixed_bem3d = get_func('setup_hmatrix_aprx_greenhybrid_mixed_bem3d', None, [PTR(CStructBem3d), PTR(CStructCluster), PTR(CStructCluster), PTR(CStructBlock), c_uint, c_uint, real, real, CFuncQuadPoints3d])
setup_hmatrix_aprx_aca_bem3d = get_func('setup_hmatrix_aprx_aca_bem3d', None, [PTR(CStructBem3d), PTR(CStructCluster), PTR(CStructCluster), PTR(CStructBlock), real])
setup_hmatrix_aprx_paca_bem3d = get_func('setup_hmatrix_aprx_paca_bem3d', None, [PTR(CStructBem3d), PTR(CStructCluster), PTR(CStructCluster), PTR(CStructBlock), real])
setup_hmatrix_aprx_hca_bem3d = get_func('setup_hmatrix_aprx_hca_bem3d', None, [PTR(CStructBem3d), PTR(CStructCluster), PTR(CStructCluster), PTR(CStructBlock), c_uint, real])
setup_h2matrix_recomp_bem3d = get_func('setup_h2matrix_recomp_bem3d', None, [PTR(CStructBem3d), c_bool, real])
setup_h2matrix_aprx_inter_bem3d = get_func('setup_h2matrix_aprx_inter_bem3d', None, [PTR(CStructBem3d), PTR(CStructClusterBasis), PTR(CStructClusterBasis), PTR(CStructBlock), c_uint])
setup_h2matrix_aprx_greenhybrid_bem3d = get_func('setup_h2matrix_aprx_greenhybrid_bem3d', None, [PTR(CStructBem3d), PTR(CStructClusterBasis), PTR(CStructClusterBasis), PTR(CStructBlock), c_uint, c_uint, real, real, CFuncQuadPoints3d])
setup_h2matrix_aprx_greenhybrid_ortho_bem3d = get_func('setup_h2matrix_aprx_greenhybrid_ortho_bem3d', None, [PTR(CStructBem3d), PTR(CStructClusterBasis), PTR(CStructClusterBasis), PTR(CStructBlock), c_uint, c_uint, real, real, CFuncQuadPoints3d])
setup_dh2matrix_aprx_inter_bem3d = get_func('setup_dh2matrix_aprx_inter_bem3d', None, [PTR(CStructBem3d), PTR(CStructDClusterBasis), PTR(CStructDClusterBasis), PTR(CStructDBlock), c_uint])
setup_dh2matrix_aprx_inter_ortho_bem3d = get_func('setup_dh2matrix_aprx_inter_ortho_bem3d', None, [PTR(CStructBem3d), PTR(CStructDClusterBasis), PTR(CStructDClusterBasis), PTR(CStructDBlock), c_uint])
setup_dh2matrix_aprx_inter_recomp_bem3d = get_func('setup_dh2matrix_aprx_inter_recomp_bem3d', None, [PTR(CStructBem3d), PTR(CStructDClusterBasis), PTR(CStructDClusterBasis), PTR(CStructDBlock), c_uint, PTR(CStructTruncmode), real])

assemble_bem3d_amatrix = get_func('assemble_bem3d_amatrix', None, [PTR(CStructBem3d), PTR(CStructAMatrix)])
assemble_bem3d_hmatrix = get_func('assemble_bem3d_hmatrix', None, [PTR(CStructBem3d), PTR(CStructBlock), PTR(CStructHMatrix)])
assemblecoarsen_bem3d_hmatrix = get_func('assemblecoarsen_bem3d_hmatrix', None, [PTR(CStructBem3d), PTR(CStructBlock), PTR(CStructHMatrix)])
assemble_bem3d_nearfield_hmatrix = get_func('assemble_bem3d_nearfield_hmatrix', None, [PTR(CStructBem3d), PTR(CStructBlock), PTR(CStructHMatrix)])
assemble_bem3d_farfield_hmatrix = get_func('assemble_bem3d_farfield_hmatrix', None, [PTR(CStructBem3d), PTR(CStructBlock), PTR(CStructHMatrix)])
assemble_bem3d_h2matrix_row_clusterbasis = get_func('assemble_bem3d_h2matrix_row_clusterbasis', None, [PTR(CStructBem3d), PTR(CStructClusterBasis)])
assemble_bem3d_h2matrix_col_clusterbasis = get_func('assemble_bem3d_h2matrix_col_clusterbasis', None, [PTR(CStructBem3d), PTR(CStructClusterBasis)])
assemble_bem3d_h2matrix = get_func('assemble_bem3d_h2matrix', None, [PTR(CStructBem3d), PTR(CStructH2Matrix)])
assemble_bem3d_nearfield_h2matrix = get_func('assemble_bem3d_nearfield_h2matrix', None, [PTR(CStructBem3d), PTR(CStructH2Matrix)])
assemble_bem3d_farfield_h2matrix = get_func('assemble_bem3d_farfield_h2matrix', None, [PTR(CStructBem3d), PTR(CStructH2Matrix)])
assemblehiercomp_bem3d_h2matrix = get_func('assemblehiercomp_bem3d_h2matrix', None, [PTR(CStructBem3d), PTR(CStructBlock), PTR(CStructH2Matrix)])
assemble_bem3d_dh2matrix_row_dclusterbasis = get_func('assemble_bem3d_dh2matrix_row_dclusterbasis', None, [PTR(CStructBem3d), PTR(CStructDClusterBasis)])
assemble_bem3d_dh2matrix_col_dclusterbasis = get_func('assemble_bem3d_dh2matrix_col_dclusterbasis', None, [PTR(CStructBem3d), PTR(CStructDClusterBasis)])
assemble_bem3d_dh2matrix_ortho_row_dclusterbasis = get_func('assemble_bem3d_dh2matrix_ortho_row_dclusterbasis', None, [PTR(CStructBem3d), PTR(CStructDClusterBasis), PTR(CStructDClusterOperator)])
assemble_bem3d_dh2matrix_ortho_col_dclusterbasis = get_func('assemble_bem3d_dh2matrix_ortho_col_dclusterbasis', None, [PTR(CStructBem3d), PTR(CStructDClusterBasis), PTR(CStructDClusterOperator)])
assemble_bem3d_dh2matrix_recomp_both_dclusterbasis = get_func('assemble_bem3d_dh2matrix_recomp_both_dclusterbasis', None, [PTR(CStructBem3d), PTR(CStructDClusterBasis), PTR(CStructDClusterOperator), PTR(CStructDClusterBasis), PTR(CStructDClusterOperator), PTR(CStructDBlock)])
assemble_bem3d_dh2matrix = get_func('assemble_bem3d_dh2matrix', None, [PTR(CStructBem3d), PTR(CStructDH2Matrix)])
assemble_bem3d_nearfield_dh2matrix = get_func('assemble_bem3d_nearfield_dh2matrix', None, [PTR(CStructBem3d), PTR(CStructDH2Matrix)])
assemble_bem3d_farfield_dh2matrix = get_func('assemble_bem3d_farfield_dh2matrix', None, [PTR(CStructBem3d), PTR(CStructDH2Matrix)])
assemble_bem3d_lagrange_c_amatrix = get_func('assemble_bem3d_lagrange_c_amatrix', None, [PTR(c_uint), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructBem3d), PTR(CStructAMatrix)])
assemble_bem3d_lagrange_wave_c_amatrix = get_func('assemble_bem3d_lagrange_wave_c_amatrix', None, [PTR(c_uint), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(real), PTR(CStructBem3d), PTR(CStructAMatrix)])
assemble_bem3d_lagrange_l_amatrix = get_func('assemble_bem3d_lagrange_l_amatrix', None, [PTR(c_uint), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructBem3d), PTR(CStructAMatrix)])
assemble_bem3d_lagrange_wave_l_amatrix = get_func('assemble_bem3d_lagrange_wave_l_amatrix', None, [PTR(c_uint), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(real), PTR(CStructBem3d), PTR(CStructAMatrix)])
assemble_bem3d_dn_lagrange_c_amatrix = get_func('assemble_bem3d_dn_lagrange_c_amatrix', None, [PTR(c_uint), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructBem3d), PTR(CStructAMatrix)])
assemble_bem3d_dn_lagrange_wave_c_amatrix = get_func('assemble_bem3d_dn_lagrange_wave_c_amatrix', None, [PTR(c_uint), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(real), PTR(CStructBem3d), PTR(CStructAMatrix)])
assemble_bem3d_dn_lagrange_l_amatrix = get_func('assemble_bem3d_dn_lagrange_l_amatrix', None, [PTR(c_uint), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructBem3d), PTR(CStructAMatrix)])
assemble_bem3d_dn_lagrange_wave_l_amatrix = get_func('assemble_bem3d_dn_lagrange_wave_l_amatrix', None, [PTR(c_uint), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(real), PTR(CStructBem3d), PTR(CStructAMatrix)])
assemble_bem3d_lagrange_amatrix = get_func('assemble_bem3d_lagrange_amatrix', None, [PTR(real * 3), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructBem3d), PTR(CStructAMatrix)])
assemble_bem3d_lagrange_wave_amatrix = get_func('assemble_bem3d_lagrange_wave_amatrix', None, [PTR(real * 3), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(CStructRealAVector), PTR(real), PTR(CStructBem3d), PTR(CStructAMatrix)])

normL2_bem3d = get_func('normL2_bem3d', real, [PTR(CStructBem3d), CFuncBoundaryFunc3d, c_void_p])
normL2_c_bem3d = get_func('normL2_c_bem3d', real, [PTR(CStructBem3d), PTR(CStructAVector)])
normL2diff_c_bem3d = get_func('normL2diff_c_bem3d', real, [PTR(CStructBem3d), PTR(CStructAVector), CFuncBoundaryFunc3d, c_void_p])
normL2_l_bem3d = get_func('normL2_l_bem3d', real, [PTR(CStructBem3d), PTR(CStructAVector)])
normL2diff_l_bem3d = get_func('normL2diff_l_bem3d', real, [PTR(CStructBem3d), PTR(CStructAVector), CFuncBoundaryFunc3d, c_void_p])
integrate_bem3d_c_avector = get_func('integrate_bem3d_c_avector', None, [PTR(CStructBem3d), CFuncBoundaryFunc3d, PTR(CStructAVector), c_void_p])
integrate_bem3d_l_avector = get_func('integrate_bem3d_l_avector', None, [PTR(CStructBem3d), CFuncBoundaryFunc3d, PTR(CStructAVector), c_void_p])
projectL2_bem3d_c_avector = get_func('projectL2_bem3d_c_avector', None, [PTR(CStructBem3d), CFuncBoundaryFunc3d, PTR(CStructAVector), c_void_p])
projectL2_bem3d_l_avector = get_func('projectL2_bem3d_l_avector', None, [PTR(CStructBem3d), CFuncBoundaryFunc3d, PTR(CStructAVector), c_void_p])
setup_vertex_to_triangle_map_bem3d = get_func('setup_vertex_to_triangle_map_bem3d', None, [PTR(CStructBem3d)])
build_bem3d_cube_quadpoints = get_func('build_bem3d_cube_quadpoints', None, [PTR(CStructBem3d), real*3, real*3, real, PTR(PTR(real*3)), PTR(PTR(real*3))])
build_bem3d_rkmatrix = get_func('build_bem3d_rkmatrix', PTR(CStructRkMatrix), [PTR(CStructCluster), PTR(CStructCluster), c_void_p])
build_bem3d_amatrix = get_func('build_bem3d_amatrix', PTR(CStructAMatrix), [PTR(CStructCluster), PTR(CStructCluster), c_void_p])
build_bem3d_curl_sparsematrix = get_func('build_bem3d_curl_sparsematrix', None, [PTR(CStructBem3d), PTR(PTR(CStructSparseMatrix)), PTR(PTR(CStructSparseMatrix)), PTR(PTR(CStructSparseMatrix))])
