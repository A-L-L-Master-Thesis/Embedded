import json
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
        return json.dumps(self, cls=Encoder).encode('utf-8')
