from ctypes import Structure as Struct
from ctypes import c_uint


class CStructAVector(Struct): pass
class CStructAMatrix(Struct): pass

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

class CStructBlock(Struct): pass
class CStructBlockEntry(Struct): pass
class CEnumClusterMode(c_uint): pass
class CStructCluster(Struct): pass
class CStructClusterBasis(Struct): pass
class CStructClusterGeometry(Struct): pass
class CStructClusterOperator(Struct): pass

class CStructDBlock(Struct): pass
class CStructDCluster(Struct): pass
class CStructLevelDir(Struct): pass
class CStructDClusterBasis(Struct): pass
class CStructDClusterOperator(Struct): pass

class CStructDUniform(Struct): pass
class CStructDH2Matrix(Struct): pass
class CStructH2Matrix(Struct): pass
class CStructH2MatrixList(Struct): pass
class CStructHMatrix(Struct): pass

class CStructMacroSurface3d(Struct): pass

class CStructRealAVector(Struct): pass
class CStructRkMatrix(Struct): pass
class CStructSingQuad2d(Struct): pass

class CStructSparseMatrix(Struct): pass
class CStructSparsePattern(Struct): pass
class CStructPatEntry(Struct): pass

class CStructSurface3d(Struct): pass
class CStructTruncMode(Struct): pass
class CStructUniform(Struct): pass
