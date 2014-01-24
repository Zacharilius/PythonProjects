"""
chatApplication.py

Creates a server and a client in a class. The server must be started first.
Then the client. The client must be provided with the server's port and IP
address.The client and server can then chat.
"""

class chatApp:
    def __init__():
        pass
    def clientSide():
        pass
    def serverSide():
        #Create a Socket

        
        pass
    def main():
        pass
    
class mySocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
    def connect(self, host, port):
        self.sock.connect((host,port))

    def mysend(self,msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        msg = ''
        while len(msg) < MSGLEN:
            chunk = self.sock.recv(MSGLEN-len(msg))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            msg = msg + chunk
        return msg
