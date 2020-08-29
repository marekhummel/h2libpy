from h2libpy.data.matrix import AMatrix, HMatrix, NormType, FillType, ClearType
from h2libpy.data.vector import AVector, RealAVector
from h2libpy.data.geometry import MacroSurface3d, Surface3d
from h2libpy.lib.surface3d import del_surface3d
from ctypes import pointer


a = AMatrix.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 4, 3)
a.print()
print(a.a)

b = AMatrix.from_submatrix(a, 3, 3, 1, 0)
b.print()
print(b.a)