# -*- coding: utf-8 -*-

from objet.robot import *
from objet.arene import *
from objet.obstacle import *


'''
    le main du projet qui relie toutes les instances
    cree des instances de Robot, Arene, Obstacles, Affichage
    ajoute les Robots et Obstacles dans l'Arene
    
'''

'''
    initialisation des attributs de depart
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



for i in range(0,1000):
	
	pcd=rob.possibleCollision(mur_droite,20,20)
	pcb=rob.possibleCollision(mur_bas,20,20)
	pcg=rob.possibleCollision(mur_gauche,20,20)
	pch=rob.possibleCollision(mur_haut,20,20)
	rob.update(pcg,pcd,pch,pcb)
	rob.printRobot()
	
	rob.update(pcg,pcd,pch,pcb)
    
    
    
'''
    
'''   

