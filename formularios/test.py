import pygame
import sys
from pygame.locals import *
from GUI_form_prueba import FormPrueba
from nivel_uno import *
from nivel_dos import *
pygame.init()
WIDTH = 1200
HEIGHT = 600
FPS = 60

RELOG = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((WIDTH, HEIGHT))

form_prueba = FormPrueba(PANTALLA, 200, 100, 900, 350, "blue", "red", 5, True)


nivel_actual = NivelUno(PANTALLA)

while True:
    RELOG.tick(FPS)
    PANTALLA.fill("Black")
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            
    nivel_actual.update(eventos)

    
    form_prueba.update(eventos)

    pygame.display.flip()