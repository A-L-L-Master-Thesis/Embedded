import socket
import threading
import time
import json
from message import Message

class Server():
    def __init__(self):
        self.start()
        self.clients = {}
        
    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('127.0.0.1', 65432))
        self.socket.listen(5)
        print('Server started!')
        
    def listen(self):
        while True:
            client, address = self.socket.accept()     
            receive_thread = threading.Thread(target=self.on_new_client, args=(client, address))
            receive_thread.daemon = True
            receive_thread.start()
                
    def send_one(self, uuid, msg: Message):
        self.clients[uuid].send(msg)
    
    def send_all(self, msg: Message):
        for client in self.clients.values():
            client.send(msg)
    
    def add_client(self, client):
        msg = self.get_message(client)
        
        if not msg:
            return False
        
        if msg.sender:
            self.clients[msg.sender] = client
            return True
        
        return False
                
    def on_new_client(self, client, address):
        print('New client connected:', address)
        
        if not self.add_client(client):
            client.close()
        else:
            self.listen_client(client, address)
            
    def get_message(self, client):
        try:
            msg = client.recv(1024)

            if not msg:
                client.close()
                return None

            msg = Message(**json.loads(msg))
            
            if msg.message:
                pass
            
            self.send_ack(client, msg.sender)
            return msg
            
        except ConnectionResetError as e:
            client.close()
            return None

    def send_ack(self, client, uuid):
        client.send(Message('server', 'ack', uuid).to_bytes())
        
    def listen_client(self, client, address):
        while True:
            msg = self.get_message(client)

            if not msg:
                break

            # Do something based on message

        print('Client connection closed', address)
            
if __name__ == "__main__":
    s = Server()
    s.listen()