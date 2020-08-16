from h2libpy.base.util import deref
from ctypes import POINTER


class StructWrapper():

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

    def __getattr__(self, name):
        ''' To make struct fields available in classes if an getter method
            is provided in subclass
        '''
        # C struct doesnt have this field
        if name not in self.avail_fields():
            raise AttributeError(f'\'{self.__class__.__name__}\' '
                                 f'has no attribute \'{name}\'')

        # Corresponding method for field is not implemented in this class
        getter = f'_{self.__class__.__name__}__getter_{name}'
        if getter not in dir(self.__class__):
            raise AttributeError(f'\'{self.__class__.__name__}\' '
                                 f'has no getter for attribute \'{name}\'')

        # Return value
        return getattr(self, getter)()

    def cobj(self, no_ptr: bool = False):
        return deref(self._as_parameter_) \
            if not no_ptr \
            else self._as_parameter_

    def avail_fields(self):
        ''' Lists all available fields in c struct '''
        fields = self._as_parameter_.contents._fields_
        members = [name for (name, ctype) in fields]
        return members
