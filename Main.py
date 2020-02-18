import Robot
import Arene
import Obstacle


'''
    le main du projet qui relie toutes les instances
    cree des instances de Robot, Arene, Obstacles, Affichage
    ajoute les Robots et Obstacles dans l'Arene
    
'''

'''
    initialisatin des attributs de depart
'''
robID= 0
robPosX= 5
robPosY= 5
robDir= 0
robVitesse= 0

areneLongueur= 200
areneLargeur= 200


'''
    creation du robot ID=0  position=[5;5]  direction=0 (droite)  vitesse=0
'''
rob = Robot()


'''
    creation d'un obstacle representant un mur
'''



'''
    creation d'une arene
'''
arene = Arene(areneLongeur, areneLargeur)

