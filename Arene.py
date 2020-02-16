from Robot import Robot
from Obstacle import Obstacle

class Arene:

	def __init__(self,longueur,largeur,listeRobot=[],listeObst=[]):
		"""
		cree l'arene avec pour attribut:
		- sa dimension avec sa longueur (selon x) et sa largeur (selon y)
		- les robots presents dessus
		- les obstacles (murs)
		"""
		self.longueur = longueur
		self.largeur = largeur
		self.listeRobot = Robot
		self.listeObst = listeObst
