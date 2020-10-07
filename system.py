import os
import uuid
from app import Drone
from handlers import write, read
from communication import Client
from exceptions import NoConnectionError
from models import Version

class System():
    def __init__(self):
        try:
            print(f'DroneOS version {read("version.json", Version).version}')
            self.drone = self.initialize()
            self.client = Client('localhost', 44444, self.drone)
            self.register_drone()
            
            # Keeps connection alive
            while True:
                pass
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