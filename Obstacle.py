import math


class Obstacle:


	def __init__(self,x0,y0,dimx,dimy):
		"""
		obstacle caracterise par les attributs:
		- position de son centre en x et y: x0 et y0
		- longueur et largeur selon y et y: dimx et dimy
		"""
		self.x0 = x0
		self.y0 = y0
		self.dimx = dimx
		self.dimy = dimy




#-------------------------------------Getter-------------------------------------

	def getObstaclePosX(self):
		return self.x0
	

	def getObstaclePosY(self):
		return self.y0

	def getDimX(self):
		return self.dimx

	def getDimY(self):
		return self.dimy



#-------------------------------------Setter-------------------------------------



