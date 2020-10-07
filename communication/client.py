import json
import socket
import threading
from .message import Message

class Client():
    def __init__(self, host, port, drone):
        self.drone = drone
        self.address = (host, port)
        self.start(host, port)
        self.listen()

    def start(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self.socket.connect((host, port))
        self.send('hey alec')
        
    def listen(self):
        receive_thread = threading.Thread(target=self.on_new_client, args=(self.socket, self.address))
        receive_thread.daemon = True
        receive_thread.start()
        
    def on_new_client(self, client, address):
        print('Server connection opened:', self.address)
        
        self.listen_client(client, address)
            
        print('Server connection closed', address)
            
    def send(self, msg):
        msg = Message(self.drone.uuid, message=msg).to_bytes()
        self.socket.sendall(msg)

    def close(self):
        self.socket.shutdown(1)
                        
    def wait_message(self, client):
        message = b''
        while True:
            chunk = client.recv(1) 
            
            if not chunk:
                raise RuntimeError("Socket connection broken")
            
            if chunk == b'\n':
                break
            
            message += chunk 

        return message
                        
    def receive_message(self, client):
        try:
            message = self.wait_message(client)

            if not message:
                client.close()
                return None

            message = Message(**json.loads(message))
            return message
            
        except ConnectionResetError as e:
            pass
        except RuntimeError as e:
            pass
            
        client.close()
        return None
            
    def listen_client(self, client, address):
        while True:
            msg = self.receive_message(client)

            print(address, msg)
            if not msg and msg.target != self.drone.uuid:
                break

            self.drone.command_execute(msg.message)

    
if __name__ == "__main__":
    c1 = Client('127.0.0.1', 65432, 'test1')
    c1.send('bob')
    c1.send('jens')
    # time.sleep(2)


