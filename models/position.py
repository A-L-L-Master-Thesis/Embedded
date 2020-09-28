from json import JSONEncoder

class Position():
    def __init__(self, altitude, latitude, longitude):
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude
        
class PositionEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__