# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from objet.arene import *
from objet.robot import *
from objet.obstacle import *

class Affichage2D:
    
    def __init__(self, arene):
        
        self.arene = arene
        self.robot = arene.listeRobot[0]
        
        self.mur0 = self.arene.listeObst[0] # premier obstacle de la listeObst
        self.mur1 = self.arene.listeObst[1] # 2eme obstacle
        self.mur2 = self.arene.listeObst[2] # 3eme obstacle
        self.mur3 = self.arene.listeObst[3] # 4eme obstacle
        
        self.window = 0
        self.width = arene.largeur
        self.height = arene.longueur
        
        
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("Affichage2D")
        glutDisplayFunc(self.draw)
        glutIdleFunc(self.draw)
        glutMainLoop()
        
        
    def drawRect(self, x, y, width, height):
        glBegin(GL_QUADS)                       #signaler a opengl que on va dessiner un rectangle (GL_QUADS)
        glVertex2f(x, y)                        #dessine les 4 vectrices
        glVertex2f(x + width, y)
        glVertex2f(x + width, y + height)
        glVertex2f(x, y + height)
        glEnd()                                 #signale la fin du dessin

    
    def refresh2d(self):
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.width, 0.0, self.height, 0.0, 1.0)
        glMatrixMode (GL_MODELVIEW)
        glLoadIdentity()
        
        
    def drawArene(self):
        #dessin mur0
        self.drawRect(self.mur0.x0, self.mur0.y0, self.mur0.dimx, self.mur0.dimy)    
        #print("drawArene", self.mur0.x0, self.mur0.y0, self.mur0.dimx, self.mur0.dimy) 
        
        #dessin mur1
        self.drawRect(self.mur1.x0, self.mur1.y0, self.mur1.dimx, self.mur1.dimy) 
        
        #dessin mur2
        self.drawRect(self.mur2.x0, self.mur2.y0, self.mur2.dimx, self.mur2.dimy) 
        
        #dessin mur3
        self.drawRect(self.mur3.x0, self.mur3.y0, self.mur3.dimx, self.mur3.dimy) 
        

    def drawRobot(self):
        #on suppose que longueur, largeur du robot = 20 x 20
        self.drawRect(self.robot.posx, self.robot.posy, 20, 20)  
        print("drawRobot", self.robot.posx, self.robot.posy, 20, 20)  
        
        
    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.refresh2d()
        
        #dessin de l'Arene avec les obstacles
        glColor3f(1.0, 0.0, 0.0)
        self.drawArene()
        
        #dessin du robot
        glColor3f(1.0, 1.0, 1.0)
        self.drawRobot()

        glutSwapBuffers()
        
        #update du Robot
        #self.robot.updateTest()
        
        pcd=self.robot.possibleCollision(mur2,20,20)
        pcb=self.robot.possibleCollision(mur1,20,20)
        pcg=self.robot.possibleCollision(mur0,20,20)
        pch=self.robot.possibleCollision(mur3,20,20)
        self.robot.update(pcg,pcd,pch,pcb)
        
        
        
        
#---------------------------------------testing------------------------        
arene1= Arene(400, 400)

rob= Robot(0,200,200,0,10)
arene1.addRobot(rob)

mur0= Obstacle(0,0,20,400) #g
mur1= Obstacle(0,0,400,20) #b
mur2= Obstacle(380,0,20,400) #d
mur3= Obstacle(0,380,400,20) #h

arene1.addObstacle(mur0)
arene1.addObstacle(mur1)
arene1.addObstacle(mur2)
arene1.addObstacle(mur3)

arene1.printAll()



affich= Affichage2D(arene1)
print("affichage2D: longueur=", affich.width, "largeur=", affich.height)

       

        
        
