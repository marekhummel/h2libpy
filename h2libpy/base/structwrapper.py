
class StructWrapper:

    def __getattr__(self, name):
        ''' To make struct fields available in classes if an getter method
            is provided in subclass
        '''
        fields = self._as_parameter_.contents._fields_
        members = [name for (name, ctype) in fields]

        # C struct doesnt have this field
        if name not in members:
            raise AttributeError(f'\'{self.__class__.__name__}\' '
                                 f'has no attribute \'{name}\'')

        # Corresponding method for field is not implemented in this class
        getter = f'_getter_{name}'
        if getter not in dir(self.__class__):
            raise AttributeError(f'\'{self.__class__.__name__}\' '
                                 f'has no getter for attribute \'{name}\'')

        return getattr(self, getter)()