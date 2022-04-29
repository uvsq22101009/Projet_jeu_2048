import tkinter as tk
import random as rd # libraire pour choisir aléatoirement des tuiles
import numpy as np # libraire pour appliquer des probabilités sur les apparitions de tuiles
import color as c # librairie pour les couleurs des tuiles/canvas
import pickle as pc # librairie pour la sauvegarde et le chargement de parties


          
    # Interface graphique
    
racine = tk.Tk()
racine.title("2048")


    # Variables globales
        
cells = []   # contient chaque détail de chaque tuile (couleur+nombre)
matrice = [] # contient les nombres présents sur la grille
end = None   # cette variable donnera si la partie est gagnée ou perdue,
              # 1 = gagné et 0 = perdu


    # Fonctions permettant de jouer  
       
def Creation_Interface():
    # création de la plateforme de jeu
    global cells
    for i in range (4):
        row = []
        for j in range (4):
            cell_frame = tk.Frame(background, bg=c.EMPTY_CELL_COLOR, width=120, height=120)
            cell_frame.grid(row=i, column=j, padx=5, pady=5)
            cell_number = tk.Label(background, bg=c.EMPTY_CELL_COLOR)
            cell_number.grid(row=i, column=j)
            cell_data = {"frame": cell_frame, "number": cell_number}
            row.append(cell_data)
        cells.append(row)
    
    
def Actualisation_Interface(mat):
    """Cette fonction va actualiser les couleurs/affichages dans le plateau"""
    for i in range (4):
        for j in range (4):
            valeur_cell = mat[i][j]
            if valeur_cell == 0:
                cells[i][j]["frame"].config(bg=c.EMPTY_CELL_COLOR)
                cells[i][j]["number"].config(bg=c.EMPTY_CELL_COLOR, text="") 
            else:
                cells[i][j]["frame"].config(bg=c.CELL_COLORS[valeur_cell])
                cells[i][j]["number"].config(bg=c.CELL_COLORS[valeur_cell], 
                                             fg=c.CELL_NUMBER_COLORS[valeur_cell],
                                             font=c.CELL_NUMBER_FONTS[valeur_cell],
                                             text=str(valeur_cell))
    

def Generateur_Tuile(mat):
    """ Cette fonction donne à matrice une tuile créée aléatoirement"""
    row = rd.randint(0,3)
    col = rd.randint(0,3)
    while mat[row][col]!=0:
        row = rd.randint(0,3)
        col = rd.randint(0,3)
    mat[row][col] = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1])


def Empiler(mat):
    """Place les tuiles vers la gauche"""
    matrice2 = [[0]*4 for _ in range (4)]
    for i in range (4):
        pos = 0
        for j in range (4):
            if mat[i][j] != 0:
                matrice2[i][pos] = mat[i][j]
                pos+=1
    mat = matrice2
    

def Combiner(mat):
    """ Cette fonction permettra de combiner 2 tuiles de même nombre"""
    for i in range (4):
        for j in range (3):
            if mat[i][j] != 0 and mat[i][j] == mat[i][j+1]:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                

           
def Inverser(mat):
    """ Cette fonction inverse les éléments de chaque sous-liste"""
    matrice2 = []
    for i in range (4):
        matrice2.append([])
        for j in range (4):
            matrice2[i].append(mat[i][3-j])
    mat = matrice2
                    
def Transposer(mat):
    """ Cette fonction fait la transposée d'une liste"""
    matrice2 = [[0]*4 for _ in range (4)]
    for i in range (4):
        for j in range (4):
            matrice2[i][j] = mat[j][i]
    mat = matrice2
    

    # Fonctions associées aux boutons
       
def Generateur():
    """ Cette fonction génère 2 tuiles aléatoirement et les affiche dans le jeu """
    global cells
    global matrice
    # réinitialiser la plateforme de jeu ainsi que les 2 tuiles placées
    matrice = []
    cells = []
    Creation_Interface()
    
    # début du code
    matrice = [[0]*4 for _ in range (4)]
    
    # générer 2 tuiles aléatoires
    row = rd.randint(0,3)
    col = rd.randint(0,3)
    tuile = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1])
    matrice[row][col] = tuile 
    cells[row][col]["frame"].config(bg=c.CELL_COLORS[tuile])
    cells[row][col]["number"].config(bg=c.CELL_COLORS[tuile], 
                                     fg=c.CELL_NUMBER_COLORS[tuile], 
                                     font=c.CELL_NUMBER_FONTS[tuile], 
                                     text=str(tuile)
                                     )
    while matrice[row][col]!=0:
        row = rd.randint(0,3)
        col = rd.randint(0,3)
    tuile = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1])
    matrice[row][col] = tuile 
    cells[row][col]["frame"].config(bg=c.CELL_COLORS[tuile])
    cells[row][col]["number"].config(bg=c.CELL_COLORS[tuile], 
                                     fg=c.CELL_NUMBER_COLORS[tuile], 
                                     font=c.CELL_NUMBER_FONTS[tuile], 
                                     text=str(tuile)
 
                                     )
def Start_Button():
    """ Cette fonction est destinée au bouton 'Start' """
    Generateur() 

       
