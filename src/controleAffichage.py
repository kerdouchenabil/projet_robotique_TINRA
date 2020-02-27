# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from graphical_engine.engine2D.affichageArene import *
from objet.arene import *
from objet.robot import *
from objet.obstacle import *

     
arene1= Arene(400, 400)

rob= Robot(0,200,200,0,1)
arene1.addRobot(rob)

mur0= Obstacle(10,200,20,400) #g
mur1= Obstacle(200,10,400,20) #b
mur2= Obstacle(390,200,20,400) #d
mur3= Obstacle(200,390,400,20) #h

arene1.addObstacle(mur0)
arene1.addObstacle(mur1)
arene1.addObstacle(mur2)
arene1.addObstacle(mur3)

arene1.printAll()



affich= Affichage2D(arene1)

glutMainLoop()  
    


	


#print("affichage2D: longueur=", affich.width, "largeur=", affich.height)

       

        
        
