from h2libpy.data.vector.avector import AVector
import ctypes


vec = AVector(4)
vec.rand()
print(vec.norm())
print(vec.dim)
print(vec.v[0:4])