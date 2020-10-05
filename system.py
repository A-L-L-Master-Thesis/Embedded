import os
import uuid
from app import Drone
from handlers import write, read
from _version import __version__
from communication import Client
from exceptions import NoConnectionError

class System():
    def __init__(self):
        try:
            print(f'DroneOS version {__version__}')
            self.drone = self.initialize()
            self.client = Client('127.0.0.1', 65432, self.drone.uuid)
            self.register_drone()
        except NoConnectionError:
            print('No connection to drone')

    def initialize(self):
        uuid_file = os.path.join(os.getcwd(), 'drone_info.json')
        
        if not os.path.exists(uuid_file):
            return write(uuid_file, Drone(str(uuid.uuid1())))
        else:
            return read(uuid_file, Drone)
        
    def register_drone(self):
        self.client.send('register')

if __name__ == "__main__":
    s = System()