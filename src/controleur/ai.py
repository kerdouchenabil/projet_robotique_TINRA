# -*- coding: utf-8 -*-

from src.objet.robot import *


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
		
	
	def start(self):
		"""
			debut de strategie
			
		"""
		xbegin = self.robot.posx
		ybegin = self.roboy.posy
		coor= [xbegin,ybegin]
		self.robot.direction = 1
		self.robot.speed = 1
		return coor    
        
        		
		
	def step(self):
		"""
			coeur de stategie (update)
		"""
		
		
		
	def stop(self):
		"""
			teste si la distance demandée a été parcourue ou pas
			si oui renvoi vrai donc fin de la strategie go_ahead 
		"""
		coord = [self.robot.posx,self.robot.posy]
		if(coord == self.start()):
			self.robot.speed = 0 
			return True
		return False 
    
        







