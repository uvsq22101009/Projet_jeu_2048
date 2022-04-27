#########################################
# groupe n°5 - MIASHS TD2
# Gabriel PHILIPPE
# Aya Saghraoui
# Wanis Chouaib
# Furkan Toraman
#########################################

import tkinter as tk
import numpy as np
import random as rd
import pickle

#permet de savoir où placer une tuile précisement 
plateau = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]


def create_grille():
    """ Cette fonction génère une grille où peuvent se situer les tuiles """
        #1e ligne
    canvas.create_rectangle(10, 10, 120, 120 , fill="gainsboro", outline="gainsboro")
    canvas.create_rectangle(150, 10, 260, 120, fill="gainsboro", outline="gainsboro")
    canvas.create_rectangle(290, 10, 400, 120, fill="gainsboro", outline="gainsboro")
    canvas.create_rectangle(430, 10, 540, 120, fill="gainsboro", outline="gainsboro")
          #2e ligne
    canvas.create_rectangle(10, 150, 120, 260 , fill="gainsboro", outline="gainsboro")
    canvas.create_rectangle(150, 150, 260, 260, fill="gainsboro", outline="gainsboro")
    canvas.create_rectangle(290, 150, 400, 260, fill="gainsboro", outline="gainsboro")
    canvas.create_rectangle(430, 150, 540, 260, fill="gainsboro", outline="gainsboro")
    #       #3e ligne
    canvas.create_rectangle(10, 290, 120, 400 , fill="gainsboro", outline="gainsboro")
    canvas.create_rectangle(150, 290, 260, 400, fill="gainsboro", outline="gainsboro")
    canvas.create_rectangle(290, 290, 400, 400, fill="gainsboro", outline="gainsboro")
    canvas.create_rectangle(430, 290, 540, 400, fill="gainsboro", outline="gainsboro")
    #       #4e ligne
    canvas.create_rectangle(10, 430, 120, 540 , fill="gainsboro", outline="gainsboro")
    canvas.create_rectangle(150, 430, 260, 540, fill="gainsboro", outline="gainsboro")
    canvas.create_rectangle(290, 430, 400, 540, fill="gainsboro", outline="gainsboro")
    canvas.create_rectangle(430, 430, 540, 540, fill="gainsboro", outline="gainsboro")
 
def move_up():
    """ Cette fonction fera bouger les tuiles vers le haut (utiliser try 
    except peut-être) """
    global plateau
    pass 
 
def move_down():
    """ Cette fonction fera bouger les tuiles vers le bas (utiliser try 
    except peut-être) """
    global plateau
    pass 

def move_left():
    """ Cette fonction fera bouger les tuiles vers la gauche (utiliser try 
    except peut-être) """
    global plateau
    pass 

def move_right():
    """ Cette fonction fera bouger les tuiles vers la droite (utiliser try 
    except peut-être) """
    global plateau
    pass  
 
def combine():
    """ Cette fonction combinera 2 tuiles identiques """
    global plateau
    pass 

def update_score():
    """ Cette fonction actualisera le score de l'utilisateur """
    pass

def game_over():
    """ Cette fonction vérifiera si la partie est terminée """
    return False
    return True
    pass

def generate():
    """ Cette fonction génèrera une tuile située de manière aléatoire """
    global plateau
    line = rd.randint(0,3)
    col = rd.randint(0,3)
    while plateau[line][col]==0:
        line = rd.randint(0,3)
        col = rd.randint(0,3)
    tuile = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1])
    plateau[line][col] = tuile
    return plateau[line][col]
    
def start_game():
    """ Cette fonction est un regroupement de fonctions permettant à 
    l'utilisateur de jouer """
    create_grille()
    while game_over()==False:
        # move()
        # combine()
        # update_score()
        # generate()
        # game_over()
        pass
    
def exit_game():
    """ Cette fonction permet de quitter une partie """
    somme=0
    for line in plateau:
        somme+=sum(line)
    print("Vous avez quitté la partie avec un score de",somme)
    racine.destroy()

def save_game():
    """ Cette fonction permet de sauvegarder une partie """
    fic = open("save_file", "w") 
    fic.write(str(plateau))
    
def load_game():
    """ Cette fonction permet de charger une partie sauvegardée """
    fic = open("save_file", "r")   
    data2 = eval(fic.readline())


racine = tk.Tk()
racine.title("2048")
racine.geometry("900x900")

HEIGHT = 550
WIDTH = 550

#///////////BOUTON DE PREPARATION///////////
Start = tk.Button(text="Start", 
                    height=1, width=4,
                    font=("Helvetica", "15"),
                    borderwidth=10,
                    activeforeground="red",
                    activebackground="bisque2",
                    bg="bisque2",
                    command=create_grille
                  )
Start.grid(row=0, column=0)

Exit = tk.Button(text="Exit", 
                    height=1, width=4,
                    font=("Helvetica", "15"),
                    borderwidth=10,
                    activeforeground="red",
                    activebackground="bisque2",
                    bg="bisque2",
                    command=exit_game
                  )
Exit.grid(row=0, column=2)

Load = tk.Button(text="Load", 
                    height=1, width=4,
                    font=("Helvetica", "15"),
                    borderwidth=10,
                    activeforeground="red",
                    activebackground="bisque2",
                    bg="bisque2"
                  )
Load.grid(row=3, column=2)

Save = tk.Button(text="Save", 
                    height=1, width=4,
                    font=("Helvetica", "15"),
                    borderwidth=10,
                    activeforeground="red",
                    activebackground="bisque2",
                    bg="bisque2"
                  )
Save.grid(row=3, column=0)

#///////////BOUTON DE DEPLACEMENT///////////
haut = tk.Button(text="Haut", 
                    height=1, width=13,
                    font=("Helvetica", "10"),
                    activebackground="bisque2",
                    bg="bisque2",
                    command=move_up
                  )
haut.grid(row=1, column=0)

bas = tk.Button(text="Bas", 
                    height=1, width=13,
                    font=("Helvetica", "10"),
                    activebackground="bisque2",
                    bg="bisque2",
                    command=move_down
                  )
bas.grid(row=2, column=0)


droite = tk.Button(text="Droite", 
                    height=1, width=13,
                    font=("Helvetica", "10"),
                    activebackground="bisque2",
                    bg="bisque2",
                    command=move_right
                  )
droite.grid(row=1, column=2)

gauche = tk.Button(text="Gauche", 
                    height=1, width=13,
                    font=("Helvetica", "10"),
                    activebackground="bisque2",
                    bg="bisque2",
                    command=move_left
                  )
gauche.grid(row=2, column=2)


#///////////CANVAS///////////
canvas = tk.Canvas(racine, bg="NavajoWhite3", height=HEIGHT, width=WIDTH)
canvas.grid(row=1, column=1, pady=50, rowspan=3)

racine.mainloop()
