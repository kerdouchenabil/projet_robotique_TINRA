from math import *

#precision des valeurs finals
precision = 3

def afficher(*parametres):

    param = list(parametres)
    longueur = createLong(param)
    angle = createAngle(param)
    instruction = list(zip(longueur, angle))
    print(longueur)
    print(angle)
    print()
    print(instruction)

    for i in range(len(param)-1):
        print("segment n°",i+1)
        print("x1 =", param[i][0], "; y1 =", param[i][1])
        print("x2 =", param[i+1][0], "; y2 =", param[i+1][1])
        print("instruction : longueur=", instruction[i][0], "; angle=", instruction[i][1])
        print()

def createLong(parametres):

    param = list(parametres)
    longueur = list()
    for i in range(len(param)-1):
        x = abs(param[i][0] - param[i+1][0])
        y = abs(param[i][1] - param[i+1][1])
        hypotenuse = round(sqrt(x**2 + y**2), precision)
        longueur.append(hypotenuse)
    return longueur

def createAngle(parametres):

    param = list(parametres)
    angle = list()
    for i in range(len(param)-1):
        angle.append(0)
    return angle


afficher([10,10], [250,200], [200, 400])