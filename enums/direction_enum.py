from enum import Enum

class DirectionEnum(Enum):
    LEFT = 'l'
    RIGHT = 'r'
    FORWARD = 'f'
    BACK = 'b'
    
    @classmethod
    def format(cls, value):
        if cls.LEFT.value == value:
            return 'Left'
        elif cls.RIGHT.value == value:
            return 'Right'
        elif cls.FORWARD.value == value:
            return 'Forward'
        elif cls.BACK.value == value:
            return 'Back'