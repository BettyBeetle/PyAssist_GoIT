from utility.field import Field

class Phone(Field):
    '''
    Class for phone object
    Class raise a ValueError if phone is invalid

    Args: Field(class: parent class)
    '''

    # function used as a decorator to catch errors when value is setting
    def _value_error(func):
        def inner(self, value):
            while True:
                value = (
                    value.strip()
                    .replace(" ","")
                    .replace("(","")
                    .replace(")","")
                    .replace("-","")
                    .removeprefix("+")
                )

                if not value.isnumeric():
                    raise ValueError(f"Invalid phone number format: {value}")
                return func(self, value)
        return inner
        
    @_value_error
    def __init__(self, value: str):
        self.value = value