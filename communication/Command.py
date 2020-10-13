import json
from encoders import Encoder


class Command():
    def __init__(self, command: str, data: str):
        self.command = command
        self.data = data

    def to_bytes(self):
        return json.dumps(self, cls=Encoder).encode('utf-8')
    
    def __str__(self) -> str:
        return f'Command {self.command} - {self.data}'
