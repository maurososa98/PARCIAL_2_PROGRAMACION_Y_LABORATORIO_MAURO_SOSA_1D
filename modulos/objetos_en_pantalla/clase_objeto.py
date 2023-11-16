import pygame
from modulos.objetos_en_pantalla.clase_nivel import *
from modulos.funciones import *

lista_imagenes_vida = lista_imagenes("imagenes/vida/0.png",12,(22,26))
grupo_vidas_nivel_1 = pygame.sprite.Group()
grupo_vidas_nivel_2 = pygame.sprite.Group()
grupo_vidas_nivel_3 = pygame.sprite.Group()

lista_imagenes_punto = lista_imagenes("imagenes/punto/0.png",16,(10,16))
grupo_puntos_nivel_1 = pygame.sprite.Group()
grupo_puntos_nivel_2 = pygame.sprite.Group()
grupo_puntos_nivel_3 = pygame.sprite.Group()

class Objeto(pygame.sprite.Sprite):
    def __init__(self,x,y, lista_imagenes, refrescar_animacion):
        pygame.sprite.Sprite.__init__(self)
        self.lista_imagenes = lista_imagenes
        self.indice = 0
        self.contador = 0

        self.image = self.lista_imagenes[self.indice]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.refrescar_animacion = refrescar_animacion
        
        self.escala_jefe_1 = (72,107)

    def update(self):
        self.animar()

    def animar(self, salta=False, desplazamiento_y=0, velocidad=0):
        self.contador += 1
        refrescar = self.refrescar_animacion
        if self.contador > refrescar:
            self.contador = 0
            self.indice += 1
            if salta and (desplazamiento_y < 0 or desplazamiento_y > 0):
                imagen_salta = pygame.image.load("imagenes/venom/salta/4.png") 
                if velocidad < 0:
                    self.image = pygame.transform.scale(imagen_salta,self.escala_jefe_1)
                elif velocidad > 0:
                    imagen_escalada = pygame.transform.scale(imagen_salta,self.escala_jefe_1)
                    self.image = pygame.transform.flip(imagen_escalada,True,False)
            else:
                if self.indice >= len(self.lista_imagenes):
                    self.indice = 0
                self.image = self.lista_imagenes[self.indice]

class ItemPunto(Objeto):
    def __init__(self, x, y, lista_imagenes, refrescar_animacion):
        super().__init__(x, y, lista_imagenes, refrescar_animacion)

class ItemVida(Objeto):
    def __init__(self, x, y, lista_imagenes, refrescar_animacion):
        super().__init__(x, y, lista_imagenes, refrescar_animacion)