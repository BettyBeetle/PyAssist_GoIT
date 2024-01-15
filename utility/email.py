from utility.field import Field
import re       ## może lepiej bibliotekę do walidacji email

class Email(Field): 
    '''
    Class for email object
    Class raise a ValueError if email is invalid

    Args:
        Field(class): parent class
    '''
    
    # function used as a decorator to catch errors when value is setting
    def _value_error(func):
        def inner(self, value):
            while True:
                value = value.strip()
                email_pattern = (r'[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]{2,}') # 'r"^[a-zA-Z0-9.!#$%&'*+\/=?^_{|}~-]+@a-zA-Z0-9?(?:.a-zA-Z0-9?)*$"`

                if not re.match(email_pattern,value): ## sprawdzenie czy wartość value pasuje do wzorca
                    raise ValueError(f"Invalid e-mail address format: {value}")
                return func(self, value)
        return inner

    @_value_error
    def __init__(self, value: str):
        self.value = value