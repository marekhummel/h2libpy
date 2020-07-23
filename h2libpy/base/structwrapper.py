from h2libpy.base.cutil import deref


class StructWrapper:
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

        return getattr(self, getter)()

    def cobj(self, no_ptr: bool = False):
        return deref(self._as_parameter_) if not no_ptr \
                                          else self._as_parameter_

    def avail_fields(self):
        fields = self._as_parameter_.contents._fields_
        members = [name for (name, ctype) in fields]
        return members
