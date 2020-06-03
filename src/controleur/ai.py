# -*- coding: utf-8 -*-

from src.objet.robot import *
from math import *


class Controleur:
	'''
		le controleur (IA) du robot
		utilise les fonctions de commande du robot: (possibilité de passer par un proxy)
		set_motor_dps(id, dps)
		get_position(id)
		get_distance()
		...
		ces fonctions sont utilisées pour implementer de petites strategies basiques comme
		stop_strategy()
		turnRight_strategy
		turnLeft_strategy
		...
		ces strategies de base sont utilisées pour implementer les fonctionnalitées attendues (strategies complexes)
		square_strategy()
		...
	'''
	
	def __init__(self, robot):
		"""
			prend le robot en parametre (possibilité d'utiliser un proxy comme intermediaire)
		"""
		
		self.robot = robot
		

	def update(self):
		"""
			mise a jour du comportement et de l'etat du robot
			en fonction de son etat precedent
			sera appelée dans chaque stratégie
		"""
		
		#a completer
		return

#------------- les objectif du robot ------------

	def setParcours(self, *cord):
		"""
			?
		"""

		return 

	def setTeteBaisse(self):
		"""
			?
		"""
		
		return
	

	def setSuivreBalise(self):
		"""
			?
		"""
            #plus tard, bien plus tard
            
		return

#------------- fonction utilitaire ------------


def createLong(parametres):
	"""
	renvoit la liste des longeurs des deplacement que le robot doit effectuer
	"""
	param = list(parametres)
	longueur = list()
	for i in range(len(param)-1):
		x = abs(param[i][0] - param[i+1][0])
		y = abs(param[i][1] - param[i+1][1])
		hypotenuse = m.sqrt(x**2 + y**2)
		hypotenuse = round(hypotenuse, precision)
		longueur.append(hypotenuse)
	return longueur


def createAngle(parametres):
	"""
		renvoit la liste des rotations que le robot doit effectuer par raport a l'origine
	"""
	param = list(parametres)
	angle = list()
	alpha_precedent = 0
	for i in range(len(param)-1):
		print(alpha_precedent)
		x = param[i+1][0] - param[i][0]
		y = param[i+1][1] - param[i][1]
		alpha = m.atan2(y, x)
		alpha = m.degrees(alpha)
		alpha = round(alpha, precision)
		angle.append(alpha)
	return angle


def control_moteur(self, ):
	"""
		strategie d'avancement du robot (vitesse, accelereation) ?
	"""
	
	
	return 


#------------- Sreategies asynchrones du controleur ------------

class go_ahead_strategy:
	"""
		strategie permettant de dire au robot d'avancer pour parcourir une certaine distance donnée
		cette strategie sera utilisée pour quelques étapes de la stratégie 'faire_un_carré'
		la stratégie doit etre asynchrone, donc doit juste avancer si la distance n'a pas encore été parcourue
		pas de boucles itératives
		
	"""

	def __init__(self, robot, dist):
		"""
			constructeur
			initialise la distance_parcourue à 0
		"""
		self.dist_parcourue = 0 #distance parcourue par le robot
		
		# mettre robot et dist comme attribut de cette classe pour les utiliser directement dans les fonctions
		self.robot=robot
		self.dist=dist
		
	
	def start(self):
		"""
			debut de strategie
			
		"""
		xbegin = self.robot.posx
		ybegin = self.roboy.posy
		self.coords_start= [xbegin,ybegin] #initialiser dans _init_ ?
		self.robot.direction = 0
		self.robot.speed = 0
		
		return [xbegin,ybegin]   #retourne les coords de depart
        
        		
		
	def step(self):
		"""
			coeur de stategie (update)
			Pour le moment, on a pas de roues donc on calcule la distance avec les coords (virtuel)
			
			pour le robot reel, la distance est egale a:
			diametre_roue * pi * nombre_tours_moteur
			
			pour le virtuel:
			distance entre deux points géométriques
		"""
		#dt=?  doit-on le fixer a 1 par exemple?
		
		self.robot.accelerate(1, 1) #acceleration+1 et dt=1 a chaque etape
		self.robot.move(1) #dt=1
		self.dist_parcourue += calcul_distance(self.robot.posx, self.coords_start[0], self.robot.posy, self.coords_start[1])
		
		
	def stop(self):
		"""
			teste si la distance demandée a été parcourue ou pas
			si oui renvoi vrai donc fin de la strategie go_ahead 
		"""
		
		if(self.dist_parcourue >= self.dist): #si fin du parcours
			self.robot.speed = 0 
			return True
		
		'''
		#Virtuel: il faut passer l'arene en parametre pour detecter un obstacle
		if(robot.distanceRobotObs(arene) < distance_securite) #si obstacle devant
			return True
		'''
		
		'''
		#Reel: on recupere directement le retour du capteur de distance (pas encore fonctionnel)
		if(robot.getDistance() < distance_securite)
			return True
		'''
		
		return False #si pas d'obstacle devant et pas encore arrivé a la fin du parcours
	
	
class turn_right_strategy:
	"""
		strategie asynchrone qui permet de tourner a droite
		start: quand on lui donne l'ordre de tourner
		step: reelement on fait tourner la roue gauche plus rapidement que la droite
		stop: quand l'angle donné est fait par rapport à l'etat start
	"""
	
	def __init__(self, robot, angle):
		"""
			constructeur, initialise la direction initiale
		"""
		self.robot = robot
		self.angle = angle
		self.dir_init = robot.getDir()
		

	def start(self):
		"""
			debut de strategie
			donner l'ordre au moteur gauche de tourner plus vite (quand le moteur sera codé avec le proxy)
		"""
		self.dir_init = robot.getDir()
		#self.robot.moteur_gauche() #a coder dans le proxy
		
		
	def step(self):
		"""
			coeur de strategie, update()
			donner l'ordre de continuer a tourner a droite
			#c'est mieux si la gestion du virtuel et réel est gérée par un proxy
		"""
		
		#Virtuel: faire tourner le robot et le bouger
		self.robot.turn(-1) #pour simuler la rotation a droite
		self.robot.move(1) #notre dt est fixé a 1 comme les autres strategies
		
		#Reel: juste continuer a garder la roue gauche tourner plus vite que la droite
		
		
	def stop(self):
		"""
			renvoi vrai si fin de la strategie
		"""
		
		if(self.robot.getDir() < self.dir_init-self.angle): #si fin de la rotation droite demandée
			return True
		
		'''
		#Virtuel: il faut passer l'arene en parametre pour detecter un obstacle
		if(robot.distanceRobotObs(arene) < distance_securite) #si obstacle devant
			return True
		'''
		
		'''
		#Reel: on recupere directement le retour du capteur de distance (pas encore fonctionnel)
		if(robot.getDistance() < distance_securite)
			return True
		'''
		
		return False #si pas d'obstacle devant et pas encore arrivé a la fin du parcours
	

	def calcul_distance(self, x1, x2, y1, y2):
		"""
		fonction qui sert juste a calculer une distance geo entre deux points ( utilisée dans step() )
		"""
		return sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) )
	





