from enum import Enum


class FillType(Enum):
    Nothing = 0
    Zeros = 1
    Identity = 2


class ClearType(Enum):
    All = 0
    Lower = 1
    LowerStrict = 2
    Upper = 3
    UpperStrict = 4


class NormType(Enum):
    Spectral = 0
    Frobenius = 1
    SquaredFrobenius = 2
