from socket import socket

class Client:
    def __init__(self, ip):
        self.socket = socket()
        self.socket.connect((ip , 8080))
