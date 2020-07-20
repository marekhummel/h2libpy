from ctypes import CFUNCTYPE
from ctypes import POINTER as PTR
from ctypes import Structure as Struct
from ctypes import c_bool, c_uint, c_void_p
from enum import IntEnum

from h2libpy.util.helper import get_func
from h2libpy.lib.amatrix import LibAMatrix
from h2libpy.lib.avector import LibAVector
from h2libpy.lib.cluster import LibCluster
from h2libpy.lib.clusterbasis import LibClusterBasis
from h2libpy.lib.clusteroperator import LibClusterOperator
from h2libpy.lib.dblock import LibDBlock
from h2libpy.lib.dclusterbasis import LibDClusterBasis
from h2libpy.lib.dclusteroperator import LibDClusterOperator
from h2libpy.lib.dh2matrix import LibDH2Matrix
from h2libpy.lib.h2matrix import LibH2Matrix
from h2libpy.lib.hmatrix import LibHMatrix
from h2libpy.lib.settings import field, real
from h2libpy.lib.singquad2d import LibSingquad2d
from h2libpy.lib.surface3d import LibSurface3d
from h2libpy.lib.truncation import LibTruncmode

# ------------------------------------


class LibBem3d(Struct): pass
class LibKernelBem3d(Struct): pass
class LibVertList(Struct): pass
class LibListNode(Struct): pass
class LibTriList(Struct): pass
class LibAprxBem3d(Struct): pass
class LibParBem3d(Struct): pass
class LibGreenCluster3d(Struct): pass
class LibGreenClusterBasis3d(Struct): pass
class LibAdmisBlock(Struct): pass
class LibCompData(Struct): pass

class LibBasisFunctionBem3d(c_uint): pass


# ------------------------------------


FuncQuadPoints3d = CFUNCTYPE(None, *[PTR(LibBem3d), real*3, real*3, real, PTR(PTR(real))*3, PTR(PTR(real))*3])

FuncBoundaryFunc3d = CFUNCTYPE(field, *[PTR(real), PTR(real), c_void_p])


# ------------------------------------


LibBem3d._fields_ = [
    ('gr', PTR(LibSurface3d)),
    ('sq', PTR(LibSingquad2d)),
    ('row_basis', LibBasisFunctionBem3d),
    ('col_basis', LibBasisFunctionBem3d),
    ('mass', PTR(real)),
    ('alpha', field),
    ('k', field),
    ('kernel_const', field),
    ('v2t', PTR(PTR(LibListNode))),
    ('aprx', PTR(LibAprxBem3d)),
    ('par', PTR(LibParBem3d)),
    ('kernels', PTR(LibKernelBem3d)),
]

LibKernelBem3d._fields_ = []

LibVertList._fields_ = [
    ('v', c_uint),
    ('next', PTR(LibVertList))
]

LibListNode._fields_ = [
    ('data', c_uint),
    ('next', PTR(LibListNode))
]

LibTriList._fields_ = [
    ('t', c_uint),
    ('vl', PTR(LibVertList)),
    ('next', PTR(LibTriList))
]

LibAprxBem3d._fields_ = [
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
    ('quadpoints', FuncQuadPoints3d),
    ('grc_green', PTR(LibGreenCluster3d)),
    ('gcc_green', PTR(LibGreenCluster3d)),
    ('grb_green', PTR(LibGreenClusterBasis3d)),
    ('gcb_green', PTR(LibGreenClusterBasis3d)),
    ('accur_aca', real),
    ('recomp', c_bool),
    ('accur_recomp', real),
    ('coarsen', c_bool),
    ('accur_coarsen', real),
    ('hiercomp', c_bool),
    ('accur_hiercomp', real),
    ('tm', PTR(LibTruncmode))
]

