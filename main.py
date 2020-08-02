import ctypes


# class CStructVector(ctypes.Structure):
#     _fields_ = [
#         ('v', ctypes.POINTER(ctypes.c_double)),
#         ('dim', ctypes.c_uint),
#         ('owner', ctypes.c_void_p)
#     ]


# lib = ctypes.CDLL('../H2Lib/libh2.so')
# new_pointer_vector = lib.new_pointer_avector
# new_pointer_vector.restype = ctypes.POINTER(CStructVector)
# new_pointer_vector.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_uint]
# print_vector = lib.print_avector
# print_vector.restype = None
# print_vector.argtypes = [ctypes.POINTER(CStructVector)]

# x = [1.0, 2.0, 3.0, 5.0]


# # ---------------


# cx = (ctypes.c_double * len(x))(*x)
# v = new_pointer_vector(cx, len(x))
# print_vector(v)


# # ---------------


# class Vector():
#     def __init__(self, lst):
#         self._clst = (ctypes.c_double * len(lst))(*lst)
#         self.cptr = new_pointer_vector(self._clst, len(lst))

#     def print(self):
#         print_vector(self.cptr)


# v2 = Vector(x)
# v2.print()


from h2libpy.data.vector.avector import AVector

x = [1.0, 2.0, 3.0, 5.0]
v = AVector.from_list(x)
v.print()
print(v.v)
