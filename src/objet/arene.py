from .robot import Robot
from .obstacle import Obstacle

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
		self._optionAffichageA = True





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
	

#-----------------------------------setOption-------------------------------

	def setOptionPrintArene(self,affiche):
		"""
		choisit ou non d'afficher les informations de l'arene sur le terminal
		a chaque pas de temps
			False -> n'affiche pas
			True  -> affiche
		"""
		self._optionAffichageA = affiche


	def setOptionPrint(self, afficheA,afficheR,afficheO):
		"""
		choisit ou non d'afficher les informations sur l'arene, ses robots et ses
		obstacles; les 3 attributs sont pour controler respectivement: 
			(affichage Arene, affichage Robot, affichage Obstacle)
			False -> n'affiche pas
			True  -> affiche
		"""	
		for robot in listeRobot:
			robot.setOptionPrintRobot(afficheR)
		for obstacle in listeObst:
			obst.setOptionPrintObstacle(afficheO)
		self.setOptionPrintArene(afficheA)
			

#---------------------------------Affichage_text--------------------------------

	def printAll(self):
		"""
		affiche les informations de l'Arene"
		"""
		if(self._optionAffichageA):
			print("Arene: longueur=", self.longueur, " largeur=", self.largeur)
			print("Nombre robots=", len(self.listeRobot), "Nombre obstacles=", len(self.listeObst))
		# on peut completer avec les robot.printRobot
		return	