def Exit_Button():
    """ Cette fonction est destinée au bouton 'Exit' """
    racine.destroy()
    
    
def Save_Button():
    """ Cette fonction est destinée au bouton 'Save' """
    fic = open("save_liste.txt", "wb") 
    pc.dump(matrice, fic)
    fic.close()
    

def Load_Button():
    """ Cette fonction est destinée au bouton 'Load' """
    global matrice
    
    matrice2 = []
    fic = open("save_liste.txt", "rb")
    b = pc.load(fic)
    fic.close()
    
    for line in b:
        matrice2.append(line)
    
    matrice = matrice2

    Actualisation_Interface(matrice)
    


    # Fonctions associées aux déplacements

def Left_Button():
    try:
        Empiler(matrice)
        Combiner(matrice)
        Empiler(matrice)
        Generateur_Tuile(matrice)
        Actualisation_Interface(matrice)
        Game_Over()
    except:
        pass

def Right_Button():
    try:
        Inverser(matrice)
        Empiler(matrice)
        Combiner(matrice)
        Empiler(matrice)
        Inverser(matrice)
        Generateur_Tuile(matrice)
        Actualisation_Interface(matrice)
        Game_Over()
    except:
        pass

def Up_Button():
    try:
        Transposer(matrice)
        Empiler(matrice)
        Combiner(matrice)
        Empiler(matrice)
        Transposer(matrice)
        Generateur_Tuile(matrice)
        Actualisation_Interface(matrice)
        Game_Over()
    except:
        pass

def Down_Button():
    try:
        Transposer(matrice)
        Inverser(matrice)
        Empiler(matrice)
        Combiner(matrice)
        Empiler(matrice)
        Inverser(matrice)
        Generateur_Tuile(matrice)
        Actualisation_Interface(matrice)
        Game_Over()         
    except:
        pass
   
    
    # Fonctions associées aux tests au cours du jeu

def Mouv_Hozizontale():
    """Regarde si on peut toujours se déplacer de manière horizontale"""
    for i in range (4):
        for j in range (3):
            if matrice[i][j] == matrice[i][j+1]:
                return True
    return False

def Mouv_Verticale():
    """Regarde si on peut toujours se déplacer de manière verticale"""
    for i in range (3):
        for j in range (4):
            if matrice[i][j] == matrice[i+1][j]:
                return True
    return False

def Game_Over():
    global end
    if any(2048 in row for row in matrice):
        end = 1
        Affich_Game_Over()
    elif not any(0 in row for row in matrice) and not Mouv_Hozizontale() and not Mouv_Verticale():
        end = 0
        Affich_Game_Over()

def Affich_Game_Over(): #//créer un fond tout blanc pour afficher winner ou looser
    if end==1:
        game_over_frame = tk.Frame(background, borderwidth=2)
        game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(game_over_frame,
                 text="Winner!",
                 bg=c.WINNER_BG,
                 fg=c.GAME_OVER_FONT_COLOR,
                 font=c.GAME_OVER_FONT).pack()
    else:
        game_over_frame = tk.Frame(background, borderwidth=2)
        game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(game_over_frame,
                 text="Loser!",
                 bg=c.LOSER_BG,
                 fg=c.GAME_OVER_FONT_COLOR,
                 font=c.GAME_OVER_FONT).pack()
     
    
      
    
    # Boutons fonctionnement   
    
Start = tk.Button(text="Start", 
                    height=1, width=4,
                    font=("Helvetica", "10"),
                    command=Start_Button
                  )
Start.grid(row=0, column=0)

Exit = tk.Button(text="Exit", 
                    height=1, width=4,
                    font=("Helvetica", "10"),
                    command=Exit_Button
                  )
Exit.grid(row=1, column=0)


Save = tk.Button(text="Save", 
                    height=1, width=4,
                    font=("Helvetica", "10"),
                    command=Save_Button
                  )
Save.grid(row=0, column=1)

Load = tk.Button(text="Load", 
                    height=1, width=4,
                    font=("Helvetica", "10"),
                    command=Load_Button
                  )
Load.grid(row=1, column=1)


    # Boutons déplacement  
    
Haut = tk.Button(text="Up", 
                    height=1, width=4,
                    font=("Helvetica", "10"),
                    command=Up_Button
                  )
Haut.grid(row=0, column=16)

Bas = tk.Button(text="Down", 
                    height=1, width=4,
                    font=("Helvetica", "10"),
                    command=Down_Button
                  )
Bas.grid(row=2, column=16)


Gauche = tk.Button(text="Left", 
                    height=1, width=4,
                    font=("Helvetica", "10"),
                    command=Left_Button
                  )
Gauche.grid(row=1, column=15)

Droite = tk.Button(text="Right", 
                    height=1, width=4,
                    font=("Helvetica", "10"),
                    command=Right_Button
                  )
Droite.grid(row=1, column=17)


    # Background
        
background = tk.Frame(racine, 
                bg=c.GRID_COLOR, 
                bd=3, width=570, 
                height=570
)
                
background.grid(pady=100, columnspan=20) #columnspan=20 pour placer correctement les boutons



Creation_Interface()


racine.mainloop()