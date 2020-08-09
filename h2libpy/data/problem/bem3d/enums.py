from enum import Enum


class QuadratureType(Enum):
    CCNear = 0
    CCFar = 1
    CLNear = 2
    CLFar = 3
    LCNear = 4
    LCFar = 5
    LLNear = 6
    LLFar = 7


class IntegralType(Enum):
    RowC = 0
    ColC = 1
    RowL = 2
    ColL = 3


class InterpolationDirection(Enum):
    Row = 0
    Col = 1
    Mixed = 2


class LagrangeType(Enum):
    Const = 0,
    Linear = 1,
    DnConst = 2,
    DnLinear = 3
