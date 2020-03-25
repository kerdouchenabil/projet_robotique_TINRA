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
	
	
	def control_moteur(self):
		"""
			strategie d'avancement du robot (vitesse, accelereation) ?
		"""
		
		#a completer
		return 

#------------- les objectif du robot ------------

	def setParcours(self):
		"""
			?
		"""
		
		#a completer
		return 

	def setTeteBaisse():
		"""
			?
		"""
		
		return
	

	def setSuivreBalise():
		"""
			?
		"""
            #plus tard, bien plus tard
            
		return
	
