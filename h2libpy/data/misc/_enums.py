from enum import Enum


class TruncModeInit(Enum):
    Nothing = 0
    RelEucl = 1
    RelFrob = 2
    BlockRelEucl = 3
    BlockRelFrob = 4
    AbsEucl = 5
