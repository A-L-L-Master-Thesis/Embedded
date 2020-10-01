from flask import Flask, jsonify
from endpoints import drone_endpoint

def flask(drone):
    app = Flask(__name__)
    
    app.register_blueprint(drone_endpoint.construct_blueprint(drone))

    @app.route('/healthcheck', methods=['GET'])
    def health_check():
        return jsonify(success=True)
        
    app.run(host='localhost', port=5000, debug=True, use_reloader=False)