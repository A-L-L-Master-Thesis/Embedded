import json
    
def write(filename, data, encoder):
    with open(filename, 'w') as file:
        json.dump(data, file, cls=encoder, indent=4)
        return data
        
def read(filename, Object):
    with open(filename, 'r') as file:
        return Object(**json.load(file))