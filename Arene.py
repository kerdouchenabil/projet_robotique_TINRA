from Robot import Robot
from Obstacle import Obstacle

class Arene:

	def __init__(self,longueur,largeur,listeRobot=[],listeObst=[]):
		"""
		cree l'arene avec pour attribut:
		- sa dimension avec sa longueur (selon x) et sa largeur (selon y)
		- liste des robots, par defaut: liste vide 
		- liste des obstacles (murs), par defaut: liste vide
		"""
		self.longueur = longueur
		self.largeur = largeur
		self.listeRobot = Robot
		self.listeObst = listeObst



#-------------------------------------Setter-------------------------------------

	def setTaille(self,x,y):
		"""
		modifie les dimensions de l'arene
		"""
		self.longueur = x
		self.largeur = y
		return
