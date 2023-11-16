import pygame
from modulos.objetos_en_pantalla.clase_enemigo  import *
from modulos.objetos_en_pantalla.clase_jefe  import *
from modulos.objetos_en_pantalla.clase_objeto  import *

class Nivel():
    def __init__(self, datos_nivel:list, tamaño_cuadricula:int):
        pygame.mixer.init()
        self.datos_nivel = datos_nivel
        self.tamaño_cuadricula = tamaño_cuadricula
        self.lista_img_rect = []
        self.indice = 0
        self.contador = 0

    def rellenar_diccionario_nivel(self, 
                                   ruta_1_piso:str, 
                                   ruta_2_plataforma:str, 
                                   ruta_3_plataforma:str, 
                                   ruta_4_trampa_piso:str, 
                                   ruta_5_trampa_pared:str,
                                   ruta_6_trampa_techo:str, nivel:int=0):
        self.ruta_1_piso = pygame.image.load(ruta_1_piso)
        self.ruta_2_plataforma = pygame.image.load(ruta_2_plataforma)
        self.ruta_3_plataforma = pygame.image.load(ruta_3_plataforma)
        self.ruta_4_trampa_piso = pygame.image.load(ruta_4_trampa_piso)
        self.ruta_5_trampa_pared = pygame.image.load(ruta_5_trampa_pared)
        self.ruta_6_trampa_techo = pygame.image.load(ruta_6_trampa_techo)

        contador_fila = 0
        for fila in self.datos_nivel:
            contador_columna = 0
            for img in fila:
                if img == 1:
                    imagen_escalada = pygame.transform.scale(self.ruta_1_piso,(self.tamaño_cuadricula, self.tamaño_cuadricula))
                    rectangulo_imagen = imagen_escalada.get_rect()
                    rectangulo_imagen.x = contador_columna * self.tamaño_cuadricula
                    rectangulo_imagen.y = contador_fila * self.tamaño_cuadricula
                    img_rect = (imagen_escalada, rectangulo_imagen)
                    self.lista_img_rect.append(img_rect)
                if img == 2:
                    imagen_escalada = pygame.transform.scale(self.ruta_2_plataforma,(self.tamaño_cuadricula, self.tamaño_cuadricula))
                    rectangulo_imagen = imagen_escalada.get_rect()
                    rectangulo_imagen.x = contador_columna * self.tamaño_cuadricula
                    rectangulo_imagen.y = contador_fila * self.tamaño_cuadricula
                    img_rect = (imagen_escalada, rectangulo_imagen)
                    self.lista_img_rect.append(img_rect)
                if img == 3:
                    imagen_escalada = pygame.transform.scale(self.ruta_3_plataforma,(self.tamaño_cuadricula, self.tamaño_cuadricula))
                    rectangulo_imagen = imagen_escalada.get_rect()
                    rectangulo_imagen.x = contador_columna * self.tamaño_cuadricula
                    rectangulo_imagen.y = contador_fila * self.tamaño_cuadricula
                    img_rect = (imagen_escalada, rectangulo_imagen)
                    self.lista_img_rect.append(img_rect)
                if img == 4:
                    imagen_escalada = pygame.transform.scale(self.ruta_4_trampa_piso,(self.tamaño_cuadricula, self.tamaño_cuadricula))
                    rectangulo_imagen = imagen_escalada.get_rect()
                    rectangulo_imagen.x = contador_columna * self.tamaño_cuadricula
                    rectangulo_imagen.y = contador_fila * self.tamaño_cuadricula
                    img_rect = (imagen_escalada, rectangulo_imagen)
                    self.lista_img_rect.append(img_rect)
                if img == 5:
                    imagen_escalada = pygame.transform.scale(self.ruta_5_trampa_pared,(self.tamaño_cuadricula, self.tamaño_cuadricula))
                    rectangulo_imagen = imagen_escalada.get_rect()
                    rectangulo_imagen.x = contador_columna * self.tamaño_cuadricula
                    rectangulo_imagen.y = contador_fila * self.tamaño_cuadricula
                    img_rect = (imagen_escalada, rectangulo_imagen)
                    self.lista_img_rect.append(img_rect)
                if img == 6:
                    imagen_escalada = pygame.transform.scale(self.ruta_6_trampa_techo,(self.tamaño_cuadricula, self.tamaño_cuadricula))
                    rectangulo_imagen = imagen_escalada.get_rect()
                    rectangulo_imagen.x = contador_columna * self.tamaño_cuadricula
                    rectangulo_imagen.y = contador_fila * self.tamaño_cuadricula
                    img_rect = (imagen_escalada, rectangulo_imagen)
                    self.lista_img_rect.append(img_rect)
                if img == 7:
                    enemigo = Enemigo(contador_columna * self.tamaño_cuadricula, contador_fila * self.tamaño_cuadricula + 9,lista_imagenes_enemigo_venom_derecha,0.5,50,lista_imagenes_enemigo_venom_izquierda,lista_imagenes_enemigo_venom_derecha, 2)
                    if nivel == 1:
                        grupo_enemigos_nivel_1.add(enemigo)
                    elif nivel == 2:
                        grupo_enemigos_nivel_2.add(enemigo)
                    elif nivel == 3:
                        grupo_enemigos_nivel_3.add(enemigo)

                if img == 8:
                    vida = ItemPunto(contador_columna * self.tamaño_cuadricula +16, contador_fila * self.tamaño_cuadricula +14, lista_imagenes_vida, 3)
                    if nivel == 1:
                        grupo_vidas_nivel_1.add(vida)
                    elif nivel == 2:
                        grupo_vidas_nivel_2.add(vida)
                    elif nivel == 3:
                        grupo_vidas_nivel_3.add(vida)

                if img == 9:
                    punto = ItemVida(contador_columna * self.tamaño_cuadricula +22, contador_fila * self.tamaño_cuadricula +19, lista_imagenes_punto,3)
                    if nivel == 1:
                        grupo_puntos_nivel_1.add(punto)
                    elif nivel == 2:
                        grupo_puntos_nivel_2.add(punto)
                    elif nivel == 3:
                        grupo_puntos_nivel_3.add(punto)

                if img == 10: # 65 grande, 
                    jefe = Jefe(contador_columna * self.tamaño_cuadricula, contador_fila * self.tamaño_cuadricula -52, lista_imagenes_jefe_venom_derecha,2,65,lista_imagenes_jefe_venom_izquierda,lista_imagenes_jefe_venom_derecha,6)
                    grupo_jefe.add(jefe)
                    lista_jefe.append(jefe)

                contador_columna += 1
            contador_fila += 1

    def dibujar_plataformas(self, pantalla):
        for i in range(len(self.lista_img_rect)):
            img_rect = self.lista_img_rect[i]
            pantalla.blit(img_rect[0],img_rect[1])

    def dibujar_salida(self, lista_imagenes:list, pantalla:pygame.Surface, posicion:tuple):
        lista_img_rect = []
        for i in range(len(lista_imagenes)):
            imagenes_salida = lista_imagenes[i]
            rectangulo_imagen = imagenes_salida.get_rect()
            rectangulo_imagen.x = posicion[0]
            rectangulo_imagen.y = posicion[1]
            img_rect = (imagenes_salida, rectangulo_imagen)
            lista_img_rect.append(img_rect)
        refrescar = 1
        self.contador += 1
        if self.contador > refrescar:
            self.contador = 0
            self.indice += 1
            if self.indice >= 12:
                self.indice = 0
        imagen_salida = lista_img_rect[self.indice]
        pantalla.blit(imagen_salida[0],imagen_salida[1])

