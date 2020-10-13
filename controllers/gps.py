import serial
import time
import string
import pynmea2
from models import PositionModel

class GpsController():

    @staticmethod
    def get_coordinates():
        gpsPort = '/dev/ttyAMA0'
        connection = serial.Serial(gpsPort, baudrate=9600, timeout=0.5)

        while True:
            data = connection.readline()
            
            if data[0:6] == b"$GPGGA":
                newmsg = pynmea2.parse(data.decode("utf-8"))
                lat = newmsg.latitude
                lng = newmsg.longitude
                alt = newmsg.altitude

                pos = PositionModel(alt,lat,lng)

                return pos