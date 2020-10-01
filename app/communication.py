import requests
import json
from .drone import Drone
from encoders import Encoder
from datetime import datetime

class Communication():
    def __init__(self):
        self.endpoint = 'https://localhost:44310/api/drones'
        self.headers = {'Content-type': 'application/json', 'Accept': '*/*'}
    
    def register(self, drone: Drone):
        data = json.dumps(drone, cls=Encoder)
        print(data)
        response = requests.post(self.endpoint, data=data, headers=self.headers, verify=False)
        print(response)
    
    def update(self):
        pass