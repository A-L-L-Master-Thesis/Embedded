import requests
import json
from models.drone import Drone, DroneEncoder

class Communication():
    endpoint = 'https://5f71932464a3720016e60933.mockapi.io/api/v1/drone'
    
    @staticmethod   
    def register(drone: Drone):
        data = json.dumps(drone, cls=DroneEncoder)
        print('drone_info', data)
        response = requests.post(Communication.endpoint, data)
        print('response_info', response.text)
    
    def update():
        pass