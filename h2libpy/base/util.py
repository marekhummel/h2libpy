from ctypes import addressof, c_bool, c_double, c_int, c_void_p, cast, pointer
from typing import Any, List, Tuple


def deref(ptr) -> Any:
    ''' Returns value behind a C pointer '''
    return ptr.contents


def cptr_to_list(ptr, length: int) -> List[Any]:
    ''' Converts an C pointer to a python list '''
    return ptr[:length]


def carray_to_tuple(carray) -> Tuple[Any, ...]:
    ''' Converts C array to python tuple '''
    return tuple(carray[:])


def pylist_to_ptr(lst: List[Any], ctype) -> Any:
    ''' Creates C pointer for given list '''
    return (ctype * len(lst))(*lst)


def try_wrap(cobj, wrapperclass) -> Any:
    ''' Trys to wrap C object in corresponding wrapper class '''
    return wrapperclass(cobj) if cobj else None


def verify_type(obj, types) -> None:
    ''' Checks if obj is of any type in types, raises error if not '''
    if not any(isinstance(obj, t) for t in types):
        raise TypeError(f'Invalid type for parameter, expected any of {types}')


def to_enum(obj, enum) -> Any:
    ''' Converts CEnum object to its python equivalent '''
    for val in enum:
        if obj.value == val.value.value:
            return val
    return None


def to_voidp(obj):
    ''' Casts object to void* '''
    return cast(obj, c_void_p)


def get_address(pyobj, ctype=None) -> Any:
    ''' Returns memory location of given object.
        Needs to be converted to a c type first, provide if it can't be
        inferred.
    '''
    if ctype is None:
        if isinstance(pyobj, float):
            return pointer(c_double(pyobj))
        elif isinstance(pyobj, int):
            return pointer(c_int(pyobj))
        elif isinstance(pyobj, bool):
            return pointer(c_bool(pyobj))
    else:
        return pointer(ctype(pyobj))


def ptr_address(cptr) -> Any:
    ''' Dedicated address getter since this is awfully complicated
        in ctypes. Returns adress of pointer '''
    return addressof(deref(cptr))
