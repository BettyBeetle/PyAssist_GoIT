from utility.field import Field

class Name (Field):
    '''
    Class for name object
    Class raise a ValueError if no name is given

    Args:
        Field (class): parent class
    '''

    # function used as a decorator to catch errors when value is setting
    def _value_error(func):
        def inner(self, value): ## self (co sugeruje, że funkcja może być częścią klasy) oraz value, która jest wartością, którą chcemy przekazać do oryginalnej funkcji.
            while True:
                if not value:
                    raise ValueError(f"No name is given: {value}")
                return func(self, value) ## else nie jest tu potrzebny bo return przerywa funkcję
        return inner

    @_value_error
    def __init__(self, value: str):
        self.value = value
    
    ### chciałabym bez tego
  
    # def _get_value(self):
    #     return self._value

    # def _set_value(self, value):
    #     self._value = value
    # value = property(_get_value, _value_error(_set_value))