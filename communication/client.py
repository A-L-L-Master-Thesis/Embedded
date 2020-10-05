import socket
import time
import json
from message import Message


class Client():
    def __init__(self, host, port, uuid):
        self.uuid = uuid
        self.connect(host, port)

    def connect(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self.socket.connect((host, port))
        self.send('')
        
    def send(self, msg):
        msg = Message(self.uuid, message=msg)
        data = msg.to_bytes()
        self.socket.send(data)
        self.wait_for_ack()
    
    def close(self):
        self.socket.shutdown(1)
        
    def get_message(self, client):
        try:
            msg = client.recv(1024)

            if not msg:
                client.close()
                return None

            msg = Message(**json.loads(msg))
            
            if msg.message:
                pass
            
            return msg
            
        except ConnectionResetError as e:
            client.close()
            return None

    def wait_for_ack(self):
        while True:
            try:
                msg = self.get_message(self.socket)
                if msg.message == 'ack':
                    return True
                else:
                    break
            except ConnectionResetError as e:
                self.socket.close()
                break
            
        return False
    
if __name__ == "__main__":
    c1 = Client('127.0.0.1', 65432, 'test1')

    c1.send('bob')
    c1.send('jens')
    #c1.listen()
    # time.sleep(2)
    c1.close()


