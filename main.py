from h2libpy.data.matrix.amatrix import AMatrix, NormType, FillType, ClearType
from h2libpy.data.vector.avector import AVector
from h2libpy.data.matrix.hmatrix import HMatrix


a = AMatrix.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
print(a)
b = AMatrix.from_list([2, 3, 4, -4, -2, 3, 9, -8, 2], 3, 3)
print(b)
print(a[2][2])
