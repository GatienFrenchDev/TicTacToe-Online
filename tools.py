import os

def affichage(grille):
    valeur = [[0]*3, [0]*3, [0]*3]
    os.system('cls' if os.name=='nt' else 'clear')
    dico = {
            0 : " ",
            1 : "X",
            2 : "O"

        }

    for i in range(len(grille)):
        for j in range(len(grille[i])):
            valeur[i][j] = dico[grille[i][j]]

    return f"""
   a     b     c
      |     |     
1  {valeur[0][0]}  |  {valeur[0][1]}  |  {valeur[0][1]}  
 _____|_____|_____
      |     |     
2  {valeur[1][0]}  |  {valeur[1][1]}  |  {valeur[1][2]}  
 _____|_____|_____
      |     |     
3  {valeur[2][0]}  |  {valeur[2][1]}  |  {valeur[2][2]}  
      |     |     

        """
