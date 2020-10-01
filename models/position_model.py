class PositionModel():
    def __init__(self, altitude, latitude, longitude):
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f'altitude: {self.altitude}, lat: {self.latitude} long: {self.longitude}'