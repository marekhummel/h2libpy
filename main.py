from h2libpy.data.vector.avector import AVector

vec = AVector.new(4)
vec.rand()
print(vec.norm())
print(vec.dim())
print(vec.values())
