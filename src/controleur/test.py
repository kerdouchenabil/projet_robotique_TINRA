import math as m

#precision des valeurs finals
precision = 3

def afficher(*parametres):

    param = list(parametres)
    longueur = createLong(param)
    angle = createAngle(param)
    instruction = list(zip(longueur, angle))
    print()
    print(longueur)
    print(angle)
    print(instruction)
    print()
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
        hypotenuse = m.sqrt(x**2 + y**2)
        hypotenuse = round(hypotenuse, precision)
        longueur.append(hypotenuse)
    return longueur

def createAngle(parametres):

    param = list(parametres)
    angle = list()
    alpha_precedent = 0
    for i in range(len(param)-1):
        print(alpha_precedent)
        x = param[i+1][0] - param[i][0]
        y = param[i+1][1] - param[i][1]
        alpha = m.atan2(y, x) - alpha_precedent
        alpha_precedent = alpha
        alpha = m.degrees(alpha)
        alpha = round(alpha, precision)
        angle.append(alpha)
    return angle


afficher([0,0], [10,0], [10, 10], [0,10], [0,0])