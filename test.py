from Robot import Robot
import math

rob = Robot("Rob",0,0,0,1)

rob.printAll()

rob.accelerate(2,1)

rob.printAll()

rob.turn(math.pi/2)

rob.printAll()

rob.move(1)

rob.printAll()
