import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

ancho = 800
alto = 600

pantalla = pygame.display.set_mode((ancho, alto), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Modos de renderizado OpenGL')

def inicializar_Ortografica():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ancho, 0, alto)

def dibujar_punto(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def plot_GL_TRIANGLES(puntos):
    glColor3f(1, 0, 0)  # Rojo
    glBegin(GL_TRIANGLES)
    for i in range(0, len(puntos), 3):
        for j in range(3):
            if i+j < len(puntos):
                glVertex2f(puntos[i+j][0], puntos[i+j][1])
    glEnd()
    
    # Dibujar puntos
    glColor3f(1, 1, 1)  # Blanco
    for p in puntos:
        dibujar_punto(p[0], p[1])

def plot_GL_QUADS(puntos):
    glColor3f(0, 1, 0)  # Verde
    glBegin(GL_QUADS)
    for i in range(0, len(puntos), 4):
        for j in range(4):
            if i+j < len(puntos):
                glVertex2f(puntos[i+j][0], puntos[i+j][1])
    glEnd()
    
    # Dibujar puntos
    glColor3f(1, 1, 1)  # Blanco
    for p in puntos:
        dibujar_punto(p[0], p[1])

def plot_GL_QUAD_STRIP(puntos):
    glColor3f(0, 0, 1)  # Azul
    glBegin(GL_QUAD_STRIP)
    for p in puntos:
        glVertex2f(p[0], p[1])
    glEnd()
    
    # Dibujar puntos
    glColor3f(1, 1, 1)  # Blanco
    for p in puntos:
        dibujar_punto(p[0], p[1])

puntos = []
modo_actual = 0
modos = [plot_GL_TRIANGLES, plot_GL_QUADS, plot_GL_QUAD_STRIP]
nombres_modos = ["GL_TRIANGLES", "GL_QUADS", "GL_QUAD_STRIP"]

inicializar_Ortografica()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            puntos.append((pos[0], alto - pos[1]))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                modo_actual = (modo_actual + 1) % len(modos)
            elif event.key == pygame.K_c:
                puntos = []

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    modos[modo_actual](puntos)

    # Mostrar el modo actual
    font = pygame.font.Font(None, 36)
    text = font.render(nombres_modos[modo_actual], True, (255, 255, 255))
    pantalla.blit(text, (10, 10))

    pygame.display.flip()
    pygame.time.wait(10)
