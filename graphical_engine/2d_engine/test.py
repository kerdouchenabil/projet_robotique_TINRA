from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

print('coucou')

window = 0
width, height = 500, 400


def draw():                                 #fonction de base qui va tout dessiner
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()


    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0)
window = glutCreateWindow("test quelquonque")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
