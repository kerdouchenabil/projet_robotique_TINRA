# -*- coding: utf-8 -*-
import math 
from .obstacle import Obstacle



class Robot:

	def __init__ (self,robotID, posx, posy, direction, speed=0) :
		"""
		String x float x float x float x float -> Robot
		- nom du Robot
		- position de depart: posx et posy
		- direction: angle du vecteur vitesse (en degre)
		- vitesse de depart (nulle par defaut): speed
		"""
		self.robotID = robotID
		self.posx = posx
		self.posy = posy
		self.direction = direction*(math.pi/180)
		self.speed = speed
		self._optionAffichageR = True
		


#---------------------------------Mouvements---------------------------------


	def accelerate (self, acc, dt) :
		"""
		float x float ->
		acceleration (freinage si acc negatif): modification de la vitesse
		"""
		self.speed = self.speed + acc*dt
		
		if(self._optionAffichageR):
			if (acc>0):
				print("le robot a accelere de ",acc)
			else:
				print("le robot a freine de ", -acc)
		return

	def turn(self, angle):
		"""
		float ->
		calcule la nouvelle direction du vecteur vitesse, permet au robot
		de tourner d'un certain angle (gauche si positif, droit si negatif)
		"""
		self.direction = self.direction+(angle*math.pi/180)
		self.direction = self.direction % (2*math.pi)
		if(self._optionAffichageR):
			print("le robot a tourne d un angle de ",angle)
		return


	def move(self,dt):
		"""
		float ->
		calcule les nouvelles positions en x et y du robot
		"""
		self.posx = self.posx + dt * math.cos(self.direction) * self.speed
		self.posy = self.posy + dt * math.sin(self.direction) * self.speed
		return


	def update(self,possibecolG,possibecolD,possibecolH,possibecolB):
		"""
		met à jour les coords du robot 
        	 """
		if (len(possibecolG)==0):
			self.move(0.1)
			if (len(possibecolD)==0):
				self.move(0.1)
				if (len(possibecolH)==0):
					self.move(0.1)
					if (len(possibecolB)==0):
						self.move(0.1)
		         
					else:
						self.turn(180)        
				else:
					self.turn(180)
			else:
				self.turn(180)
		         
		else:
			self.turn(180)
            
		
              
             
		
			
