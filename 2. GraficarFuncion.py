import math
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
pygame.init()

ancho = 1000
alto = 800

pantalla = pygame.display.set_mode((ancho, alto), DOUBLEBUF | OPENGL)
#colocar titulo:
pygame.display.set_caption('Graficos en OpenGL')

def inicializar_Ortografica():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 5, -1, 1) # el vector de la cámara

def plotearGrafico():
    glBegin(GL_POINTS) # graficar un punto
    px: GL_DOUBLE # coordenada X de DOUBLE en OpenGL
    py: GL_DOUBLE # coordenada Y en DOUBLE en OpenGL
    for px in np.arange(0, 5, 0.0005):
        py = math.exp(-px) * math.cos(2*math.pi * px)
        # py = math.exp(-px)
        # e**(-x) * (cos(2*pi*x))
        glVertex2f(px, py)
        # graficar el vértice x, y
    glEnd() # termine de graficarlo en pantalla

def DibujarEstrella(x, y, tamanio):
    glPointSize(tamanio)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


Fin = False
inicializar_Ortografica()
glPointSize(4)
while not Fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Fin = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # borrar pantalla
    glMatrixMode(GL_MODELVIEW) # normalizar entre [-1, 1]
    glLoadIdentity() # borrar contenido de pantalla
    plotearGrafico() # dibujar la función
    pygame.display.flip() # actualizar pantalla
    pygame.time.wait(100) # esperar 100ms.

pygame.quit()

