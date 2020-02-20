# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Arene import Arene
from Robot import Robot
from Obstacle import Obstacle

class Affichage2D:
    
    def __init__(self, arene):
        
        self.arene = arene
        self.robot = arene.getRobot0()
        
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
        
        