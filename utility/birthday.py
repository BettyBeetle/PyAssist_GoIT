from utility.field import Field
from datetime import datetime


class FutureDateError(Exception):
    """
    Custom exception to indicate that a future date was attempted to be assigned as a birthday.
    This exception is raised when attempting to set a date of birth that is in the future.
    
    Args:
        Exception (class): parent class for all exceptions.
    """

    pass

class Birthday(Field):
    '''
    Class for birthday object
    Class raise a ValueError if birthday is invalid

    Args:
        Field(class): parent class
    '''
    
    # Function used as a decorator to catch errors when value is setting
    def _value_error(func):
        def inner(self, value):
            try:
                value = datetime.strptime(
                    value.strip()
                    .replace(".", "-")
                    .replace(",", "-")
                    .replace("/ ", "-")
                    .replace(" ", "-"),
                    "%d-%m-%Y",
                ).date()
                
                if value is  None:
                    return None
                
                elif value is not None and value > datetime.now().date():
                    raise FutureDateError(f"Cannot set a future date as a birthday: {value}")
                return func(self, value)
            
            except ValueError as e:
                raise ValueError(f"Invalid date format: {value}")
        return inner

    @_value_error
    def __init__(self, value: None):
        self.value = value