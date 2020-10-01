import json
from flask import Blueprint, jsonify, Response
from app import Drone
from encoders import DroneEncoder

def construct_blueprint(drone: Drone):
    drone_endpoint = Blueprint('drone', __name__, url_prefix='/drone')

    @drone_endpoint.route('/status', methods=['GET'])
    def status():
        data = json.dumps(drone, cls=DroneEncoder)
        return Response(data, status=200)
    

    return drone_endpoint
