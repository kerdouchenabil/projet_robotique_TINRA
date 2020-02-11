# -*- coding: utf-8 -*-
import math 




class Robot:

	def __init__ (self, posx, posy, direction, maxspeed, speed=None) :
		"""
		float x float x float x float x float -> Robot
		- starting positions (x and y)
		- maximum speed and initial speed (optionnal, by default 0)
		- direction of the Robot in radian 
		"""
		self.posx = posx
		self.posy = posy
		self.maxspeed = vmax
		self.direction = direction 
		if speed == None:
			self.speed = 0
		else
			self.speed = speed


	def accelerate (self, acc, dt) :
		"""
		float x float ->
		calculate new speed
		dt is the time step
		doesn't modify direction
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
		self.direction = self.direction-angle
		return
		
		
	def turn_right(self, angle):
		"""
		float ->
		calculate nex direction direction
		doesn't modify speed
		angle in degree, converted in radian
		"""
		self.direction = self.direction+angle
		return


	def move(self,dt):
		"""
		float ->
		calculate new positions x and y after dt (time step)
		using the speed and direction
		"""
		self.posx = self.posx + dt * math.cos(self.direction) * self.speed
		self.posy = self.posy + dt * math.cos(self.direction) * self.speed
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
		

		