#------------------------------fonction pour collisions--------------------------



	def findIntersection(self,coor2,coor3,coor4):
		"""
		list[float] x list[float] x list[float] x list[float] -> list[float]
		trouver le point d'intersection de deux droites L1, L2:
		L1 est trace utilisant les points de Robot et coor2
		L2 est trace utilisant les points de coor3 et coor4
		coorX[0] est la coordonnee x, coorX[1] la coordonne y 
		"""
		
		#on s'assure que L1 et L2 ne soit pas parallele sinon la liste est vide:
		zero = (self.posx-coor2[0])*(coor3[1]-coor4[1]) - (self.posy- coor2[1])*(coor3[0]-coor4[0])
		if (zero == 0):
			coor = []
			return 	coor	
		
		#on calcule le point x
		x = (self.posx*coor2[1]-self.posy*coor2[0])*(coor3[0]-coor4[0]) - (self.posx-coor2[0])*(coor3[0]*coor4[1]-coor3[1]*coor4[0])
		x = x/((self.posx - coor2[0])*(coor3[1]-coor4[1]) - (self.posy -coor2[1])*(coor3[0] - coor4[0]))

		#on calcule le point y
		y = (self.posx*coor2[1]-self.posy*coor2[0])*(coor3[1]-coor4[1]) - (self.posy-coor2[1])*(coor3[0]*coor4[1]-coor3[1]*coor4[0])
		y = y/((self.posx - coor2[0])*(coor3[1]-coor4[1]) - (self.posy -coor2[1])*(coor3[0] - coor4[0]))

		coor= [x,y]
	
		return coor



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
		factx = (obstacle.dimx/50)* math.cos(self.direction)
		facty = (obstacle.dimx/50)* math.sin(self.direction)

		while((i*factx <= limitx) and (factx*i >= -limitx) and (facty*i <= limity) and (facty*i >= -limity)):
			x = self.posx + i*factx
			y = self.posy + i*facty
			tof = obstacle.pointInObstacle(x,y)
			if(tof == True):
				listePos = [x,y]
				break
			i +=1
		
		return listePos


	def distancePointRobot(self,listpos):
		'''
		calcule la distance d un point avec le robot
		'''
		return math.sqrt((listpos[0] - self.posx)**2 + (listpos[1] - self.posy)**2)



	def pointsCollision(self,obstacle,listPos):
		"""
		list[float]-> list[float]
		obtenir les coordonnees du point de collision à partir de points trouves avec la fonction
		possibleCollision
		"""

		#on recupere les 4 points delimitants l'obstacle
		obsPosx1y1 = [(obstacle.x0-obstacle.dimx/2), (obstacle.y0-obstacle.dimy/2)]
		obsPosx1y2 = [(obstacle.x0-obstacle.dimx/2), (obstacle.y0+obstacle.dimy/2)]
		obsPosx2y1 = [(obstacle.x0+obstacle.dimx/2), (obstacle.y0-obstacle.dimy/2)]
		obsPosx2y2 = [(obstacle.x0+obstacle.dimx/2), (obstacle.y0+obstacle.dimy/2)]

		dist = -1
		coor = []

		coor2 = self.findIntersection(listPos,obsPosx1y1,obsPosx1y2)
		dist2 = self.distancePointRobot(coor2)
		if(obstacle.pointInObstacle(coor2[0],coor2[1]) and (dist2 < dist or dist == -1)):
			dist = dist2
			coor = coor2
		

		coor2 = self.findIntersection(listPos,obsPosx1y2,obsPosx2y2)
		dist2 = self.distancePointRobot(coor2)
		if(obstacle.pointInObstacle(coor2[0],coor2[1]) and (dist2 < dist or dist == -1)):
			dist = dist2
			coor = coor2
		

		coor2 = self.findIntersection(listPos,obsPosx2y2,obsPosx2y1)
		dist2 = self.distancePointRobot(coor2)
		if(obstacle.pointInObstacle(coor2[0],coor2[1]) and (dist2 < dist or dist == -1)):
			dist = dist2
			coor = coor2
		


		coor2 = self.findIntersection(listPos,obsPosx2y1,obsPosx1y1)
		dist2 = self.distancePointRobot(coor2)
		if(obstacle.pointInObstacle(coor2[0],coor2[1]) and (dist2 < dist or dist == -1)):
			dist = dist2
			coor = coor2

		return coor

		

	
	def distanceRobotObs(self,arene):
		'''
		retourne la distance de l'obstacle le plus proche qui se trouve au travers de sa trajectoire
		s'il n'y a pas d'obstacle, la valeur sera negative
		'''
		listobst = arene.getListObstacle()
		dist = -1
		coor = []
		for obstacle in listobst:
			listpos = self.possibleCollision(obstacle,arene.longueur, arene.largeur) 
			if (len(listpos) == 2):  # si obstacle est dans la trajectoire de robot
				listpos = self.pointsCollision(obstacle,listpos) # calcule le point de collision entre robot et obstacle
				dist_int = self.distancePointRobot(listpos)  # calcule la distance entre robot et point de collision
				if (dist_int < dist or dist == -1):
					dist = dist_int
					coor = listpos
		
		if(self._optionAffichageR):
			if(dist == -1):
				print ("")
				print (" le robot ",self.robotID, "n'a aucun obstacles dans sa trajectoire")
				print ("")

			else:
				print ("")
				print (" un obstacle se trouve dans la tajectoire du robot ",self.robotID)
				print (" point possible de collision = [",coor[0],",",coor[1],"]")
				print (" distance avec ce point = ",dist)
				print ("")
		
		return	dist



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
		self._optionAffichageR = affiche




#-----------------------------------updateTest-----------------------------------

	def updateTest(self):
		'''
			juste pour tester l'affichage opengl
			a supprimer plus tard
		'''
		self.move(0.1)
		self.turn(1)


#------------------print---------------------------------------------------------

	
	def printRobot(self):
		"""
		affiche toutes les informations sur le Robot"
		"""
		speedx = self.speed*math.cos(self.direction)
		speedy = self.speed*math.sin(self.direction)
		angle = self.direction * (180/math.pi)
		if(self._optionAffichageR):
			print ("")
			print ("---------------------------------------------------------")
			print (" nom du Robot: ",self.robotID)
			print (" position = [",self.posx,",",self.posy,"]")
			print (" vitesse = ",self.speed)
			print (" direction de la vitesse(°) = ",angle)
			print ("---------------------------------------------------------")
			print ("")
		return		


	

		

