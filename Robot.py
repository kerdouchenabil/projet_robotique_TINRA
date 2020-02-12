from math import *
import math


class Robot:
    '''
    classe qui represente le robot,
    représenté par un point
    il dispose d'un attribut direction de type Vecteur (pour l'instant dx,dy)
    Constructeur qui initialise ce point, sa direction, et lui donne un nom
    il se déplace avec l'appel des fonctions de déplacement,
    ses coords sont mises à jour après chaque déplacement.

    '''

    def __init__(self, x, y, nom):
        self.x = x
        self.y = y
        self.nom = nom
        self.dx = 1.5  # initialisation de la direction à [1,0] (à droite)
        self.dy = 1

    def affiche(self):
        print("Robot [ x=", self.x, "; y=", self.y, "]")

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDX(self):
        return self.dx

    def getDY(self):
        return self.dy

    def setPos(self, newx, newy):
        self.x = newx
        self.y = newy

    def setDir(self, newdx, newdy):
        self.dx = newdx
        self.dy = newdy

    # avance selon la direction (dx,dy)
    def avance(self):
        self.setPos(self.x + self.dx, self.y + self.dy)

    def recule(self):  # si le robot fait marche arrière
        self.setPos(self.x - self.dx, self.y - self.dy)

    def tournerDroite(self):
        '''
            tourner d'un angle th= +math.pi/2
        '''
        # cosx= cos(self.dx)
        # sinx= sin(self.dy)
        newdx = self.dx * cos(math.pi / 2) - self.dy * sin(math.pi / 2)
        newdy = self.dx * sin(math.pi / 2) + self.dy * cos(math.pi / 2)
        self.setDir(newdx, newdy)

    def tournerGauche(self):
        '''
            tourner d'un angle th= -math.pi/2
        '''
        # cosx= cos(self.dx)
        # sinx= sin(self.dy)
        newdx = self.dx * cos(-math.pi / 2) - self.dy * sin(-math.pi / 2)
        newdy = self.dx * sin(-math.pi / 2) + self.dy * cos(-math.pi / 2)
        self.setDir(newdx, newdy)


