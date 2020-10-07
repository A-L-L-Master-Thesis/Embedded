import json
import struct
from json import JSONEncoder


class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Message():
    def __init__(self, sender, message, target = "server"):
        self.sender = sender
        self.message = message
        self.target = target

    def to_bytes(self):
        data = json.dumps(self, cls=Encoder)
        return f'{data}\n'.encode('utf-8')
    
    def __str__(self) -> str:
        return self.message
