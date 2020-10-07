import json
from encoders import Encoder

class DroneModel():
    def __init__(self, uuid, lastUpdate, position, battery, status):
        self.uuid = uuid
        self.lastUpdate = lastUpdate
        self.position = position
        self.battery = battery
        self.status = status

    def to_json(self):
            return json.dumps(self, cls=Encoder)
