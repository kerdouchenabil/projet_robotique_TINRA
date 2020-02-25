from objet.robot import *
from objet.obstacle import *
from objet.arene import *
import math

rob = Robot("Rob",0,0,0,1)
rob2 = Robot("Rob2",-1,-1,225,2)

rob.printRobot()

rob.accelerate(2,1)

rob.printRobot()

rob.turn(55)

rob.printRobot()

rob.move(1)

rob.printRobot()

obst1 = Obstacle(6,6.1,2,8)
obst2 = Obstacle(-10,-11,2,8)
obst3 = Obstacle(-3.9,7,2,8)
obst = [obst1, obst2, obst3]

arene = Arene(20,20,[rob,rob2],obst)

listpos = rob.possibleCollision(obst1,20,20)
print(listpos)
listpos = rob.pointsCollision(obst1,listpos)
print(listpos)
a = obst1.pointInObstacle(listpos[0],listpos[1])
dist = rob.distancePointRobot(listpos)
print(a)
print(dist)


listpos = rob2.possibleCollision(obst2,20,20)
print(listpos)
listpos = rob2.pointsCollision(obst2,listpos)
print(listpos)
a = obst2.pointInObstacle(listpos[0],listpos[1])
dist = rob2.distancePointRobot(listpos)
print(a)
print(dist)

dist1 = rob.distanceRobotObs(arene)
dist2 = rob2.distanceRobotObs(arene)
print(dist1)
print(dist2)


