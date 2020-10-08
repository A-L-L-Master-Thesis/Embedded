import json
import time
import socket
import threading
from .message import Message

DRONE_UPDATE_INTERVAL = 10

class Client():
    def __init__(self, host, port, drone_controller):
        self.drone_controller = drone_controller
        self.address = (host, port)
        self.start(host, port)
        self.new_client()

    def start(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self.socket.connect((host, port))
        
    def listen(self):
        receive_thread = threading.Thread(target=self.listen_server)
        receive_thread.daemon = True
        receive_thread.start()
        
    def update(self):
        receive_thread = threading.Thread(target=self.update_drone)
        receive_thread.daemon = True
        receive_thread.start()
        
    def new_client(self):
        self.listen()
        self.update()
            
    def send(self, command, data):
        msg = Message(self.drone_controller.drone.uuid, command=command, data=data).to_bytes()
        self.socket.sendall(msg)

    def close(self):
        self.socket.shutdown(1)
                        
    def wait_message(self):
        message = b''
        while True:
            chunk = self.socket.recv(1) 
            
            if not chunk:
                raise RuntimeError("Socket connection broken")
            
            if chunk == b'\n':
                break
            
            message += chunk 

        return message
                        
    def receive_message(self):
        try:
            message = self.wait_message()

            if not message:
                self.socket.close()
                return None

            message = Message(**json.loads(message))
            return message
            
        except ConnectionResetError as e:
            pass
        except RuntimeError as e:
            pass
            
        self.socket.close()
        return None
            
    def listen_server(self):
        print('Server connection opened:', self.address)
        while True:
            msg = self.receive_message()

            print(self.address, msg)
            if not msg and msg.target != self.drone_controller.drone.uuid:
                break

            self.drone_controller.command_execute(msg.message)
            
        print('Server connection closed', self.address)
        
    def update_drone(self):
        while True:
            self.send('update', self.drone_controller.drone)
            time.sleep(DRONE_UPDATE_INTERVAL)

if __name__ == "__main__":
    c1 = Client('127.0.0.1', 65432, 'test1')
    c1.send('bob')
    c1.send('jens')


