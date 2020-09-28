from json import JSONEncoder

class Drone():
    def __init__(self, uuid, *args, **kwargs):
        self.uuid = uuid
        
class DroneEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__