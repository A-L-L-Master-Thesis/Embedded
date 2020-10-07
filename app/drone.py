from exceptions import NoConnectionError
import socket
import threading
import time
from commands import ControlCommands, ReadCommands, SetCommands
from models import PositionModel, StatsModel
from datetime import datetime
from enums import StatusEnum

class Drone():
    def __init__(self, uuid):
        self.log = []
        self.uuid = uuid
        
        self.control = ControlCommands(self.send_command)
        self.read = ReadCommands(self.send_command)
        self.set = SetCommands(self.send_command)
        
        self.commands = self.commands()
        
        self.connect()
        self.activate()
        
        self.update()
        self.print_info()
        
    def commands(self):
         return {
            'update': self.update,
            'read': self.read.battery
        }
        
    def command_execute(self, command):
        if command in self.commands:
            self.commands[command]()
            return True
        return False
        
    def update(self):
        self.lastUpdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # self.position = PositionModel(22, 1, 2)
        # self.battery = self.read.battery()
        # self.status = self.drone_status()
        
    def drone_status(self):
        return StatusEnum.CHARGING.value
    
    def connect(self):
        # Socket for sending command
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        self.socket.bind(('', 8889))

        # Thread for receiving command acknowledgment 
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()


        self.MAX_TIME_OUT = 15.0
        
    def activate(self):
        """
        command: command
        description: entry SDK mode
        response: ok, error
        """
        result = self.send_command('command')
        if result == None:
            raise NoConnectionError
    
    def send_command(self, command):
        def _time_difference(start):
            return time.time() - start
        
        self.log.append(StatsModel(command, len(self.log)))
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
        print(f'Local ip: {socket.gethostbyname(socket.gethostname())}')
        print(f'Last update: {self.lastUpdate}')
        print(f'UUID: {self.uuid}')
        print(f'Position: {self.position}')
        print(f'Battery: {self.battery}%')
        print(f'Status: {StatusEnum.format(self.status)}')
        