from ctypes import Structure as Struct
from ctypes import c_uint


class CEnumBasisFunctionBem3d(c_uint):
    BASIS_NONE_BEM3D: 'CEnumBasisFunctionBem3d'
    BASIS_CONSTANT_BEM3D: 'CEnumBasisFunctionBem3d'
    BASIS_LINEAR_BEM3D: 'CEnumBasisFunctionBem3d'

class CEnumClusterMode(c_uint):
    H2_ADAPTIVE: 'CEnumClusterMode'
    H2_REGULAR: 'CEnumClusterMode'
    H2_SIMSUB: 'CEnumClusterMode'
    H2_PCA: 'CEnumClusterMode'


class CStructAdmisBlock(Struct): pass
class CStructAMatrix(Struct): pass
class CStructAprxBem3d(Struct): pass
class CStructAVector(Struct): pass
class CStructBem3d(Struct): pass
class CStructBlock(Struct): pass
class CStructBlockEntry(Struct): pass
class CStructCluster(Struct): pass
class CStructClusterBasis(Struct): pass
class CStructClusterGeometry(Struct): pass
class CStructClusterOperator(Struct): pass
class CStructCompData(Struct): pass
class CStructDBlock(Struct): pass
class CStructDCluster(Struct): pass
class CStructDClusterBasis(Struct): pass
class CStructDClusterOperator(Struct): pass
class CStructDH2Matrix(Struct): pass
class CStructDUniform(Struct): pass
class CStructGreenCluster3d(Struct): pass
class CStructGreenClusterBasis3d(Struct): pass
class CStructH2Matrix(Struct): pass
class CStructH2MatrixList(Struct): pass
class CStructHMatrix(Struct): pass
class CStructKernelBem3d(Struct): pass
class CStructLevelDir(Struct): pass
class CStructListNode(Struct): pass
class CStructMacroSurface3d(Struct): pass
class CStructParBem3d(Struct): pass
class CStructPatEntry(Struct): pass
class CStructRealAVector(Struct): pass
class CStructRkMatrix(Struct): pass
class CStructSingQuad2d(Struct): pass
class CStructSparseMatrix(Struct): pass
class CStructSparsePattern(Struct): pass
class CStructSurface3d(Struct): pass
class CStructTriList(Struct): pass
class CStructTruncMode(Struct): pass
class CStructUniform(Struct): pass
class CStructVertList(Struct): pass

# class CStructCopyNearData(Struct): pass
# class CStructAddevalBlock(Struct): pass
# class CStructAddevalData(Struct): pass
# class CStructExpandData(Struct): pass
# class CStructOrthoData(Struct): pass
# class CStructAddevalData(Struct): pass
# class CStructDirAdmData(Struct): pass
