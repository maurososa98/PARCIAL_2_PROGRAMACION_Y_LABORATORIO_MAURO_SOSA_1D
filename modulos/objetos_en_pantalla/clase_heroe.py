import pygame
class Heroe:
    def __init__(self, lista_imagenes_derecha:list, lista_imagenes_izquierda:list, posicion:tuple, velocidad:int, pantalla:pygame.Surface, ancho_pantalla:int):
        self.lista_imagenes_derecha = lista_imagenes_derecha
        self.lista_imagenes_izquierda = lista_imagenes_izquierda

        self.indice = 0
        self.contador = 0

        self.imagen = self.lista_imagenes_derecha[self.indice]
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = posicion[0]
        self.rectangulo.y = posicion[1]
        self.width = self.imagen.get_width()
        self.height = self.imagen.get_height()

        self.velocidad = velocidad
        self.pantalla = pantalla

        self.giro = False
        self.lista_proyectiles = []
        self.ultimo_disparo = pygame.time.get_ticks()
        self.sonido_disparo = pygame.mixer.Sound(("musica\disparar.mp3"))

        self.desplazamiento_x = 0
        self.desplazamiento_y = 0

        self.velocidad_salto = 0
        self.esta_saltando = False
        self.giro = False

        self.esta_aire = True

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def mover(self, lista_teclas, nivel):
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
                    proyectil.rectangulo.x = self.rectangulo.x + 5
                    proyectil.rectangulo.y = self.rectangulo.y + 20
                else:
                    proyectil.velocidad = 10
                    proyectil.rectangulo.x = self.rectangulo.x + 45
                    proyectil.rectangulo.y = self.rectangulo.y + 20
                self.lista_proyectiles.append(proyectil)
                self.sonido_disparo.play()
                self.sonido_disparo.set_volume(0.2)
                self.ultimo_disparo = calculo
        self.dibujar_proyectil()

        # Grabedad
        self.velocidad_salto += 1
        if self.velocidad_salto > 20:
            self.velocidad_salto = 20
        self.desplazamiento_y += self.velocidad_salto

        self.coliciones(nivel)

        # Se actualizan las cordenadas del heroe
        self.rectangulo.x += self.desplazamiento_x
        self.rectangulo.y += self.desplazamiento_y

        self.animar_heroe()
        self.limitar_pantalla()

    def coliciones(self, nivel):
        self.esta_aire = True
        for rectangulo_plataforma in nivel.lista_img_rect:
            if rectangulo_plataforma[1].colliderect(self.rectangulo.x + self.desplazamiento_x, self.rectangulo.y, self.width, self.height):
                self.desplazamiento_x = 0

            if rectangulo_plataforma[1].colliderect(self.rectangulo.x, self.rectangulo.y + self.desplazamiento_y, self.width, self.height):
                if self.velocidad_salto < 0: # SUBIENDO
                    self.desplazamiento_y = rectangulo_plataforma[1].bottom - self.rectangulo.top
                    self.velocidad_salto = 0
                elif self.velocidad_salto >= 0: # BAJANDO
                    self.desplazamiento_y = rectangulo_plataforma[1].top - self.rectangulo.bottom
                    self.velocidad_salto = 0
                    self.esta_aire = False

    def dibujar_proyectil(self):
        for i in range(len(self.lista_proyectiles)):
            self.lista_proyectiles[i].dibujar(self.pantalla)
            self.lista_proyectiles[i].trayectoria()
            if self.lista_proyectiles[i].rectangulo.left > 880 or self.lista_proyectiles[i].rectangulo.right < 0:
                del self.lista_proyectiles[i]
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
        self.pantalla.blit(self.imagen,self.rectangulo)

    def limitar_pantalla(self):
        if self.rectangulo.left < 0:
            self.rectangulo.left = 0
            self.desplazamiento_x = 0
        if self.rectangulo.right > self.pantalla.get_width():
            self.rectangulo.right = self.pantalla.get_width()
            self.desplazamiento_x = 0



class Proyectil(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load(r"imagenes\spiderman\tira_tela\3.png")
        self.rectangulo = self.imagen.get_rect()
        self.velocidad = 10

    def trayectoria(self):
        self.rectangulo.left  = self.rectangulo.left  + self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rectangulo)
