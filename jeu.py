from serveur import Serveur
from client import Client

class Jeu:
    def __init__(self):
        pass

    def menu(self):
        print('''                                   
  __  __              _          
 |  \/  |___ _ _ _ __(_)___ _ _  
 | |\/| / _ \ '_| '_ \ / _ \ ' \  
 |_|  |_\___/_| | .__/_\___/_||_|
                |_|              

    1. Héberger une partie
    2. Rejoindre une partie''')
        entree = input('\nTapez 1 ou 2 : ')
        if entree == '1':
            self.serveur()
        elif entree == '2':
            print('''
Entrer l'IP de la partie : ''')
            ip = input('')
            self.client(ip)
        else:
            self.menu()

    def serveur(self):
        self.serveur = Serveur(8080)
    
    def client(self, ip):
        self.ip_serv = ip
        self.client = Client(self.ip_serv)


jeu = Jeu()
jeu.menu()