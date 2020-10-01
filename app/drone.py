import socket
import os
import threading
import time
from .stats import Stats
from commands import ControlCommands, ReadCommands, SetCommands
from models import PositionModel
from datetime import datetime
from enums import StatusEnum
from _version import __version__

class Drone():
    def __init__(self, uuid):
        self.uuid = uuid
                
        # self.control = ControlCommands(self.send_command)
        # self.read = ReadCommands(self.send_command)
        # self.set = SetCommands(self.send_command)
        
        # self.connect()
        # self.activate()
        self.update()
        
        # self.control.takeoff()
        
        # time.sleep(3)
        # self.print_info()
        
        # self.control.land()
        # self.update()
        # self.print_info()
        
    def update(self):
        # self.lastUpdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # self.position = PositionModel(22, 1, 2)
        # self.battery = self.read.battery()
        # self.status = self.drone_status()
        
        self.lastUpdate = datetime.now().isoformat()
        self.position = PositionModel(22, 1, 2)
        self.battery = 33
        self.status = StatusEnum.CHARGING.value
        
    def drone_status(self):
        # Implement logic to figure out status
        return StatusEnum.CHARGING.value
    
    def connect(self):
        # Socket for sending command
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        self.socket.bind(('', 8889))

        # Thread for receiving command acknowledgment 
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.log = []

        self.MAX_TIME_OUT = 15.0
        
    def activate(self):
        """
        command: command
        description: entry SDK mode
        response: ok, error
        """
        self.send_command('command')
    
    def send_command(self, command):
        def _time_difference(start):
            return time.time() - start
        
        self.log.append(Stats(command, len(self.log)))
        self.socket.sendto(command.encode('utf-8'), ('192.168.10.1', 8889))
        
        start = time.time()
        while not self.log[-1].response:
            if _time_difference(start) > self.MAX_TIME_OUT:
                self.log.append(f'Max timeout exceeded... command: {command}')
                return None
            
        return self.log[-1].response.decode('utf-8').rstrip("\r\n")
            
    def _receive_thread(self):
        """Listen to responses from the Tello.
        Runs as a thread, sets self.response to whatever the Tello last returned.
        """
        while True:
            try:
                self.response, ip = self.socket.recvfrom(1024)
                self.log[-1].add_response(self.response)
                #print(f'{ip}: {self.response}')
            except socket.error as error:
                print(f'Caught exception socket.error : {error}')
                
    def print_info(self):
        print(f'DroneOS version {__version__}')
        print(f'Local ip: {socket.gethostbyname(socket.gethostname())}')
        print(f'Last update: {self.lastUpdate}')
        print(f'UUID: {self.uuid}')
        print(f'Position: {self.position}')
        print(f'Battery: {self.battery}%')
        print(f'Status: {StatusEnum.format(self.status)}')
        print('test', self.read.height())
        print('test1', self.read.attitude())