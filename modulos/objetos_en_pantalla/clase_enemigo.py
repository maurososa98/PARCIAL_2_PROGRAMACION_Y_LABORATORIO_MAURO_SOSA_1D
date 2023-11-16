import pygame
from modulos.objetos_en_pantalla.clase_nivel import *
from modulos.objetos_en_pantalla.clase_objeto  import *

escala_enenigo = (65,46)
lista_imagenes_enemigo_venom_derecha = lista_imagenes("imagenes/enemigo_venom/0.png",28,escala_enenigo)
lista_imagenes_enemigo_venom_izquierda = lista_imagenes("imagenes/enemigo_venom/0.png",28,escala_enenigo,True)
grupo_enemigos_nivel_1 = pygame.sprite.Group()
grupo_enemigos_nivel_2 = pygame.sprite.Group()
grupo_enemigos_nivel_3 = pygame.sprite.Group()

class Enemigo(Objeto):
    def __init__(self, x, y, lista_imagenes, refrescar_animacion,cuanto_camina, lista_imagenes_izquierda, lista_imagenes_derecha, velocidad):
        super().__init__(x, y, lista_imagenes, refrescar_animacion)
        pygame.sprite.Sprite.__init__(self)
        self.velocidad = velocidad
        self.contador_pasos = 0
        self.cuanto_camina = cuanto_camina
        self.lista_imagenes_izquierda = lista_imagenes_izquierda
        self.lista_imagenes_derecha = lista_imagenes_derecha

    def update(self):
        self.rect.x += self.velocidad
        self.contador_pasos += 1
        if self.velocidad < 0:
            self.lista_imagenes = self.lista_imagenes_izquierda
        elif self.velocidad > 0:
            self.lista_imagenes = self.lista_imagenes_derecha
        if abs(self.contador_pasos) > self.cuanto_camina:
            self.velocidad *= -1
            self.contador_pasos = 0
        self.animar()