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
score = 0    # contient le score
end = None   # cette variable donnera si la partie est gagnée ou perdue,
              # 1 = gagné et 0 = perdu


    # Fonctions permettant de jouer  
       
def creer_plat():
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
        
    # création du tableau de score
    score_frame = tk.Frame()
    score_frame.place(relx=0.5, y=45, anchor="center")
    tk.Label(score_frame, text="Score", font=c.SCORE_LABEL_FONT).grid(row=0)
    score_label = tk.Label(score_frame, text=str(score), font=c.SCORE_FONT)
    score_label.grid(row=1)
    
    
def actualiser_plat(mat):
    """Cette fonction va actualiser les couleurs/affichages dans le plateau"""
    global score_label
    for i in range (4):
        for j in range (4):
            valeur_cell = mat[i][j]
            if valeur_cell == 0:
                cells[i][j]["frame"].config(bg=c.EMPTY_CELL_COLOR)
                cells[i][j]["number"].config(bg=c.CELL_COLORS, text="")
            else:
                cells[i][j]["frame"].config(bg=c.CELL_COLORS[valeur_cell])
                cells[i][j]["number"].config(bg=c.CELL_COLORS[valeur_cell], 
                                                 fg=c.CELL_NUMBER_COLORS[valeur_cell],
                                                 font=c.CELL_NUMBER_FONTS[valeur_cell],
                                             text=str(valeur_cell))
    

def creer_tuile():
    """ Cette fonction donne à matrice une tuile créée aléatoirement"""
    row = rd.randint(0,3)
    col = rd.randint(0,3)
    while matrice[row][col]!=0:
        row = rd.randint(0,3)
        col = rd.randint(0,3)
    matrice[row][col] = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1])


def empiler(mat):
    """Place les tuiles vers la gauche"""
    matrice2 = [[0]*4 for _ in range (4)]
    for i in range (4):
        pos = 0
        for j in range (4):
            if mat[i][j] != 0:
                matrice2[i][pos] = mat[i][j]
                pos+=1
    mat = matrice2
    

def combiner(mat):
    """ Cette fonction permettra de combiner 2 tuiles de même nombre"""
    global score
    for i in range (4):
        for j in range (3):
            if mat[i][j] != 0 and mat[i][j] == mat[i][j+1]:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                score += mat[i][j]



           
def inverse(mat):
    """ Cette fonction inverse les éléments de chaque sous-liste"""
    matrice2 = []
    for i in range (4):
        matrice2.append([])
        for j in range (4):
            matrice2[i].append(mat[i][3-j])
    mat = matrice2
                    
def transpose(mat):
    """ Cette fonction fait la transposée d'une liste"""
    matrice2 = [[0]*4 for _ in range (4)]
    for i in range (4):
        for j in range (4):
            matrice2[i][j] = mat[j][i]
    mat = matrice2
    

    # Fonctions associées aux boutons
       
def start():
    global cells
    global matrice
    # réinitialiser la plateforme de jeu ainsi que les 2 tuiles placées
    matrice = []
    cells = []
    creer_plat()
    
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
       
def exit_game():
    # fermer la fenêtre graphique
    racine.destroy()
    
def save_game():
    # sauvegarder une partie dans un fichier texte
    fic = open("save_liste.txt", "wb") 
    pc.dump(matrice, fic)
    fic.close()
    
    # sauvegarder un score dans un fichier texte
    fic = open("save_score.txt", "wb") 
    pc.dump(score, fic)
    fic.close()

def load_game():
    # charger une partie provenant d'un fichier texte
    global matrice, score
    
    fic = open("save_liste.txt", "rb")
    b = pc.load(fic)
    fic.close()
    
    for line in b:
        matrice.append(line)
    
    # charger un score provenant d'un fichier texte
    fic = open("save_score.txt", "rb")
    b = pc.load(fic)
    fic.close()
        
    score = b

    creer_plat()
    actualiser_plat(matrice)
    


    # Fonctions associées aux déplacements

def left_move():
    empiler(matrice)
    combiner(matrice)
    empiler(matrice)
    creer_tuile()
    actualiser_plat()
    game_over()

def right_move():
    inverse(matrice)
    empiler(matrice)
    combiner(matrice)
    empiler(matrice)
    inverse(matrice)
    creer_tuile()
    actualiser_plat()
    game_over()

def up_move():
    transpose(matrice)
    empiler(matrice)
    combiner(matrice)
    empiler(matrice)
    transpose(matrice)
    creer_tuile()
    actualiser_plat()
    game_over()

def down_move():
    transpose(matrice)
    inverse(matrice)
    empiler(matrice)
    combiner(matrice)
    empiler(matrice)
    inverse(matrice)
    creer_tuile()
    actualiser_plat()
    game_over()
    
    
    # Fonctions associées aux tests au cours du jeu

def mouv_hozizontale():
    """Regarde si on peut toujours se déplacer de manière horizontale"""
    for i in range (4):
        for j in range (3):
            if matrice[i][j] == matrice[i][j+1]:
                return True
    return False

def mouv_verticale():
    """Regarde si on peut toujours se déplacer de manière verticale"""
    for i in range (3):
        for j in range (4):
            if matrice[i][j] == matrice[i+1][j]:
                return True
    return False

def game_over():
    global end
    if any(2048 in row for row in matrice):
        end = 1
        return True
    elif not any(0 in row for row in matrice) and not mouv_hozizontale() and not mouv_verticale():
        end = 0
        return True
    return False

def print_game_over():
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


#/////////////////////FONCTION FINALE//////////////
def main():
    """ Cette fonction regroupera les fonctions permettant de jouer"""
    start()
    # while game_over()==False:
    #     if '<KeyPress-Up>':
    #         up_move()
    #     elif '<KeyPress-Down>':
    #         down_move()
    #     elif '<KeyPress-Right>':
    #         right_move()
    #     elif '<KeyPress-Left>':
    #         left_move()
    # print_game_over()        
    
    
    
    
    
    # Boutons    
    
Start = tk.Button(text="Start", 
                    height=1, width=4,
                    font=("Helvetica", "10"),
                    command=main
                  )
Start.grid(row=0, column=0)

Exit = tk.Button(text="Exit", 
                    height=1, width=4,
                    font=("Helvetica", "10"),
                    command=exit_game
                  )
Exit.grid(row=1, column=0)


Save = tk.Button(text="Save", 
                    height=1, width=4,
                    font=("Helvetica", "10"),
                    command=save_game
                  )
Save.grid(row=0, column=2)

Load = tk.Button(text="Load", 
                    height=1, width=4,
                    font=("Helvetica", "10"),
                    command=load_game
                  )
Load.grid(row=1, column=2)


    # Background
        
background = tk.Frame(racine, 
                bg=c.GRID_COLOR, 
                bd=3, width=570, 
                height=570
)
                
background.grid(pady=100, columnspan=3)



creer_plat()



racine.mainloop()