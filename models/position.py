from json import JSONEncoder

class Position():
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        
class PositionEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__