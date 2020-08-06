from h2libpy.data.matrix import AMatrix, HMatrix
from h2libpy.data.matrix.enums import NormType, FillType, ClearType
from h2libpy.data.vector import AVector


a = AMatrix.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
print(a)
b = AMatrix.from_list([2, 3, 4, -4, -2, 3, 9, -8, 2], 3, 3)
print(b)
print(a[2][2])
