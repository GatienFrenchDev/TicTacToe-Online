from socket import socket
import json
from tools import affichage

# Vide => 0
# Serveur => 1
# Client => 2


class Client:
    def __init__(self, ip):
        self.socket = socket()
        self.socket.connect((ip, 8080))
        self.grille = [[0]*3,[0]*3,[0]*3]
        self.socket.send(str(self.grille).encode())
        print(affichage(self.grille))
        self.main()

    def main(self):
        while not self.hasWon():
            data = self.socket.recv(1000).decode()
            self.grille = json.loads(data)
            if data == "end":
                print("""
=============
TU AS PERDU !
=============
                """)
                return
            print(affichage(self.grille))
            self.cocher()
            print(affichage(self.grille))
            self.socket.send(str(self.grille).encode())
        self.socket.send("end".encode())

    def cocher(self):
        choix = input('Entrer la case a jouer (ex : a2): ')
        coup = (ord(choix[0].lower())-97, int(choix[1])-1)
        if self.grille[coup[0]][coup[1]] == 0:
            self.grille[coup[0]][coup[1]] = 2
        else:
            self.cocher()

    def hasWon(self) -> bool:
        grille = self.grille
        # check ligne
        for ligne in self.grille:
            if ligne == [2]*3:
                return True
        
        # check colonne
        for i in range(3):
            liste = []
            for k in range(3):
                liste += [grille[k][i]]
            if liste == [2]*3:
                return True
        
        # check diagonale
        liste = []
        for i in range(3):
            liste += [grille[i][i]]
            liste += [grille[2-i][i]]
        for diagonale in liste:
            if diagonale == [2]*3:
                return True
        
        return False

