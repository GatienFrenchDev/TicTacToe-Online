import os

def affichage(grille):
    os.system('cls' if os.name=='nt' else 'clear')
    dico = {
            0 : " ",
            1 : "X",
            2 : "O"

        }

    for i in range(len(grille)):
        for j in range(len(grille[i])):
            grille[i][j] = dico[grille[i][j]]

    return f"""
    a     b     c
        |     |     
    1  {grille[0][0]}  |  {grille[0][1]}  |  {grille[0][2]}  
    _____|_____|_____
        |     |     
    2  {grille[1][0]}  |  {grille[1][1]}  |  {grille[1][2]}
    _____|_____|_____
        |     |     
    3  {grille[2][0]}  |  {grille[2][1]}  |  {grille[2][2]}  
        |     |     
        """
