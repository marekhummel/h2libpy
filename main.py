from h2libpy.data.vector.avector import AVector
from h2libpy.lib.amatrix import LibAVector


x = LibAVector()

vec = AVector.new(4)
vec.rand()
print(vec.norm())
print(vec.dim())
print(vec.values())
