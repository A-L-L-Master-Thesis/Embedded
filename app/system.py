import os
import uuid
import socket
from _version import __version__
from .communication import Communication
from models import Drone, DroneEncoder
from handlers import write, read

class System():
    def __init__(self):
        self.uuid_file = os.path.join(os.getcwd(), 'drone_info.json')
        self.initialize()
        
        self.print_info()
        self.register_drone()
    
    def initialize(self):
        if not os.path.exists(self.uuid_file):
            self.drone = write(self.uuid_file, Drone(str(uuid.uuid1())), DroneEncoder)
        else:
            self.drone = read(self.uuid_file, Drone)
        
        self.drone.update()
        
    def print_info(self):
        print(f'DroneOS version {__version__}')
        print(f'Drone uuid: {self.drone.uuid}')
        print(f'Drone local ip: {socket.gethostbyname(socket.gethostname())}')

    def register_drone(self):
        Communication.register(self.drone)
        print("Drone registered with backend")

