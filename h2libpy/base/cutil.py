def deref(ptr):
    return ptr.contents


def cptr_to_list(ptr, length: int):
    return ptr[:length]


def carray_to_tuple(carray):
    return tuple(carray[:])
