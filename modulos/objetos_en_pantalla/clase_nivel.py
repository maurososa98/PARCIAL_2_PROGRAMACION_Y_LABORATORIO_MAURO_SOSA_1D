import pygame
from modulos.objetos_en_pantalla.clase_enemigo  import *
from modulos.objetos_en_pantalla.clase_jefe  import *
from modulos.objetos_en_pantalla.clase_objeto  import *
from modulos.funciones import *

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

                if img == 10:
                    jefe = Jefe(contador_columna * self.tamaño_cuadricula, contador_fila * self.tamaño_cuadricula -52, lista_imagenes_jefe_venom_derecha,2,65,lista_imagenes_jefe_venom_izquierda,lista_imagenes_jefe_venom_derecha,6)
                    grupo_jefe.add(jefe)
                    lista_jefe.append(jefe)
                if img == 11:
                    salida = Salida(contador_columna * self.tamaño_cuadricula, contador_fila * self.tamaño_cuadricula, lista_imagenes_salida,3)
                    if nivel == 1:
                        grupo_salida_nivel_1.add(salida)
                    elif nivel == 2:
                        grupo_salida_nivel_2.add(salida)
                    elif nivel == 3:
                        grupo_salida_nivel_3.add(salida)

                contador_columna += 1
            contador_fila += 1

    def dibujar_plataformas(self, pantalla):
        for i in range(len(self.lista_img_rect)):
            img_rect = self.lista_img_rect[i]
            pantalla.blit(img_rect[0],img_rect[1])

class Bala(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"imagenes\trampa\trampa_disparo.png")
        self.rect = self.image.get_rect()
        self.velocidad = 5
        self.ultimo_disparo = pygame.time.get_ticks()
        self.sonido_disparo = pygame.mixer.Sound(("musica/trampa_dispara.mp3"))

    def trayectoria(self, arriba:bool=True, derecha:bool=False):
        if arriba:
            self.rect.bottom -= self.velocidad
        if derecha:
            self.rect.left += self.velocidad
            self.imagen = pygame.transform.rotate(pygame.image.load(r"imagenes\trampa\trampa_disparo.png"), 270)
    
    def crear_bala(self, posicion:tuple):
        calculo = pygame.time.get_ticks()
        if calculo - self.ultimo_disparo > 700 and len(grupo_balas) < 1:
            bala = Bala()
            bala.rect.x = posicion[0]
            bala.rect.y = posicion[1]
            grupo_balas.add(bala)
            self.sonido_disparo.play()
            self.sonido_disparo.set_volume(0.01)
            self.ultimo_disparo = calculo
    
    def dibujar_bala(self, pantalla, ancho_pantalla, trayectoria_derecha:bool=False):
        for i in range(len(self.grupo_balas)):
            if trayectoria_derecha:
                self.grupo_balas[i].trayectoria(False,True)
            else:
                self.grupo_balas[i].trayectoria()
            pantalla.blit(self.grupo_balas[i].image, self.grupo_balas[i].rect)
            if self.grupo_balas[i].rect.bottom < 0 or self.listagrupo_balas_balas[i].rect.left > ancho_pantalla:
                del self.grupo_balas[i]



grupo_balas = pygame.sprite.Group()

# grupo_balas_nivel_2 = pygame.sprite.Group()
# grupo_balas_nivel_3 = pygame.sprite.Group()









































