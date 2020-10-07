import json
from encoders import Encoder
class PositionModel():
    def __init__(self, altitude, latitude, longitude):
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude

    def to_json(self):
            return json.dumps(self, cls=Encoder)
        
    def __str__(self):
        return f'altitude: {self.altitude}, lat: {self.latitude} long: {self.longitude}'