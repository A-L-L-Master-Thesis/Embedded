from enum import Enum

class StatusEnum(Enum):
    IDLE = 0
    CHARGING = 1
    LAUNCHING = 2
    LANDING = 3
    RETURNING = 4
    SEARCHING = 5
    FOLLOWING = 6
    ERROR = 440
    
    @classmethod
    def format(cls, value):
        if cls.IDLE.value == value:
            return 'Idle'
        elif cls.CHARGING.value == value:
            return 'Charging'
        elif cls.LAUNCHING.value == value:
            return 'Launching'
        elif cls.LANDING.value == value:
            return 'Landing'
        elif cls.RETURNING.value == value:
            return 'Returning'
        elif cls.SEARCHING.value == value:
            return 'Searching'
        elif cls.FOLLOWING.value == value:
            return 'Following'
        elif cls.ERROR.value == value:
            return 'Error'