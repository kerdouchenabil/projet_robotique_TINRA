# -*- coding: utf-8 -*-
import math 




class Robot:

	def __init__ (self, posx, posy, direction, speed=0) :
		"""
		float x float x float x float x float -> Robot
		- position de depart: posx et posy
		- direction: angle du vecteur vitesse (en radian)
		- vitesse de depart (nulle par defaut): speed
		"""
		self.posx = posx
		self.posy = posy
		self.direction = direction 
		self.speed = speed


	def accelerate (self, acc, dt) :
		"""
		float x float ->
		acceleration (freinage si acc negatif): modification de la vitesse
		"""
		self.speed = self.speed + acc*dt
		return

	def turn_left(self, angle):
		"""
		float ->
		calculate nex direction direction
		doesn't modify speed
		angle in degree, converted in radian
		"""
		self.direction = self.direction+angle
		return
		
		
	def turn_right(self, angle):
		"""
		float ->
		calculate nex direction direction
		doesn't modify speed
		angle in degree, converted in radian
		"""
		self.direction = self.direction-angle
		return


	def move(self,dt):
		"""
		float ->
		calculate new positions x and y after dt (time step)
		using the speed and direction
		"""
		self.posx = self.posx + dt * math.cos(self.direction) * self.speed
		self.posy = self.posy + dt * math.sin(self.direction) * self.speed
		return


	def position_x(self):
		"""
		return the position x
		"""
		return self.posx


	def position_y(self):
		"""
		return the position y
		"""
		return self.posy
	
	#getter
	def getPos(self):
		#return (self.posx,self.posy)
	
	
	def getDirection(self):
		return self.direction

	#setter
	def setPos(self,posx,posy):
		self.posx=posx
		self.posy=posy
	
	def setDirection(self,direction)
		self.direction=direction
		
	def setVit(self,vit):
		self.speed=vit
	
	def printAll(self):
		"""
		print all parameters
		"""
		speedx = self.speed*math.cos(self.direction)
		speedy = self.speed*math.sin(self.direction)
		angle = self.direction * (180/math.pi)
		print " pos = [",self.posx,",",self.posy,"]"
		print " speed = ",self.speed
		print "        speedx = ",speedx," ,  speedy = ",speedy
		print " angle direction(°) = ",angle
		print ""
		return		

		

