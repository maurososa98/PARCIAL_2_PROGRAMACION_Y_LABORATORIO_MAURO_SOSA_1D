import pygame
import pygame.font
from pygame.locals import *
pygame.font.init()

class Configuracion:
    def __init__(self, tamaño_pantalla:tuple, FPS:int, titulo_pantalla:str, icono:str, imagen_fondo:str, fuente:str, musica:str):
        pygame.mixer.init()
        self.tamaño_pantalla = tamaño_pantalla
        self.PANTALLA = pygame.display.set_mode(self.tamaño_pantalla)
        self.FPS = FPS
        self.reloj = pygame.time.Clock()
        self.bandera_iniciar = True
        self.set_titulo_pantalla(titulo_pantalla) 
        self.set_icono(icono)
        self.set_imagen_fondo(imagen_fondo)
        self.set_fuente(fuente)
        self.set_musica(musica)

    def set_titulo_pantalla(self, titulo_pantalla):
        pygame.display.set_caption(titulo_pantalla)

    def set_icono(self, icono):
        self.icono = pygame.image.load(icono)
        pygame.display.set_icon(self.icono)

    def set_fps(self, FPS):
        self.FPS = FPS

    def set_imagen_fondo(self, imagen_fondo):
        fondo = pygame.image.load(imagen_fondo)
        self.fondo = pygame.transform.scale(fondo, self.tamaño_pantalla)

    def set_fuente(self, fuente:str, tamaño_fuente:int=30):
        self.fuente = pygame.font.SysFont(fuente, tamaño_fuente)

    def set_musica(self, ruta:str):
        self.musica_fondo = pygame.mixer.Sound(ruta)
        self.reproducir_musica()
        self.musica_fondo.set_volume(0.03)

    def reproducir_musica(self):
        self.musica_fondo.play(-1)

    def parar_musica(self):
        self.musica_fondo.stop()

    def fill_pantalla(self, color=None):
        if color != None:
            self.PANTALLA.fill(color)