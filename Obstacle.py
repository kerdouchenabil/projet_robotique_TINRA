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


#------------------------------------Fonction-----------------------------------
		
	def pointInObstacle(self,x,y):
		"""
		calcule si le point (x,y) se trouve dans l'obstacle
		"""
		incertitude = 10**(-6)
		xmin = self.x0 - (self.dimx/2 *(1 + incertitude))
		xmax = self.x0 + (self.dimx/2 *(1 + incertitude))
		ymin = self.y0 - (self.dimy/2 *(1 + incertitude))
		ymax = self.y0 + (self.dimy/2 *(1 + incertitude))
		if ((x >= xmin) and (x <= xmax)):
			if ((y >= ymin) and (y <=ymax)):
				return True 
		return False

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

	def setObstaclePos(self,x,y):
		"""
		modifie la position de l'obstacle
		"""
		self.x0 = x
		self.y0 = y
		return

	def setObstacleDim(self,x,y):
		"""
		modifie les dimensions de l'obstacle
		"""
		self.dimx = x
		self.dimy = y
		return