class CreadorBalas():
    def __init__(self):
        self.lista_balas = []
        self.ultimo_disparo = pygame.time.get_ticks()
        self.sonido_disparo = pygame.mixer.Sound(("musica/trampa_dispara.mp3"))

    def crear_bala(self, posicion:tuple):
        calculo = pygame.time.get_ticks()
        if calculo - self.ultimo_disparo > 700 and len(self.lista_balas) < 1:
            bala = Bala()
            bala.rectangulo.x = posicion[0]
            bala.rectangulo.y = posicion[1]
            self.lista_balas.append(bala)
            self.sonido_disparo.play()
            self.sonido_disparo.set_volume(0.01)
            self.ultimo_disparo = calculo

    def dibujar_bala(self, pantalla, ancho_pantalla, trayectoria_derecha:bool=False):
        for i in range(len(self.lista_balas)):
            if trayectoria_derecha:
                self.lista_balas[i].trayectoria(False,True)
            else:
                self.lista_balas[i].trayectoria()
            pantalla.blit(self.lista_balas[i].imagen, self.lista_balas[i].rectangulo)
            if self.lista_balas[i].rectangulo.bottom < 0 or self.lista_balas[i].rectangulo.left > ancho_pantalla:
                del self.lista_balas[i]

class Bala(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load(r"imagenes\trampa\trampa_disparo.png")
        # self.imagen =  pygame.transform.scale(self.imagen, ())
        self.rectangulo = self.imagen.get_rect()
        self.velocidad = 5

    def trayectoria(self, arriba:bool=True, derecha:bool=False):
        if arriba:
            self.rectangulo.bottom -= self.velocidad
        if derecha:
            self.rectangulo.left += self.velocidad
            self.imagen = pygame.transform.rotate(pygame.image.load(r"imagenes\trampa\trampa_disparo.png"), 270)











































