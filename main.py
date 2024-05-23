import pyxel
from objects.player import Player
import variables as var
import random

# Initialisation Pyxel
pyxel.init(var.WIN_WIDTH, var.WIN_HEIGHT)

# [------- Variables de touche aléatoire pour les events -------]

# Charger le fichier de ressource
fichierSKINS = pyxel.load("SKINS.pyxres")

# Initialisation des joueurs
p1 = Player(2, 25, 0, 0)
p2 = Player(2, 51, 16, 0)
p3 = Player(2, 75, 32, 0)

# [--------------------------------------------------------------]


# [---------------- FONCTIONS DU JEU ----------------]

    

def handleMovements(): # Supporter les touches pour les mouvements
    # Joueur 1
    if pyxel.btnp(pyxel.KEY_D):
        p1.move(100)
    if pyxel.btnp(pyxel.KEY_M):
        p2.move(100)
    if pyxel.btnp(pyxel.KEY_KP_PLUS):
        p3.move(100)


    if pyxel.btnp(pyxel.KEY_ESCAPE):
        quit()

# [--------------------------------------------------]

# [-------------- FONCTIONS AU DEMARAGE --------------]


# [--------------------------------------------------]


# [-------------- FONCTIONS PRINCIPALES --------------]
def update():
    # Ecouter les mouvements de chaque joueurs
    handleMovements()


# Redissiner chaque éléments à chaque x instant de la boucle
def draw():
    # Image de fond
    pyxel.blt(0, 0, 0, 0, 96, 256, 120, False)

    # Redessiner les joueurs à chaque frame
    p1.draw()
    p1.liberer()
    p2.draw()
    p2.liberer()
    p3.draw()
    p3.liberer()

pyxel.run(update, draw)
# [--------------------------------------------------]
