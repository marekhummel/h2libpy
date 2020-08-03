def deref(ptr):
    return ptr.contents


def cptr_to_list(ptr, length: int):
    return ptr[:length]


def carray_to_tuple(carray):
    return tuple(carray[:])


def pylist_to_ptr(lst, ctype):
    return (ctype * len(lst))(*lst)


def try_wrap(obj, wrapperclass):
    ''' Trys to wrap c object in corresponding wrapper class '''
    return wrapperclass(obj) if obj else None


def is_scalar(obj):
    return isinstance(obj, int) or isinstance(obj, float)
