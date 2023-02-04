from socket import socket
import json

# Vide => 0
# Serveur => 1
# Client => 2

class Client:
    def __init__(self, ip):
        self.socket = socket()
        self.socket.connect((ip , 8080))
        self.grille = [[0]*3]*3
        self.socket.send(str(self.grille).encode())
        self.grille = json.loads(self.socket.recv(1000).decode())
        self.affichage()
        self.cocher()
        
    def cocher(self):
        choix = input('Entrer la case a jouer (ex : a2): ')
        coup = (ord(choix[0].lower())-97, int(choix[1])-1)
        if self.grille[coup[0]][coup[1]] == 0:
            self.grille[coup[0]][coup[1]] = 1
            self.socket.send(str(self.grille).encode())
        else:
            self.cocher()
    
    def affichage(self):
        print(self.grille)