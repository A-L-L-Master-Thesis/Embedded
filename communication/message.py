import json
from encoders import Encoder
from .Command import Command

class Message():
    def __init__(self, sender, command, data, target = "server"):
        self.sender = sender
        self.message = Command(command, data)
        self.target = target

    def to_bytes(self):
        data = json.dumps(self, cls=Encoder)
        return f'{data}\n'.encode('utf-8')
    
    def __str__(self) -> str:
        return self.message
