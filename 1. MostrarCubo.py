import pygame                 # <--- interacción, creación de la pantalla
from pygame.locals import *   # <--- botones ESC, ESPACIO, etc
from OpenGL.GL import *       # <--- GPU
from OpenGL.GLU import *
from Cube import wireCube

pygame.init()

# project settings
screen_width = 1000 # normalizar [-1, 1]
screen_height = 800 # normalizar [-1, 1]
background_color = (0, 0, 0, 1)
drawing_color = (0.5, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')


def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    # modelview
    glMatrixMode(GL_MODELVIEW)
    glTranslate(0, 0, -5)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    glTranslate(0, 0, -2)


def display():
    # borrar la pantalla
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # establecer un giro de pantalla
    glRotatef(1, 1, 1, 1)
    # de manera matricial (0,0) y los bordes -1 y 1
    glPushMatrix()
    # dibujar el cubo
    wireCube()
    # envía este cubo a la pantalla
    glPopMatrix()


done = False
initialise()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    display() # ejecutar la función display
    pygame.display.flip() # actualizar la pantalla
    pygame.time.wait(5) # esperar 5 ms.
pygame.quit()
