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
		self.window = 0
		self.width = arene.largeur
		self.height = arene.longueur

		# initialisation
		glutInit()

		#parametre pour l'ouverture de la fenetre
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
		glutInitWindowSize(self.width, self.height)
		glutInitWindowPosition(0, 0)

		#creation de la fenetre
		glutCreateWindow("Affichage2D")
		glutDisplayFunc(self.draw)
		glutIdleFunc(self.animation)
		
        


        
	def drawRect(self, x, y, wdth, hght):
		glBegin(GL_QUADS)           #signaler a opengl que on va dessiner un rectangle (GL_QUADS)
		glVertex2f(x - wdth/2, y - hght/2)      #dessine les 4 vectrices
		glVertex2f(x + wdth/2, y - hght/2)
		glVertex2f(x + wdth/2, y + hght/2)
		glVertex2f(x - wdth/2, y + hght/2)
		glEnd()                                 #signale la fin du dessin

    
	def refresh2d(self):
		glViewport(0, 0, self.width, self.height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(0.0, self.width, 0.0, self.height, 0.0, 1.0)
		glMatrixMode (GL_MODELVIEW)
		glLoadIdentity()


	def drawRobot(self,rob):
		self.drawRect(rob.posx,rob.posy, 20, 20)

	def drawObstacle(self,obst):
		self.drawRect(obst.x0, obst.y0, obst.dimx, obst.dimy)

	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		self.refresh2d()
        
		#dessin de l'Arene avec les obstacles
		glColor3f(1.0, 0.0, 0.0)
		for obst in self.arene.listeObst:
			self.drawObstacle(obst)
        
		#dessin du robot
		glColor3f(1.0, 1.0, 1.0)
		for rob in self.arene.listeRobot:
			self.drawRobot(rob)

		glutSwapBuffers() 


	def animation(self):
		"""
		rob = self.arene.listeRobot[0]
		mur0= self.arene.listeObst[0]
		mur1= self.arene.listeObst[1]
		mur2= self.arene.listeObst[2]
		mur3= self.arene.listeObst[3]
		pcd=rob.possibleCollision(mur2,20,20)
		pcb=rob.possibleCollision(mur1,20,20)
		pcg=rob.possibleCollision(mur0,20,20)
		pch=rob.possibleCollision(mur3,20,20)

		rob.update(pcg,pcd,pch,pcb)	
		"""
		self.arene.update(0.5,20)
		self.arene.listeRobot[0].printRobot()
		glutPostRedisplay()	




       

        
        