LibParBem3d._fields_ = [
    ('hn', PTR(PTR(LibHMatrix))),
    ('h2n', PTR(PTR(LibH2Matrix))),
    ('dh2n', PTR(PTR(LibDH2Matrix))),
    ('rbn', PTR(PTR(LibClusterBasis))),
    ('cbn', PTR(PTR(LibClusterBasis))),
    ('drbn', PTR(PTR(LibDClusterBasis))),
    ('dcbn', PTR(PTR(LibDClusterBasis))),
    ('rwn', PTR(PTR(LibClusterOperator))),
    ('cwn', PTR(PTR(LibClusterOperator))),
    ('ron', PTR(PTR(LibDClusterOperator))),
    ('con', PTR(PTR(LibDClusterOperator))),
    ('leveln', PTR(c_uint)),
    ('grcn', PTR(PTR(LibGreenCluster3d))),
    ('grcnn', c_uint),
    ('gccn', PTR(PTR(LibGreenCluster3d))),
    ('gccnn', c_uint),
    ('grbn', PTR(PTR(LibGreenClusterBasis3d))),
    ('grbnn', c_uint),
    ('gcbn', PTR(PTR(LibGreenClusterBasis3d))),
    ('gcbnn', c_uint),
]

LibGreenCluster3d._fields_ = [
    ('xi', PTR(c_uint)),
    ('xihat', PTR(c_uint)),
    ('V', PTR(LibAMatrix)),
    ('t', PTR(LibCluster)),
    ('sons', c_uint)
]

LibGreenClusterBasis3d._fields_ = [
    ('xi', PTR(c_uint)),
    ('xihat', PTR(c_uint)),
    ('Qinv', PTR(LibAMatrix)),
    ('cb', PTR(LibClusterBasis)),
    ('sons', c_uint),
    ('m', c_uint)
]

LibAdmisBlock._fields_ = [
    ('name', c_uint),
    ('rname', c_uint),
    ('cname', c_uint),
    ('father', c_uint),
    ('son', c_uint),
    ('length', c_uint),
    ('next', PTR(LibAdmisBlock))
]

LibCompData._fields_ = [
    ('nco', PTR(PTR(LibDClusterOperator))),
    ('nro', PTR(PTR(LibDClusterOperator))),
    ('noro', PTR(PTR(LibDClusterOperator))),
    ('noco', PTR(PTR(LibDClusterOperator))),
    ('ncb', PTR(PTR(LibDClusterBasis))),
    ('nrb', PTR(PTR(LibDClusterBasis))),
    ('nb', PTR(PTR(LibDBlock))),
    ('bem', PTR(LibBem3d)),
    ('rows', c_bool),
    ('cblock', PTR(PTR(LibAdmisBlock))),
    ('rblock', PTR(PTR(LibAdmisBlock))),
]


LibBasisFunctionBem3d.BASIS_NONE_BEM3D = LibBasisFunctionBem3d(0)
LibBasisFunctionBem3d.BASIS_CONSTANT_BEM3D = LibBasisFunctionBem3d(ord('c'))
LibBasisFunctionBem3d.BASIS_LINEAR_BEM3D = LibBasisFunctionBem3d(ord('l'))

# ------------------------------------


assemble_bem3d_amatrix = get_func('assemble_bem3d_amatrix', None, [PTR(LibBem3d), PTR(LibAMatrix)])
projectL2_bem3d_c_avector = get_func('projectL2_bem3d_c_avector', None, [PTR(LibBem3d), PTR(FuncBoundaryFunc3d), PTR(LibAVector), c_void_p])
normL2diff_c_bem3d = get_func('normL2diff_c_bem3d', real, [PTR(LibBem3d), PTR(LibAVector), FuncBoundaryFunc3d, c_void_p])
normL2_bem3d = get_func('normL2_bem3d', real, [PTR(LibBem3d), FuncBoundaryFunc3d, c_void_p])
del_bem3d = get_func('del_bem3d', None, [PTR(LibBem3d)])
projectL2_bem3d_c_avector = get_func('projectL2_bem3d_c_avector', None, [PTR(LibBem3d), FuncBoundaryFunc3d, PTR(LibAVector), c_void_p])