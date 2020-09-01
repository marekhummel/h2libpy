from collections import defaultdict
from ctypes import POINTER
from typing import Any, Callable, Dict, List

from h2libpy.base.util import deref, ptr_address, to_voidp


class StructWrapper():
    __init__: Callable[[Any, List[Any]], None]
    _objs: Dict[Any, int] = defaultdict(lambda: 0)

    def __init_subclass__(cls, *, cstruct):
        ''' Sets default constructor for all struct wrappers.
            All struct wrappers should accept an pointer to their corresponding
            c struct in the constructor '''
        def _new_init(self, cobj, refs=[]):
            assert isinstance(cobj, POINTER(cstruct))
            self._as_parameter_ = cobj
            self._refs = refs
            StructWrapper._objs[ptr_address(cobj)] += 1
            old_init(self)

        def _new_del(self):
            StructWrapper._objs[ptr_address(self._as_parameter_)] -= 1

        old_init = cls.__init__
        cls.__init__ = _new_init
        cls.__del__ = _new_del
        # if hasattr(cls, 'delete'): cls.__del__ = cls.delete
        return super().__init_subclass__()

    def __getattr__(self, name: str):
        ''' To make struct fields available in classes if an getter method
            is provided in subclass
        '''
        # C struct doesnt have this field
        if name not in self.avail_fields():
            error = f"'{self.__class__.__name__}' has no attribute '{name}'"
            raise AttributeError(error)

        # Corresponding method for field is not implemented in this class
        getter = f'_{self.__class__.__name__}__getter_{name}'
        if getter not in dir(self.__class__):
            raise AttributeError(f"'{self.__class__.__name__}' "
                                 f"has no getter for attribute '{name}'")

        # Return value
        return getattr(self, getter)()

    def __setattr__(self, name: str, value: Any):
        ''' Prohibits from setting a class varible with the same name like
            a field of the struct
        '''
        if name not in ['_as_parameter_', '_refs']:
            if name in self.avail_fields():
                raise AttributeError("Can't set fields of C struct.")
        super().__setattr__(name, value)

    def cobj(self):
        ''' Returns wrapped c object '''
        return deref(self._as_parameter_)

    def as_voidp(self):
        ''' Casts wrapped c object to void* '''
        return to_voidp(self.cobj())

    def avail_fields(self) -> List[str]:
        ''' Lists all available fields in c struct '''
        fields = self._as_parameter_.contents._fields_
        members = [name for (name, ctype) in fields]
        return members

    def delete(self, del_func):
        ''' Generic delete function. Only deletes if no other wrapper
            to the same c objects exist '''
        if StructWrapper._objs[ptr_address(self._as_parameter_)] == 1:
            del_func(self)
