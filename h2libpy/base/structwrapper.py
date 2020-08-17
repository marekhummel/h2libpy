from ctypes import POINTER, cast, c_void_p
from typing import Any, Callable, List

from h2libpy.base.util import deref


class StructWrapper():
    __init__: Callable[[Any, List[Any]], None]

    def __init_subclass__(cls, *, cstruct):
        ''' Sets default constructor for all struct wrappers.
            All struct wrappers should accept an pointer to their corresponding
            c struct in the constructor '''
        def _new_init(self, cobj, refs=[]):
            assert isinstance(cobj, POINTER(cstruct))
            self._as_parameter_ = cobj
            self._refs = refs
        cls.__init__ = _new_init
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
        return self.as_voidp()

    def avail_fields(self) -> List[str]:
        ''' Lists all available fields in c struct '''
        fields = self._as_parameter_.contents._fields_
        members = [name for (name, ctype) in fields]
        return members
