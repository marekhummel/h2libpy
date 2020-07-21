from h2libpy.data.vector.avector import AVector

vec = AVector.new(4)
vec.rand()
vec.norm()
# vec.dim()
print(vec.dim)
print(vec.v)
# vec.values()

# print(vec.__dict__)