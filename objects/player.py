import pyxel
import random

class Player:
    def __init__(self, posX: int, posY: int, skinX: int, skinY: int, ) -> None:
        self.speed = 3
        self.posX = posX
        self.posY = posY
        self.skinX = skinX
        self.skinY = skinY
        self.fall = False
        self.dureeMalus = 40
        self.passTime = 0
        self.TOUCHES = {
            0: [pyxel.KEY_EXCLAIM, 0, 48, pyxel.KEY_EXCLAIM],
            1: [pyxel.KEY_P, 32, 80, pyxel.KEY_P],
            2: [pyxel.KEY_T, 16, 80, pyxel.KEY_T],
            3: [pyxel.KEY_KP_1, 16, 48, pyxel.KEY_1],
            4: [pyxel.KEY_KP_2, 32, 48, pyxel.KEY_2],
            5: [pyxel.KEY_KP_3, 0, 64, pyxel.KEY_3],
            6: [pyxel.KEY_KP_4, 16, 64, pyxel.KEY_4],
            7: [pyxel.KEY_KP_5, 32, 64, pyxel.KEY_5],
            8: [pyxel.KEY_KP_6, 0, 80, pyxel.KEY_6],
        }
        self.toucheRandom = 0

    # Dessiner le joueur en fonction de la position
    def draw(self) -> None:
        # Joueur tombé = changement de skin
        if self.fall == True and self.passTime < self.dureeMalus:
            pyxel.blt(self.posX, self.posY, 0, self.skinX, self.skinY+32, 16, 16, False)

            # Bouton à cliquer
            pyxel.blt(self.posX+16, self.posY, 0, self.TOUCHES[self.toucheRandom][1], self.TOUCHES[self.toucheRandom][2], 16, 16, False)

            self.passTime+=1
        else:
            # Skin de victoire
            if self.posX >= 240:
                 pyxel.blt(self.posX, self.posY, 0, self.skinX, self.skinY+16, 16, 16, False)
            # Skin normal
            else:
                pyxel.blt(self.posX, self.posY, 0, self.skinX, self.skinY, 16, 16, False)


    # Deplacer le joueur
    def move(self, malX) -> None:
            # Gerer la fin du jeu
            if self.posX >= 240:
                 self.speed = 0
                 return
            
            if self.posX >= malX and self.posX <= malX+1:
                if self.fall == False: self.toucheRandom = random.randint(0, len(self.TOUCHES)-1)
                self.fall = True

                if self.passTime >= self.dureeMalus:
                     self.fall = False
                     self.passTime = 0
                     self.posX -= 20

            if not self.fall: 
                 self.posX += self.speed

    def liberer(self) -> None:
         if self.passTime >= self.dureeMalus:
            self.fall = False
            self.passTime = 0
            self.posX -= 21

         if (pyxel.btnp(self.TOUCHES[self.toucheRandom][0]) or pyxel.btnp(self.TOUCHES[self.toucheRandom][3])) and self.fall:
            self.fall = False
            self.passTime = 0
            self.posX += self.speed