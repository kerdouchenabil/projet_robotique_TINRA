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





#--------------------------------fonctions ajout--------------------------------
	
	def addObstacle(self, obs):
		'''
		teste si l'objet est de la Classe Obstacle, si oui
		ajoute un obstacle a la liste des obstacles de l'Arene
		'''
		if( isinstance(obs, Obstacle) ):
			self.listeObst.append(obs)
			print("Obstacle ajouté a la listeObst")
		else:
			print("ajout pas possible dans listeObst")
			

#-------------------------------------Setter-------------------------------------

	def setAreneDimension(self,x,y):
		"""
		modifie les dimensions de l'arene
		"""
		self.longueur = x
		self.largeur = y
		return
