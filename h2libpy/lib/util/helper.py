from h2libpy import lib
from typing import Callable, Any, List


def get_func(name: str, returntype: Any, argtypes: List[Any]) -> Callable:
    ''' Returns callable function object from c lib '''
    f = lib.__getattr__(name)
    f.restype = returntype
    f.argtypes = argtypes
    return f


def uninit() -> None:
    ''' uninit function of h2lib '''
    uninit_h2lib = get_func('uninit_h2lib', None, [])
    uninit_h2lib()
