import os
import uuid
from controllers import DroneController
from handlers import write, read
from communication import Client
from exceptions import NoConnectionError
from models import Version, DroneModel

class System():
    def __init__(self):
        try:
            print(f'DroneOS version {read("version.json", Version).version}')
            self.drone_controller = self.initialize()
            # self.client = Client('85.218.161.148', 44444, self.drone_controller)
            self.drone_controller.control.takeoff()
            # Keeps connection alive
            while True:
                pass
        except NoConnectionError:
            print('No connection to drone')

    def initialize(self):
        uuid_file = os.path.join(os.getcwd(), 'drone_info.json')
        
        if not os.path.exists(uuid_file):
            return DroneController(write(uuid_file, DroneModel(str(uuid.uuid1()))))
        else:
            return DroneController(read(uuid_file, DroneModel))


if __name__ == "__main__":
    s = System()