import pygame
from modulos.funciones import *

class Heroe:
    def __init__(self, lista_imagenes_derecha:list, lista_imagenes_izquierda:list, posicion:tuple, velocidad:int, pantalla:pygame.Surface, ancho_pantalla:int):
        self.lista_imagenes_derecha = lista_imagenes_derecha
        self.lista_imagenes_izquierda = lista_imagenes_izquierda

        self.indice = 0
        self.contador = 0

        self.imagen = self.lista_imagenes_derecha[self.indice]
        self.rect = self.imagen.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.width = self.imagen.get_width()
        self.height = self.imagen.get_height()

        self.velocidad = velocidad
        self.pantalla = pantalla

        self.giro = False
        self.lista_proyectiles = []
        self.proyectil_colisiono_plataforma = False
        self.ultimo_disparo = pygame.time.get_ticks()
        self.sonido_disparo = pygame.mixer.Sound(("musica/disparar.mp3"))
        self.sonido_salto = pygame.mixer.Sound(("musica/salta.wav"))
        self.sonido_enemigo_golpeado = pygame.mixer.Sound(("musica/enemigo_golpeado.wav"))
        self.sonido_jefe_golpeado = pygame.mixer.Sound(("musica/audio_venom_3_golpeado.mp3"))

        self.desplazamiento_x = 0
        self.desplazamiento_y = 0

        self.velocidad_salto = 0
        self.esta_saltando = False
        self.esta_aire = True

        self.fin_del_juego = 1
        self.cantidad_colisiones = 0
        self.cantidad_enemigos_eliminados = 0
        self.imagen_fin = pygame.image.load("imagenes/spiderman/fin_del_juego.png")
        self.imagen_fin = pygame.transform.scale(self.imagen_fin,(38,50))
        self.vidas_jefe = 28

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def mover(self, lista_teclas, nivel, grupo_enemigos, grupo_salida, grupo_balas_1, grupo_balas_2, grupo_balas_3, grupo_jefe):
        if self.fin_del_juego >= 1:
            self.desplazamiento_x = 0
            self.desplazamiento_y = 0

            if lista_teclas[pygame.K_LEFT]:
                self.desplazamiento_x -= self.velocidad
                self.contador += 1
                self.giro = True
            elif lista_teclas[pygame.K_RIGHT]:
                self.desplazamiento_x += self.velocidad
                self.contador += 1
                self.giro = False
            else:
                self.contador = 0
                self.indice = 0
                if self.esta_aire:
                    if self.giro:
                        imagen_salta = pygame.image.load("imagenes/spiderman/salta/3.png")
                        imagen_salta = pygame.transform.scale(imagen_salta,(40, 55))
                        imagen_salta = pygame.transform.flip(imagen_salta,True,False)
                        self.imagen = imagen_salta
                    else:
                        imagen_salta = pygame.image.load("imagenes/spiderman/salta/3.png") 
                        self.imagen = pygame.transform.scale(imagen_salta,(40, 55))
                else:
                    if self.giro:
                        self.imagen = self.lista_imagenes_izquierda[0]
                    else:
                        self.imagen = self.lista_imagenes_derecha[0]

            if lista_teclas[pygame.K_UP] and self.esta_saltando == False and self.esta_aire == False:
                self.sonido_salto.play()
                self.sonido_salto.set_volume(0.2)
                self.velocidad_salto = -16
                self.esta_saltando = True
            if lista_teclas[pygame.K_UP] == False:
                self.esta_saltando = False

            if lista_teclas[pygame.K_SPACE]:
                calculo = pygame.time.get_ticks()
                if calculo - self.ultimo_disparo > 250 and len(self.lista_proyectiles) < 3:
                    proyectil = Proyectil()
                    if self.giro:
                        proyectil.velocidad = -10
                        proyectil.rect.x = self.rect.x + 5
                        proyectil.rect.y = self.rect.y + 20
                    else:
                        proyectil.velocidad = 10
                        proyectil.rect.x = self.rect.x + 45
                        proyectil.rect.y = self.rect.y + 20
                    self.lista_proyectiles.append(proyectil)
                    self.sonido_disparo.play()
                    self.sonido_disparo.set_volume(0.2)
                    self.ultimo_disparo = calculo
            self.dibujar_proyectil(grupo_enemigos, nivel, grupo_jefe)

            # Grabedad
            self.velocidad_salto += 1
            if self.velocidad_salto > 20:
                self.velocidad_salto = 20
            self.desplazamiento_y += self.velocidad_salto

            self.colisiones_plataformas(nivel)
            self.colisiones_enemigos(grupo_enemigos, grupo_balas_1, grupo_balas_2, grupo_balas_3,grupo_jefe)
            self.colisiones_salida(grupo_salida)

            # Se actualizan las cordenadas del heroe
            self.rect.x += self.desplazamiento_x
            self.rect.y += self.desplazamiento_y

            self.limitar_pantalla()
        elif self.fin_del_juego == 0: # Fin del juego
            if self.giro:
                imagen_fin = pygame.transform.flip(self.imagen_fin,True,False)
                self.imagen = imagen_fin
            else:
                self.imagen = self.imagen_fin

        self.animar_heroe()

        return [self.fin_del_juego, self.cantidad_enemigos_eliminados, self.vidas_jefe]

    def colisiones_plataformas(self, nivel):
        self.esta_aire = True
        for rectangulo_plataforma in nivel.lista_img_rect:
            if rectangulo_plataforma[1].colliderect(self.rect.x + self.desplazamiento_x, self.rect.y, self.width, self.height):
                self.desplazamiento_x = 0

            if rectangulo_plataforma[1].colliderect(self.rect.x, self.rect.y + self.desplazamiento_y, self.width, self.height):
                if self.velocidad_salto < 0: # SUBIENDO
                    self.desplazamiento_y = rectangulo_plataforma[1].bottom - self.rect.top
                    self.velocidad_salto = 0
                elif self.velocidad_salto >= 0: # BAJANDO
                    self.desplazamiento_y = rectangulo_plataforma[1].top - self.rect.bottom
                    self.velocidad_salto = 0
                    self.esta_aire = False

    def colisiones_enemigos(self, grupo_enemigos, grupo_balas_1, grupo_balas_2, grupo_balas_3, grupo_jefe):
        if (pygame.sprite.spritecollide(self,grupo_enemigos,False) or
            pygame.sprite.spritecollide(self,grupo_balas_1,False) or
            pygame.sprite.spritecollide(self,grupo_balas_2,False) or
            pygame.sprite.spritecollide(self,grupo_balas_3,False) or
            pygame.sprite.spritecollide(self,grupo_jefe,False)):
            self.cantidad_colisiones += 1
            if self.cantidad_colisiones == 3:
                self.fin_del_juego = 0

    def colisiones_salida(self, grupo_salida):
        if pygame.sprite.spritecollide(self,grupo_salida,False):
            if self.fin_del_juego == 1:
                self.fin_del_juego = 2
            elif self.fin_del_juego == 2:
                self.fin_del_juego = 3

    def dibujar_proyectil(self, grupo_enemigos, nivel, grupo_jefe):
        for i in range(len(self.lista_proyectiles)):
            self.lista_proyectiles[i].dibujar(self.pantalla)
            self.lista_proyectiles[i].trayectoria()
            rect_proyectil = self.lista_proyectiles[i].rect
            if pygame.sprite.spritecollide(self.lista_proyectiles[i],grupo_enemigos,True):
                self.sonido_enemigo_golpeado.play()
                self.sonido_enemigo_golpeado.set_volume(0.2)
                self.cantidad_enemigos_eliminados += 1
                del self.lista_proyectiles[i]
                break
            if pygame.sprite.spritecollide(self.lista_proyectiles[i],grupo_jefe,False):
                if self.vidas_jefe > 0:
                    self.sonido_jefe_golpeado.play()
                    self.sonido_jefe_golpeado.set_volume(0.2)
                self.vidas_jefe -= 1
                if self.vidas_jefe <= 0:
                    self.vidas_jefe = 0
                del self.lista_proyectiles[i]
                break
            if (self.lista_proyectiles[i].rect.left > 880 or self.lista_proyectiles[i].rect.right < 0):
                del self.lista_proyectiles[i]
                break
            for rectangulo_plataforma in nivel.lista_img_rect:
                if rectangulo_plataforma[1].colliderect(rect_proyectil):
                    del self.lista_proyectiles[i]
                    self.proyectil_colisiono_plataforma = True
            if self.proyectil_colisiono_plataforma:
                self.proyectil_colisiono_plataforma = False
                break

    def animar_heroe(self):
        refrescar = 0
        if self.contador > refrescar:
            self.contador = 0
            self.indice += 1
            if self.esta_aire:
                if self.giro:
                    imagen_salta = pygame.image.load("imagenes/spiderman/salta/3.png")
                    imagen_salta = pygame.transform.scale(imagen_salta,(40, 55))
                    imagen_salta = pygame.transform.flip(imagen_salta,True,False)
                    self.imagen = imagen_salta
                else:
                    imagen_salta = pygame.image.load("imagenes/spiderman/salta/3.png") 
                    self.imagen = pygame.transform.scale(imagen_salta,(40, 55))
            else:
                if self.indice >= len(self.lista_imagenes_derecha):
                    self.indice = 0
                if self.giro:
                    self.imagen = self.lista_imagenes_izquierda[self.indice]
                else:
                    self.imagen = self.lista_imagenes_derecha[self.indice]
        self.pantalla.blit(self.imagen,self.rect)

    def limitar_pantalla(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.desplazamiento_x = 0
        if self.rect.right > self.pantalla.get_width():
            self.rect.right = self.pantalla.get_width()
            self.desplazamiento_x = 0

    def vidas_en_pantalla(self, pantalla, tamaño_pantalla, vidas):
        imagen_vidas = pygame.image.load(f"imagenes/cantidad_vida/{vidas}.png")
        imagen_vidas = pygame.transform.scale(imagen_vidas, (86,31))
        pantalla.blit(imagen_vidas, (tamaño_pantalla[0] - 820, tamaño_pantalla[1] -40))

class Proyectil(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"imagenes\spiderman\tira_tela\3.png")
        self.rect = self.image.get_rect()
        self.velocidad = 10

    def trayectoria(self):
        self.rect.left  = self.rect.left  + self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)























