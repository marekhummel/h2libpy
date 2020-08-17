from h2libpy.data.matrix import AMatrix, HMatrix, NormType, FillType, ClearType
from h2libpy.data.vector import AVector, RealAVector
from h2libpy.lib.amatrix import del_amatrix
from h2libpy.data.geometry import MacroSurface3d, Surface3d
from h2libpy.lib.surface3d import del_surface3d
from ctypes import pointer


# a = AMatrix.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
# del_amatrix(a)
# print(a.a)
# print(a.cobj())
# # del_amatrix(a) 

# from h2libpy.lib.util.helper import get_func
# x = get_func('INTERPOLATION_EPS_BEM3D', None, None)
# print(x)

v = RealAVector.from_list([1,2,3,4,5])
v.v3 = [2,3,5]
print(v)
print(v.v)
print(v.v3)

x = pointer(v.cobj())