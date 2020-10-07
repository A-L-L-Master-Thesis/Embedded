import json
import socket
import threading
from message import Message

class Server():
    def __init__(self, host, port):
        self.clients = {}
        self.start(host, port)
        self.listen()
        
    def start(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(5)
        print('Server started!')
        
    def listen(self):
        while True:
            client, address = self.socket.accept()     
            receive_thread = threading.Thread(target=self.on_new_client, args=(client, address))
            receive_thread.daemon = True
            receive_thread.start()
            
    def on_new_client(self, client, address):
        print('New client connected:', address)
        
        if not self.handshake(client):
            client.close()
        else:
            self.listen_client(client, address)
            
        print('Client connection closed', address)
        
    def handshake(self, client):
        msg = self.receive_message(client)
        
        if msg and msg.sender:
            self.clients[msg.sender] = client
            return True
        
        return False

    def send(self, uuid, msg: Message):
        msg = Message('server', message=msg).to_bytes()
        self.clients[uuid].send(msg)
        
    def send_all(self, msg: Message):
        for uuid in self.clients.keys():
            self.send(uuid, msg)
            
    
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
            print(message)

            if not message:
                client.close()
                return None

            print(message)
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

            if not msg:
                break
            
            self.send_all('update')

            # Do something based on message            
if __name__ == "__main__":
    s = Server('127.0.0.1', 44444)