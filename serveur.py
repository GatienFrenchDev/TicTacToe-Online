import socket


class Serveur:
    def __init__(self, port):
        self.port = port
        self.ip = socket.gethostbyname(socket.gethostname())
        self.socket = socket.socket()
        self.socket.bind((self.ip, port))
        self.socket.listen()
        print(f'''
=====================
PARTIE DISPONIBLE sur
    {self.ip}
=====================
        ''')
        (sclient,adclient) = self.socket.accept()
        print(adclient)