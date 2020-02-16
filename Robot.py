# -*- coding: utf-8 -*-
import math 




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
		if(optionPrint):
			print("le robot a accelere de ",acc)
		return

	def turn(self, angle):
		"""
		float ->
		calcule la nouvelle direction du vecteur vitesse, permet au robot
		de tourner d'un certain angle (gauche si positif, droit si negatif)
		"""
		self.direction = self.direction+angle
		if(optionPrint):
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

	
	def printAll(self):
		"""
		affiche toutes les informations sur le Robot"
		"""
		speedx = self.speed*math.cos(self.direction)
		speedy = self.speed*math.sin(self.direction)
		angle = self.direction * (180/math.pi)
		if(optionPrint):
			print ("")
			print ("---------------------------------------------------------")
			print (" nom du Robot: ",self.robotID)
			print (" position = [",self.posx,",",self.posy,"]")
			print (" vitesse = ",self.speed)
			print (" direction de la vitesse(°) = ",angle)
			print ("---------------------------------------------------------")
			print ("")
		return		


	

		

