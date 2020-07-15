from h2libpy.data.vector.avector import AVector

vec = AVector(5)
vec.rand()
vec.print()
print(vec.norm())
print(vec.get_dim())
