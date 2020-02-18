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
		self.listeRobot = listeRobot
		self.listeObst = listeObst





#--------------------------------fonctions ajout--------------------------------
	
	def addObstacle(self, obs):
		'''
		teste si l'objet est de Classe Obstacle, si oui
		ajoute un obstacle a la liste des obstacles de l'Arene
		'''
		if( isinstance(obs, Obstacle) ):
			self.listeObst.append(obs)
			print("Obstacle ajouté a la listeObst")
		else:
			print("ajout pas possible dans listeObst")
	
	
	def addRobot(self, rob):
		'''
		teste si l'objet est de Classe Robot, si oui
		ajoute le Robot a la liste des Robots de l'Arene
		'''
		if( isinstance(rob, Robot) ):
			self.listeRobot.append(rob)
			print("Robot ajouté a la listeRobot")
		else:
			print("ajout pas possible dans Robot")
			
					

#-------------------------------------Setter-------------------------------------

	def setAreneDimension(self,x,y):
		"""
		modifie les dimensions de l'arene
		"""
		self.longueur = x
		self.largeur = y
		return
	
	
	
#-------------------------------------Getter-------------------------------------

	def getRobot0(self) :
		'''
			retourne le premier robot de la liste listeRobot[0]
			si listeRobot non vide
			(facilite le travail avec un seul robot)
		'''
		if( not self.listeRobot ):
			print("listeRobot vide !")
			return
		else:
			return self.listeRobot[0]
		
	




