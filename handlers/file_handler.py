import json
from encoders import Encoder
    
def write(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, cls=Encoder, indent=4)
        return data
        
def read(filename, Object):
    with open(filename, 'r') as file:
        return Object(**json.load(file))