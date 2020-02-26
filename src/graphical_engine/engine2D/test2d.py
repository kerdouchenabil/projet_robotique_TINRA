from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0
width, height = 500, 400


def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_rectangle(x, y, width, height):
    glBegin(GL_QUADS)                       #signaler a opengl que on va dessiner un rectangle (GL_QUADS)
    glVertex2f(x, y)                        #dessine les 4 vectrices
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()                                 #signale la fin du dessin

def draw():                                 #fonction de base qui va tout dessiner
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    refresh2d(width, height)                # set mode to 2d
    glColor3f(0.0, 0.0, 1.0)                #set la couleur a bleu : r, g, b avec des valeur entre 0 et 1
    draw_rectangle(10, 10, 200, 100)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0)
window = glutCreateWindow("test 2d graphique")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
