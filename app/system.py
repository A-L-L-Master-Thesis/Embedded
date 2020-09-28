import os
import json
import uuid
import socket
from _version import __version__
from models import Drone, DroneEncoder
from handlers import write, read

class System():
    def __init__(self):
        self.uuid_file = os.path.join(os.getcwd(), 'drone_info.json')
        self.initiliaze()
        
        self.print_info()
        self.register_drone()
    
    def initiliaze(self):
        if not os.path.exists(self.uuid_file):
            self.drone_info = write(self.uuid_file, Drone(str(uuid.uuid1())), DroneEncoder)
        else:
            self.drone_info = read(self.uuid_file, Drone)
        
    def print_info(self):
        print(f'DroneOS version {__version__}')
        print(f'Drone uuid: {self.drone_info.uuid}')
        print(f'Drone local ip: {socket.gethostbyname(socket.gethostname())}')

    def register_drone(self):
        pass

