from json import JSONEncoder, dumps
from . import Encoder

class DroneEncoder(JSONEncoder):
        def default(self, o):
            data = {'uuid': o.uuid,
                    'lastUpdate': o.lastUpdate,
                    'status': o.status,
                    'position': dumps(o.position),
                    'battery': o.battery
                    }
            return data