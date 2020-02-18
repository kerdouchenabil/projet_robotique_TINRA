# -*- coding: utf-8 -*-
import math 
from Obstacle import Obstacle



class Robot:

	def __init__ (self,robotID, posx, posy, direction, speed=0) :
		"""
		String x float x float x float x float -> Robot
		- nom du Robot
		- position de depart: posx et posy
		- direction: angle du vecteur vitesse (en radian)
		- vitesse de depart (nulle par defaut): speed
		"""
		self.robotID = robotID
		self.posx = posx
		self.posy = posy
		self.direction = direction 
		self.speed = speed
		self.optionPrint = True
		


#---------------------------------Mouvements---------------------------------


	def accelerate (self, acc, dt) :
		"""
		float x float ->
		acceleration (freinage si acc negatif): modification de la vitesse
		"""
		self.speed = self.speed + acc*dt
		
		if(self.optionPrint):
			if (acc>0):
				print("le robot a accelere de ",acc)
			else:
				print("le robot a freine de ", acc)
		return

	def turn(self, angle):
		"""
		float ->
		calcule la nouvelle direction du vecteur vitesse, permet au robot
		de tourner d'un certain angle (gauche si positif, droit si negatif)
		"""
		self.direction = self.direction+angle
		if(self.optionPrint):
			angleDegre = angle * (180/math.pi)
			print("le robot a tourne d un angle de ",angleDegre)
		return


	def move(self,dt):
		"""
		float ->
		calcule les nouvelles positions en x et y du robot
		"""
		self.posx = self.posx + dt * math.cos(self.direction) * self.speed
		self.posy = self.posy + dt * math.sin(self.direction) * self.speed
		return


#------------------------------fonction pour collisions--------------------------

	def possibleCollision(self,obstacle,limitx,limity):
		"""
		Obstacle x float x float -> list[float]
		avec pour parametres, l'obstacle et la distance x et y du champ de vision du robot 
		(par exemple, les coordonnees de l'arene
		calcule les coordonnees de collisions avec l'obstacle et retourne les points en x et y
		lui appartenant dans la trajectoire de l'obstacle, sous forme de liste
		cette liste est vide s'il n'y a pas eu de collisions
		"""
		i = 1
		listePos = []
		factx = (obstacle.dimx/10)* math.cos(self.direction)
		facty = (obstacle.dimx/10)* math.sin(self.direction)

		while((i*factx <= limitx) and (factx*i >= -limitx) and (facty*i <= limity) and (facty*i >= -limity)):
			x = self.posx + dt * factx
			y = self.posy + dt * facty
			
			if((x >= (obstacle.x0 - obstacle.dimx/2)) and (x <= (obstacle.x0 + obstacle.dimx/2))) :
				if ((y >= (obstacle.y0 - obstacle.dimy/2)) and (y <= (obstacle.y0 + obstacle.dimy/2))):
					listePos = [x,y]
					break
			i +=1

		
		return listePos

	def findIntersection(coor1,coor2,coor3,coor4):
		"""
		list[float] x list[float] x list[float] x list[float] -> list[float]
		trouver le point d'intersection de deux droites L1, L2:
		L1 est trace utilisant les points de coor1 et coor2
		L2 est trace utilisant les points de coor3 et coor4
		coorX[0] est la coordonnee x, coorX[1] la coordonne y 
		"""
		
		#on calcule le point x
		x = (coor1[0]*coor2[1]-coor1[1]*coor2[0])*(coor3[0]-coor4[0]) - (coor1[0]-coor2[0])*(coor3[0]*coor4[1]-coor3[1]*coor4[0])
		x = x/((coor1[0] - coor2[0])*(coor3[1]-coor4[1]) - (coor1[1] -coor2[1])*(coor3[0] - coor4[0]))

		#on calcule le point y
		y = (coor1[0]*coor2[1]-coor1[1]*coor2[0])*(coor3[1]-coor4[1]) - (coor1[1]-coor2[1])*(coor3[0]*coor4[1]-coor3[1]*coor4[0])
		y = y/((coor1[0] - coor2[0])*(coor3[1]-coor4[1]) - (coor1[1] -coor2[1])*(coor3[0] - coor4[0]))

		coor= [x,y]
	
		return coor


	def stayInObstacle(obstacle, listPos):
		return

	def calcDistance2Points(listPos1,listPos2):
		return



	def pointsCollision(self,obstacle,listPos):
		"""
		list[float]-> list[float]
		obtenir les coordonnees du point de collision à partir de points appartenant a l'obstacle
		et se trouvant sur la trajectoire du robot
		"""

		#on recupere les 4 points delimitants l'obstacle
		obsPosX1Y1 = [(obstacle.x0-obstacle.dimx/2), (obstacle.y0-obstacle.dimy/2)]
		obsPosX1Y2 = [(obstacle.x0-obstacle.dimx/2), (obstacle.y0+obstacle.dimy/2)]
		obsPosX2Y1 = [(obstacle.x0+obstacle.dimx/2), (obstacle.y0-obstacle.dimy/2)]
		obsPosX1Y2 = [(obstacle.x0+obstacle.dimx/2), (obstacle.y0+obstacle.dimy/2)]

		if(listPos[0] != posx):
			
		
		return
		

	
	def distanceRobotObs(self,arene):
		return		



#-------------------------------------Getter-------------------------------------


	def getPosX(self):
		"""
		retourne la position x
		"""
		return self.posx


	def getPosY(self):
		"""
		retourne the position y
		"""
		return self.posy
	
	
	def getDirection(self):
		"""
		retourne la direction du vecteur vitesse en radian
		"""
		return self.direction

	def getVitesse(self):
		"""
		retourne le module du vecteur vitesse
		"""
		return self.speed

	def getRobotID(self):
		"""
		recupere le nom du robot
		"""
		return self.robotID


#-------------------------------------Setter-------------------------------------


	def setPos(self,posx,posy):
		"""
		modifie les positions x et y
		"""
		self.posx=posx
		self.posy=posy

	def setPosX(self,posx):
		"""
		modifie uniquement la position x
		"""
		self.posx=posx

	def setPos(self,posy):
		"""
		modifie uniquement la position x
		"""
		self.posy=posy

	
	def setDirection(self,direction):
		"""
		modifie la direction (parametre en radian)
		"""
		self.direction=direction
		
	def setVit(self,vit):
		"""
		modifie la vitesse (module du vecteur)
		"""
		self.speed=vit

	def setRobotID(self,new_name):
		"""
		modifie le nom du robot
		"""
		self.robotID = new_name


#-----------------------------------setOption-------------------------------

	def setOptionPrintRobot(self,affiche):
		"""
		choisit ou non d'afficher les informations du robot sur le terminal
		a chaque pas de temps
			False -> n'affiche pas
			True  -> affiche
		"""
		self.optionPrint = affiche


#-----------------------------------print-----------------------------------

	
	def printRobot(self):
		"""
		affiche toutes les informations sur le Robot"
		"""
		speedx = self.speed*math.cos(self.direction)
		speedy = self.speed*math.sin(self.direction)
		angle = self.direction * (180/math.pi)
		if(self.optionPrint):
			print ("")
			print ("---------------------------------------------------------")
			print (" nom du Robot: ",self.robotID)
			print (" position = [",self.posx,",",self.posy,"]")
			print (" vitesse = ",self.speed)
			print (" direction de la vitesse(°) = ",angle)
			print ("---------------------------------------------------------")
			print ("")
		return		


	

		

