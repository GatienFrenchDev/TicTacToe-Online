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
        self.grille = [[0]*3]*3
        self.socket.listen()
        print(f'''
=====================
PARTIE DISPONIBLE sur
    {self.ip}
=====================
        ''')
        (sclient,adclient) = self.socket.accept()
        self.sclient = sclient
        self.main()
    
    def main(self):
        while not self.hasWon():
            data = self.sclient.recv(1024).decode()
            self.grille = json.loads(data)
            if data == "end":
                print("""
=============
TU AS PERDU !
=============
                """)
                return
            self.affichage()
            self.cocher()
            self.sclient.send(str(self.grille).encode())
        self.sclient.send("end".encode())
        

    def cocher(self):
        choix = input('Entrer la case a jouer (ex : a2): ')
        coup = (ord(choix[0].lower())-97, int(choix[1])-1)
        if self.grille[coup[0]][coup[1]] == 0:
            self.grille[coup[0]][coup[1]] = 1
        else:
            self.cocher()

    def affichage(self):
        print(self.grille)
    
    def hasWon(self) -> bool:
        grille = self.grille
        # check ligne
        for ligne in self.grille:
            if ligne == [1]*3:
                return True
        
        # check colonne
        for i in range(3):
            liste = []
            for k in range(3):
                liste += [grille[k][i]]
            if liste == [1]*3:
                return True
        
        # check diagonale
        liste = []
        for i in range(3):
            liste += [grille[i][i]]
            liste += [grille[2-i][i]]
        for diagonale in liste:
            if diagonale == [1]*3:
                return True
        
        return False