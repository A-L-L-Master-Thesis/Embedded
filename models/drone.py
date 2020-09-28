from datetime import datetime
from json import JSONEncoder
from enum import Enum
from models.position import Position

class StatusEnum(Enum):
    IDLE = 0
    CHARGING = 1
    LAUNCHING = 2
    LANDING = 3
    RETURNING = 4
    SEARCHING = 5
    FOLLOWING = 6
    ERROR = 440
class Drone():
    def __init__(self, uuid: str):
        self.uuid = uuid

    def update(self):
        self.lastUpdate = datetime.now().isoformat()
        self.position = Position(22, 1, 2)
        self.battery = 33
        self.status = StatusEnum.CHARGING.value
class DroneEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__