import json
from encoders import DroneEncoder
from .Command import Command

class Message():
    def __init__(self, sender, message, target = "server"):
        self.sender = sender
        self.message = Command(message['command'], message['data'])
        self.target = target

    def to_bytes(self):
        data = json.dumps(self, cls=DroneEncoder)
        return f'{data}\n'.encode('utf-8')
    
    def __str__(self) -> str:
        return self.message
