from h2libpy.data.vector.avector import AVector


v = AVector.from_list([1, 2, 3])
print(v.v)

v2 = AVector.from_list([5, 6, 7])
v.copy(v2)
v2.scale(3)
print(v2.v)

v3 = v - v2
print(v3.v)
# print(v3.v)
# print(v3[0], v3[1], v3[2])
v4 = -v
print(v4.v)

print(v)