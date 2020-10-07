from json import JSONEncoder
from models.drone_model import DroneModel

class DroneEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, DroneModel):
            return {
                'uuid': o.uuid,
                'lastUpdate': o.lastUpdate,
                'currentPosition': o.position,
                'batteryPercentage': o.battery,
                'status': o.status,
            }
        return o.__dict__
