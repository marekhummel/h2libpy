from h2libpy.data.matrix import AMatrix, HMatrix
from h2libpy.data.matrix.enums import NormType, FillType, ClearType
from h2libpy.data.vector import AVector
from h2libpy.lib.amatrix import del_amatrix
from h2libpy.data.geometry import MacroSurface3d, Surface3d
from h2libpy.lib.surface3d import del_surface3d


# a = AMatrix.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)
# del_amatrix(a)
# print(a.a)
# print(a.cobj())
# # del_amatrix(a) 

mg = MacroSurface3d.new_sphere()
gr = Surface3d.from_macrosurface3d(mg, 8)
del_surface3d(gr)
print(gr.cobj() is None)
try:
    del_surface3d(gr)
except e:
    pass