import os
import uuid
import socket
from app import Communication, Drone
from handlers import write, read


class System():
    def __init__(self):
        self.communication = Communication()
        self.drone = self.initialize()
        self.register_drone()

    def initialize(self):
        uuid_file = os.path.join(os.getcwd(), 'drone_info.json')
        
        if not os.path.exists(uuid_file):
            return write(uuid_file, Drone(str(uuid.uuid1())))
        else:
            return read(uuid_file, Drone)
        
    def register_drone(self):
        self.communication.register(self.drone)
        print("Drone registered with backend")


if __name__ == "__main__":
    s = System()