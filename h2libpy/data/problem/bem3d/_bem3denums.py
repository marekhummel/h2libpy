from enum import Enum
from h2libpy.lib.bem3d import CEnumBasisFunctionBem3d


class BasisFunction(Enum):
    Dummy = CEnumBasisFunctionBem3d.BASIS_NONE_BEM3D
    Constant = CEnumBasisFunctionBem3d.BASIS_CONSTANT_BEM3D
    Linear = CEnumBasisFunctionBem3d.BASIS_LINEAR_BEM3D
