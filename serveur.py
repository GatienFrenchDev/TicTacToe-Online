import socket
import json

# Vide => 0
# Serveur => 1
# Client => 2

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
        self.grille = json.loads(sclient.recv(1024).decode())
        self.affichage()
        self.cocher(sclient)
    
    def cocher(self, sclient):
        choix = input('Entrer la case a jouer (ex : a2): ')
        coup = (ord(choix[0].lower())-97, int(choix[1])-1)
        if self.grille[coup[0]][coup[1]] == 0:
            self.grille[coup[0]][coup[1]] = 1
            sclient.send(str(self.grille).encode())
        else:
            self.cocher()

    def affichage(self):
        print(self.grille)