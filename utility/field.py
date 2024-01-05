from abc import ABC, abstractmethod

class Field(ABC):

    @abstractmethod
    def __init__(self, value=None):
        self.value = value
    
    # overridden method __repr__ ## reprezentacją tego obiektu będzie tekstowa zawartość value
    def __repr__(self) -> str:
        return f"{self.value}"
    
    