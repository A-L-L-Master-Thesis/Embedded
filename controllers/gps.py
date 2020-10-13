import serial
import time
import string
import pynmea2
from models import PositionModel

class GpsController():

    @staticmethod
    def get_coordinates():
        # The serial port that the gps is connected to, most likely to be /dev/ttyAMA0 or /dev/ttyS0
        gpsPort = '/dev/ttyAMA0'
        connection = serial.Serial(gpsPort, baudrate=9600, timeout=0.5)

        while True:
            data = connection.readline()
            
            if data[0:6] == b"$GPGGA":
                parsed_data = pynmea2.parse(data.decode("utf-8"))
                
                lat = parsed_data.latitude
                lng = parsed_data.longitude
                alt = parsed_data.altitude

                pos = PositionModel(alt,lat,lng)

                return pos