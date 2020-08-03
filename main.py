from h2libpy.data.matrix.amatrix import AMatrix, NormType, FillType, ClearType
from h2libpy.data.vector.avector import AVector


a = AMatrix.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
# print(a.a)
# a.print()
b = AMatrix.from_submatrix(a, 2, 3, 1, 0)
print(b.a)
b.print()
# print(b.ld)