from ctypes import c_bool, c_double, c_int, pointer


def deref(ptr):
    ''' Returns value behind a C pointer '''
    return ptr.contents


def cptr_to_list(ptr, length: int):
    ''' Converts an C pointer to a python list '''
    return ptr[:length]


def carray_to_tuple(carray):
    ''' Converts C array to python tuple '''
    return tuple(carray[:])


def pylist_to_ptr(lst, ctype):
    ''' Creates C pointer for given list '''
    return (ctype * len(lst))(*lst)


def try_wrap(obj, wrapperclass):
    ''' Trys to wrap C object in corresponding wrapper class '''
    return wrapperclass(obj) if obj else None


def verify_type(obj, types):
    ''' Checks if obj is of any type in types, raises error if not '''
    if not any(isinstance(obj, t) for t in types):
        raise TypeError(f'Invalid type for parameter, expected any of {types}')


def to_enum(obj, enum):
    ''' Converts CEnum object to its python equivalent '''
    for val in enum:
        if obj.value == val.value.value:
            return val
    return None


def get_address(obj, ctype=None):
    ''' Returns memory location of given object.
        Needs to be converted to a c type first, provide if it can't be
        inferred.
    '''
    if ctype is None:
        if isinstance(obj, float):
            return pointer(c_double(obj))
        elif isinstance(obj, int):
            return pointer(c_int(obj))
        elif isinstance(obj, bool):
            return pointer(c_bool(obj))
    else:
        return pointer(ctype(obj))
