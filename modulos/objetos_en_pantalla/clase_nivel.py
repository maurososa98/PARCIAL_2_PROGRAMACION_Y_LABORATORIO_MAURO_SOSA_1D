from modulos.objetos_en_pantalla.clase_heroe import *

import pygame

class Niveles():
    def __init__(self, imagen_fondo, pantalla, tamaño_pantalla):
        self.bandera_menu_principal = True
        self.bandera_nivel_1 = False
        self.bandera_nivel_2 = False
        self.bandera_nivel_3 = False
        self.bandera_menu_pausa = False

        self.pantalla = pantalla
        self.tamaño_pantalla = tamaño_pantalla

        self.pressed_keys = None

        self.set_imagen_fondo(imagen_fondo)

        self.set_heroe()
        self.fin_juego = 1

        self.puntos = 0
        self.sonido_puntos = pygame.mixer.Sound(("musica/punto.wav"))

        self.vidas_spiderman = 3
        self.vidas_jefe = 28
        self.jefe_muerto = False

        self.sonido_vidas = pygame.mixer.Sound(("musica/vida.wav"))
        self.sonido_resta_vida = pygame.mixer.Sound(("musica/resta_vida.wav"))
        self.sonido_enemigo_golpeado = pygame.mixer.Sound(("musica/enemigo_golpeado.wav"))
        self.cant_enemigos_eliminados = 0

    def set_heroe(self):
        posicion_inicial_x = 55
        posicion_inicial_y = 600
        self.heroe = Heroe(lista_camina_derecha,lista_camina_izquierda,(posicion_inicial_x,posicion_inicial_y),6,self.pantalla,self.tamaño_pantalla[0])

    def mover_heroe(self, nivel, grupo_enemigos, grupo_salida, grupo_balas_1, grupo_balas_2, grupo_balas_3, grupo_jefe= []):
        datos = self.heroe.mover(self.pressed_keys, nivel, grupo_enemigos, grupo_salida, grupo_balas_1, grupo_balas_2, grupo_balas_3, grupo_jefe)
        self.fin_juego = datos[0]
        self.cant_enemigos_eliminados = datos[1]
        self.vidas_jefe = datos[2]

    def set_imagen_fondo(self, imagen_fondo):
        fondo = pygame.image.load(imagen_fondo)
        self.fondo = pygame.transform.scale(fondo, self.tamaño_pantalla)

    def blit_fondo(self):
        self.pantalla.blit(self.fondo,(0,0))

    def texto_en_pantalla(self, texto, color, x, y):
        texto_en_pantalla = self.fuente.render(texto, True, color)
        self.pantalla.blit(texto_en_pantalla, (x,y))

    def recolectar_puntos(self, grupo_puntos_nivel):
        if self.fin_juego >= 1:
            if (pygame.sprite.spritecollide(self.heroe,grupo_puntos_nivel,True)):
                self.puntos += 100
                self.sonido_puntos.play()
                self.sonido_puntos.set_volume(0.2)

    def recolectar_vidas(self, grupo_vidas_nivel):
        if self.fin_juego >= 1:
            if pygame.sprite.spritecollide(self.heroe,grupo_vidas_nivel,True):
                self.sonido_vidas.play()
                self.sonido_vidas.set_volume(0.2)
                self.vidas_spiderman += 1
                if self.vidas_spiderman > 3:
                    self.vidas_spiderman = 3

    def registro_colisiones(self, grupo_enemigos_nivel, grupo_balas_1, grupo_balas_2, grupo_balas_3, grupo_jefe=[]):
        if (pygame.sprite.spritecollide(self.heroe,grupo_enemigos_nivel,False) or 
            pygame.sprite.spritecollide(self.heroe,grupo_balas_1,False) or
            pygame.sprite.spritecollide(self.heroe,grupo_balas_2,False) or
            pygame.sprite.spritecollide(self.heroe,grupo_balas_3,False) or
            pygame.sprite.spritecollide(self.heroe,grupo_jefe,False)):
            if self.heroe.fin_del_juego != 0:
                self.sonido_resta_vida.play()
                self.sonido_resta_vida.set_volume(0.2)
            self.vidas_spiderman -= 1
            if self.vidas_spiderman <= 0:
                self.vidas_spiderman = 0
            else:
                self.heroe.rect.x = 55
                self.heroe.rect.y = 554
                self.sonido_resta_vida.play()
                self.sonido_resta_vida.set_volume(0.2)

    def registro_nivel(self):
        return self.fin_juego








































