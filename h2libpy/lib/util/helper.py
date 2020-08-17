from h2libpy import lib
from typing import Callable, Any, List


def get_func(name: str, returntype: Any, argtypes: List[Any]) -> Callable:
    f = lib.__getattr__(name)
    f.restype = returntype
    f.argtypes = argtypes
    return f


def uninit() -> None:
    uninit_h2lib = get_func('uninit_h2lib', None, [])
    uninit_h2lib()
