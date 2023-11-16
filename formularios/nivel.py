import pygame
from pygame.locals import *

from UI.GUI_button import *
from UI.GUI_slider import *
from UI.GUI_textbox import *
from UI.GUI_label import *
from UI.GUI_form import *
from UI.GUI_button_image import *
from GUI_form_menu_score import *


class Nivel:
    def __init__(self, pantalla, personaje_principal, lista_plataformas, imagen_fondo):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        
    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
        
        self.actualizar_pantalla()
    
    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo, (0,0))
        
        for plataformas in self.plataformas:
            plataformas.draw(self._slave)
        
        self.jugador.update(self._slave, self.plataformas)
        
        
        
    def leer_inputs(self):
        keys = pygame.key.get_pressed()
        
        if keys(pygame.K_RIGHT):
            self.jugador.