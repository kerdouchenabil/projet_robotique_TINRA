# -*- coding: utf-8 -*-

from Robot import Robot
from Arene import Arene
from Obstacle import Obstacle


'''
    le main du projet qui relie toutes les instances
    cree des instances de Robot, Arene, Obstacles, Affichage
    ajoute les Robots et Obstacles dans l'Arene
    
'''

'''
    initialisatin des attributs de depart
'''
robID= 0
robPosX= 370
robPosY= 143
robDir= 1
robVitesse= 1

areneLongeur= 400
areneLargeur= 400


'''
    creation du robot ID=0  position=[5;5]  direction=0 (droite)  vitesse=0
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
pcd=rob.possibleCollision(mur_droite,20,20)
pcb=rob.possibleCollision(mur_bas,20,20)
pcg=rob.possibleCollision(mur_gauche,20,20)
pch=rob.possibleCollision(mur_haut,20,20)
arene.printAll()
print("")
print("possible collision ")
print("mur de droite ",pcd)
print("mur du bas",pcb)
print("mur de gauche ",pcg)
print("mur du haut ",pch)

for i in range(0,20000):
    pcd=rob.possibleCollision(mur_droite,20,20)
    pcb=rob.possibleCollision(mur_bas,20,20)
    pcg=rob.possibleCollision(mur_gauche,20,20)
    pch=rob.possibleCollision(mur_haut,20,20)
    rob.uptade(pcg,pcd,pch,pcb)
    rob.printRobot()
