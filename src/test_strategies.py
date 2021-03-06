#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from controleur.ai import *
from objet.arene import *
from objet.obstacle import *
'''
    initialisation des attributs de depart
'''
robID= 0
robPosX= 100
robPosY= 300
robDir= 0
robVitesse= 0

areneLongeur= 500
areneLargeur= 500


'''
    creation du robot ID=0  position=[50;50]  direction=0 (droite)  vitesse=0
'''
rob = Robot(robID, robPosX, robPosY, robDir, robVitesse)
'''
    creation des murs
'''

longeurMur=areneLongeur
largeurMur=10
mur_haut=Obstacle(longeurMur/2,0+largeurMur/2,longeurMur,largeurMur)
mur_bas=Obstacle(longeurMur/2,longeurMur-largeurMur/2,longeurMur,largeurMur)
mur_gauche=Obstacle(0+largeurMur/2,longeurMur/2,largeurMur,longeurMur)
mur_droite=Obstacle(longeurMur-largeurMur/2,longeurMur/2,largeurMur,longeurMur)




'''
    creation d'une arene
'''
arene = Arene(areneLongeur, areneLargeur)


'''
ajout du robot et des murs dans l'arene 
'''
arene.addObstacle(mur_haut)
arene.addObstacle(mur_bas)
arene.addObstacle(mur_gauche)
arene.addObstacle(mur_droite)
arene.addRobot(rob)
'''
creation des stratégies pour faire un carée
'''
toutdroit = go_ahead_strategy(rob,100)
tournedroite = turn_right_strategy(rob,90)
tournegauche = turn_left_strategy(rob,90)

'''
print("__________ go_ahead_strategy __________")
toutdroit.start()
arret = False
while(arret==False):
   toutdroit.step()
   rob.printRobot()
   arret=toutdroit.stop()

print("")
print("__________ turn_right_strategy __________")
tournedroite.start()
arret = False
while(arret==False):
   tournedroite.step()
   rob.printRobot()
   arret=tournedroite.stop()

print("")
print("__________ turn_left_strategy __________")
tournegauche.start()
arret = False
while(arret==False):
   tournegauche.step()
   rob.printRobot()
   arret=tournegauche.stop()
'''   

fairecarre = square_right_strategy(rob, 100, 200, 100)
print("")
print("__________ square_right_strategy __________")
fairecarre.start()
arret = False
while(arret==False):
   fairecarre.step()
   rob.printRobot()
   arret=fairecarre.stop()

