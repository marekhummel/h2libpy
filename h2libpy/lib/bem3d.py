from ctypes import CFUNCTYPE
from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_bool, c_uint, c_void_p

from h2libpy.lib.util.helper import get_func
from h2libpy.lib.amatrix import CStructAMatrix
from h2libpy.lib.avector import CStructAVector
from h2libpy.lib.cluster import CStructCluster
from h2libpy.lib.clusterbasis import CStructClusterBasis
from h2libpy.lib.clusteroperator import CStructClusterOperator
from h2libpy.lib.dblock import CStructDBlock
from h2libpy.lib.dclusterbasis import CStructDClusterBasis
from h2libpy.lib.dclusteroperator import CStructDClusterOperator
from h2libpy.lib.dh2matrix import CStructDH2Matrix
from h2libpy.lib.h2matrix import CStructH2Matrix
from h2libpy.lib.hmatrix import CStructHMatrix
from h2libpy.lib.settings import field, real
from h2libpy.lib.singquad2d import CStructSingquad2d
from h2libpy.lib.surface3d import CStructSurface3d
from h2libpy.lib.truncation import CStructTruncmode

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


CFuncQuadPoints3d = CFUNCTYPE(None, *[PTR(CStructBem3d), real*3, real*3, real, PTR(PTR(real))*3, PTR(PTR(real))*3])

CFuncBoundaryFunc3d = CFUNCTYPE(field, *[PTR(real), PTR(real), c_void_p])


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
    ('aprx', PTR(CStructAprxBem3d)),
    ('par', PTR(CStructParBem3d)),
    ('kernels', PTR(CStructKernelBem3d)),
]

CStructKernelBem3d._fields_ = []

CStructVertList._fields_ = [
    ('v', c_uint),
    ('next', PTR(CStructVertList))
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


CEnumBasisFunctionBem3d.BASIS_NONE_BEM3D = CEnumBasisFunctionBem3d(0)
CEnumBasisFunctionBem3d.BASIS_CONSTANT_BEM3D = CEnumBasisFunctionBem3d(ord('c'))
CEnumBasisFunctionBem3d.BASIS_LINEAR_BEM3D = CEnumBasisFunctionBem3d(ord('l'))

# ------------------------------------


assemble_bem3d_amatrix = get_func('assemble_bem3d_amatrix', None, [PTR(CStructBem3d), PTR(CStructAMatrix)])
projectL2_bem3d_c_avector = get_func('projectL2_bem3d_c_avector', None, [PTR(CStructBem3d), PTR(CFuncBoundaryFunc3d), PTR(CStructAVector), c_void_p])
normL2diff_c_bem3d = get_func('normL2diff_c_bem3d', real, [PTR(CStructBem3d), PTR(CStructAVector), CFuncBoundaryFunc3d, c_void_p])
normL2_bem3d = get_func('normL2_bem3d', real, [PTR(CStructBem3d), CFuncBoundaryFunc3d, c_void_p])
del_bem3d = get_func('del_bem3d', None, [PTR(CStructBem3d)])
projectL2_bem3d_c_avector = get_func('projectL2_bem3d_c_avector', None, [PTR(CStructBem3d), CFuncBoundaryFunc3d, PTR(CStructAVector), c_void_p])
