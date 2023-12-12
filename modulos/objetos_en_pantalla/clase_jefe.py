import pygame
from modulos.objetos_en_pantalla.clase_enemigo import *
from modulos.objetos_en_pantalla.clase_nivel import *
from modulos.funciones import *

class Jefe(Enemigo):
    def __init__(self, x, y, lista_imagenes, refrescar_animacion, cuanto_camina, lista_imagenes_izquierda, lista_imagenes_derecha, velocidad):
        super().__init__(x, y, lista_imagenes, refrescar_animacion, cuanto_camina, lista_imagenes_izquierda, lista_imagenes_derecha, velocidad)
        self.ultimo_salto = pygame.time.get_ticks()
        self.calculo = 0
        
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.desplazamiento_y = 0
        self.desplazamiento_X = 0
        self.contador_salto = 0

        self.velocidad_salto = 0
        self.esta_saltando = False
        self.giro = False

    def animar_salto(self, nivel):
        self.desplazamiento_y = 0

        self.contador_pasos += 1
        if self.velocidad < 0:
            self.lista_imagenes = lista_imagenes_jefe_venom_izquierda
        elif self.velocidad > 0:
            self.lista_imagenes = lista_imagenes_jefe_venom_derecha
        if abs(self.contador_pasos) > self.cuanto_camina:
            self.velocidad *= -1
            self.contador_pasos = 0
        self.desplazamiento_x = self.velocidad

        self.contador_salto +=1
        if self.contador_salto > 50 and self.esta_saltando == False:
            self.contador_salto = 0
            self.velocidad_salto = -16
            self.esta_saltando = True

        # Grabedad
        self.velocidad_salto += 1
        if self.velocidad_salto > 20:
            self.velocidad_salto = 20
        self.desplazamiento_y += self.velocidad_salto

        for rectangulo_plataforma in nivel.lista_img_rect:
            if rectangulo_plataforma[1].colliderect(self.rect.x + self.velocidad, self.rect.y, self.width, self.height):
                self.desplazamiento_x = 0

            if rectangulo_plataforma[1].colliderect(self.rect.x, self.rect.y + self.desplazamiento_y, self.width, self.height):
                if self.velocidad_salto < 0: # SUBIENDO
                    self.desplazamiento_y = rectangulo_plataforma[1].bottom - self.rect.top
                    self.velocidad_salto = 0
                if self.velocidad_salto >= 0: # BAJANDO
                    self.desplazamiento_y = rectangulo_plataforma[1].top - self.rect.bottom
                    self.velocidad_salto = 0
                    self.esta_saltando = False

        if self.rect.left < 0:
            self.rect.left = 0
            self.desplazamiento_x = 0
        if self.rect.right > 880:
            self.rect.right = 880
            self.desplazamiento_x = 0

        self.rect.y += self.desplazamiento_y
        self.rect.x += self.desplazamiento_x

        self.animar(self.esta_saltando,self.desplazamiento_y,self.velocidad)

    def vidas_en_pantalla(self, pantalla, tamaño_pantalla, vidas):
        imagen_vidas = pygame.image.load(f"imagenes/venom/cantidad_vida/{vidas}.png")
        imagen_vidas = pygame.transform.scale(imagen_vidas, (200,50))
        pantalla.blit(imagen_vidas, (tamaño_pantalla[0] - 850, 20))
