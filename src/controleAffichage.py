# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from graphical_engine.engine2D.affichageArene import *
from objet.arene import *
from objet.robot import *
from objet.obstacle import *

#-------------------------------------------------------------
# construit l'arene  
#-------------------------------------------------------------
arene1= Arene(400, 400)

rob= Robot(0,200,200,10,1)
arene1.addRobot(rob)

mur0= Obstacle(10,200,20,400) #g
mur1= Obstacle(200,10,400,20) #b
mur2= Obstacle(390,200,20,400) #d
mur3= Obstacle(200,390,400,20) #h

arene1.addObstacle(mur0)
arene1.addObstacle(mur1)
arene1.addObstacle(mur2)
arene1.addObstacle(mur3)


#-------------------------------------------------------------
# option pour l'affichage des informations sur l'arene 
# True ou False pour activer/desactiver; respectivement:
# 1 -> arene
# 2 -> robots
# 3 -> actions du robot
# 4 -> obstacles
#-------------------------------------------------------------
arene1.setOptionPrint(True,False,True,True)
arene1.printAll()


#-------------------------------------------------------------
# parametre pour le test  
#-------------------------------------------------------------
dt = 0.1		# pas de temps
distanceLimite = 20	# distance minimale avec le mur avant que le robot change de direction
angleTourne = 60	# le robot tourne de cet angle 


#-------------------------------------------------------------
# debut du test  
#-------------------------------------------------------------
affichage= Affichage2D(arene1,dt,angleTourne,distanceLimite)
glutMainLoop()  
    


	




       

        
        
