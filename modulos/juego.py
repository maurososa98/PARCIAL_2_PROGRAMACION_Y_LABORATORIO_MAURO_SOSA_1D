from modulos.objetos_en_pantalla.clase_heroe import *
from modulos.objetos_en_pantalla.clase_nivel import *
from modulos.objetos_en_pantalla.clase_enemigo import *
from modulos.objetos_en_pantalla.clase_jefe import *
from modulos.objetos_en_pantalla.clase_bala import *
from modulos.valores.colores import *
from modulos.valores.niveles import *
from modulos.configuracion import *
from modulos.funciones import *
import pygame

# HEROE -----------------------------------------------------
escala_heroe = (38,50)
lista_camina_derecha = lista_imagenes("imagenes/spiderman/camina/0.png",11,escala_heroe)
lista_camina_izquierda = lista_imagenes("imagenes/spiderman/camina/0.png",11,escala_heroe,True)

lista_camina_derecha_poder = lista_imagenes("imagenes/spiderman_poder/camina/0.png",8,escala_heroe)
lista_camina_izquierda_poder = lista_imagenes("imagenes/spiderman_poder/camina/0.png",8,escala_heroe,True)

# MUSICA -----------------------------------------------------
musica_pausa = "musica/menu_pausa.mp3"
musica_nivel_1 = "musica/nivel_1.mp3"
musica_nivel_2 = "musica/nivel_2.mp3"
musica_nivel_3 = "musica/nivel_3.mp3"

nivel_1 = Nivel(datos_nivel_1, 55)
nivel_1.rellenar_diccionario_nivel("imagenes/fondo/piso.png",
                                   "imagenes/fondo/plataforma.png",
                                   "imagenes/fondo/plataforma_edificio.png",
                                   "imagenes/trampa/trampa_piso.png",
                                   "imagenes/trampa/trampa_pared.png",
                                   "imagenes/trampa/trampa_techo.png",1)

nivel_2 = Nivel(datos_nivel_2, 55)
nivel_2.rellenar_diccionario_nivel("imagenes/fondo/piso.png",
                                   "imagenes/fondo/plataforma.png",
                                   "imagenes/fondo/plataforma_edificio.png",
                                   "imagenes/trampa/trampa_piso.png",
                                   "imagenes/trampa/trampa_pared.png",
                                   "imagenes/trampa/trampa_techo.png",2)

nivel_3 = Nivel(datos_nivel_3, 55)
nivel_3.rellenar_diccionario_nivel("imagenes/fondo/piso.png",
                                   "imagenes/fondo/plataforma.png",
                                   "imagenes/fondo/plataforma_edificio.png",
                                   "imagenes/trampa/trampa_piso.png",
                                   "imagenes/trampa/trampa_pared.png",
                                   "imagenes/trampa/trampa_techo.png",3)

grupo_bala_1 = pygame.sprite.Group()
bala_1 = CreadorBalas()

grupo_bala_2 = pygame.sprite.Group()
bala_2 = CreadorBalas()

grupo_bala_3 = pygame.sprite.Group()
bala_3 = CreadorBalas()

lista_imagenes_salida = lista_imagenes("imagenes/salida/0.png", 12, (45,45))

fondo_menu_pausa = "imagenes/fondo/menu_pausa.png"
fondo_nivel_1 = "imagenes/fondo/fondo_1.png"
fondo_nivel_2 = "imagenes/fondo/fondo_2.png"
fondo_nivel_3 = "imagenes/fondo/fondo_3.png"

musica_menu_pausa = "musica/menu_pausa.mp3"
musica_nivel_1 = "musica/nivel_1.mp3"
musica_nivel_2 = "musica/nivel_2.mp3"
musica_nivel_3 = "musica/nivel_3.mp3"


class Juego(Configuracion):
    def __init__(self, tamaño_pantalla: tuple, FPS: int, titulo_pantalla: str, icono: str, imagen_fondo: str, fuente: str, musica: str):
        super().__init__(tamaño_pantalla, FPS, titulo_pantalla, icono, imagen_fondo, fuente, musica)
        self.bandera_menu_principal = True
        self.bandera_nivel_1 = False
        self.bandera_nivel_2 = False
        self.bandera_nivel_3 = False
        self.bandera_menu_pausa = False

        self.set_heroe()
        self.pressed_keys = []
        self.fin_juego = 1
        self.cant_colisiones = 0
        self.datos = 0
        
        self.puntos = 0
        self.sonido_puntos = pygame.mixer.Sound(("musica/punto.wav"))

        self.vidas_spiderman = 3
        self.vidas_jefe = 28
        self.jefe_muerto = False
        
        self.sonido_vidas = pygame.mixer.Sound(("musica/vida.wav"))
        self.sonido_reta_vida = pygame.mixer.Sound(("musica/resta_vida.wav"))
        self.sonido_enemigo_golpeado = pygame.mixer.Sound(("musica/enemigo_golpeado.wav"))
        self.cant_enemigos_eliminados = 0

    def set_heroe(self):
        posicion_inicial_x = 55
        posicion_inicial_y = 0
        self.heroe = Heroe(lista_camina_derecha,lista_camina_izquierda,(posicion_inicial_x,posicion_inicial_y),6,self.PANTALLA,self.tamaño_pantalla[0])

    def mover_heroe(self, nivel, grupo_enemigos, grupo_salida, grupo_balas_1, grupo_balas_2, grupo_balas_3, grupo_jefe= []):
        datos = self.heroe.mover(self.pressed_keys, nivel, grupo_enemigos, grupo_salida, grupo_balas_1, grupo_balas_2, grupo_balas_3, grupo_jefe)
        self.fin_juego = datos[0]
        self.cant_colisiones = datos[1]
        self.cant_enemigos_eliminados = datos[2]
        self.vidas_jefe = datos[3]

    def blit_fondo(self):
        self.PANTALLA.blit(self.fondo,(0,0))
        self.PANTALLA.get_width()

    def texto_en_pantalla(self, texto, color, x, y):
        texto_en_pantalla = self.fuente.render(texto, True, color)
        self.PANTALLA.blit(texto_en_pantalla, (x,y))

    def init(self):
        pygame.init()
        while self.bandera_iniciar:
            self.reloj.tick(self.FPS)

            if self.bandera_menu_principal:
                self.blit_fondo()

            if self.bandera_nivel_1:
                self.blit_fondo()
                nivel_1.dibujar_plataformas(self.PANTALLA)

                grupo_enemigos_nivel_1.update()
                grupo_puntos_nivel_1.update()
                grupo_vidas_nivel_1.update()
                grupo_salida_nivel_1.update()

                grupo_enemigos_nivel_1.draw(self.PANTALLA)
                grupo_puntos_nivel_1.draw(self.PANTALLA)
                grupo_vidas_nivel_1.draw(self.PANTALLA)
                grupo_salida_nivel_1.draw(self.PANTALLA)
                
                bala_1.crear_bala((190,425),self.PANTALLA,grupo_bala_1)
                bala_1.animar(grupo_bala_1, True, False)
                
                bala_2.crear_bala((405,270),self.PANTALLA,grupo_bala_2)
                bala_2.animar(grupo_bala_2, True, False)

                bala_3.crear_bala((625,535),self.PANTALLA,grupo_bala_3)
                bala_3.animar(grupo_bala_3, True, False)

                self.get_pressed()
                self.mover_heroe(nivel_1, grupo_enemigos_nivel_1, grupo_salida_nivel_1,grupo_bala_1, grupo_bala_2, grupo_bala_3)
                self.recolectar_puntos(grupo_puntos_nivel_1)
                self.recolectar_vidas(grupo_vidas_nivel_1)
                self.registro_colisiones(grupo_enemigos_nivel_1, grupo_bala_1, grupo_bala_2, grupo_bala_3)

                if self.fin_juego == 2:
                    self.bandera_nivel_1 = False
                    self.bandera_nivel_2 = True
                    self.heroe.rect.x = 55
                    self.heroe.rect.y = 554
                    self.set_imagen_fondo(fondo_nivel_2)
                    self.parar_musica()
                    self.set_musica(musica_nivel_2)
                    self.reproducir_musica()

            if self.bandera_nivel_2:
                self.blit_fondo()
                nivel_2.dibujar_plataformas(self.PANTALLA)
                
                grupo_enemigos_nivel_2.update()
                grupo_puntos_nivel_2.update()
                grupo_vidas_nivel_2.update()
                grupo_salida_nivel_2.update()
                
                grupo_enemigos_nivel_2.draw(self.PANTALLA)
                grupo_puntos_nivel_2.draw(self.PANTALLA)
                grupo_vidas_nivel_2.draw(self.PANTALLA)
                grupo_salida_nivel_2.draw(self.PANTALLA)
                
                bala_1.crear_bala((350,550),self.PANTALLA,grupo_bala_1)
                bala_1.animar(grupo_bala_1, True, False)
                
                bala_2.crear_bala((535,350),self.PANTALLA,grupo_bala_2)
                bala_2.animar(grupo_bala_2, False, True)

                bala_3.crear_bala((55,130),self.PANTALLA,grupo_bala_3)
                bala_3.animar(grupo_bala_3, False, True)

                self.get_pressed()
                self.mover_heroe(nivel_2, grupo_enemigos_nivel_2, grupo_salida_nivel_2,grupo_bala_1, grupo_bala_2, grupo_bala_3)
                self.recolectar_puntos(grupo_puntos_nivel_2)
                self.recolectar_vidas(grupo_vidas_nivel_2)
                self.registro_colisiones(grupo_enemigos_nivel_2, grupo_bala_1, grupo_bala_2, grupo_bala_3)
                
                if self.fin_juego == 3:
                    self.bandera_nivel_2 = False
                    self.bandera_nivel_3 = True
                    self.heroe.rect.x = 55
                    self.heroe.rect.y = 554
                    self.set_imagen_fondo(fondo_nivel_3)
                    self.parar_musica()
                    self.set_musica(musica_nivel_3)
                    self.reproducir_musica()

            if self.bandera_nivel_3:
                self.blit_fondo()
                nivel_3.dibujar_plataformas(self.PANTALLA)
                
                grupo_enemigos_nivel_3.update()
                grupo_puntos_nivel_3.update()
                grupo_vidas_nivel_3.update()
                grupo_salida_nivel_3.update()
                
                grupo_enemigos_nivel_3.draw(self.PANTALLA)
                grupo_puntos_nivel_3.draw(self.PANTALLA)
                grupo_vidas_nivel_3.draw(self.PANTALLA)
                grupo_salida_nivel_3.draw(self.PANTALLA)
                grupo_jefe.draw(self.PANTALLA)

                bala_1.crear_bala((55,195),self.PANTALLA,grupo_bala_1)
                bala_1.animar(grupo_bala_1, False, True)

                bala_2.crear_bala((185,535),self.PANTALLA,grupo_bala_2)
                bala_2.animar(grupo_bala_2, True, False)
                
                bala_3.crear_bala((680,535),self.PANTALLA,grupo_bala_3)
                bala_3.animar(grupo_bala_3, True, False)

                if self.vidas_jefe >= 14:
                    grupo_jefe.update()
                elif self.vidas_jefe < 14 and self.vidas_jefe > 0:
                    lista_jefe[0].animar_salto(nivel_3)
                elif self.vidas_jefe == 0 and self.jefe_muerto == False:
                    self.jefe_muerto = True
                    lista_jefe[0].rect.y += 62
                    lista_jefe[0].image = pygame.image.load("imagenes/venom/muere/6.png") 
                    
                lista_jefe[0].vidas_en_pantalla(self.PANTALLA, self.tamaño_pantalla, self.vidas_jefe)

                self.get_pressed()
                self.mover_heroe(nivel_3, grupo_enemigos_nivel_3, grupo_salida_nivel_3,grupo_bala_1, grupo_bala_2, grupo_bala_3,grupo_jefe)
                self.recolectar_puntos(grupo_puntos_nivel_3)
                self.recolectar_vidas(grupo_vidas_nivel_3)
                self.registro_colisiones(grupo_enemigos_nivel_3, grupo_bala_1, grupo_bala_2, grupo_bala_3,grupo_jefe)

            if self.bandera_menu_pausa:
                pass

            self.texto_en_pantalla(f"PUNTOS: {self.puntos}", NEGRO, self.tamaño_pantalla[0] - 200, self.tamaño_pantalla[1] -35)
            self.heroe.vidas_en_pantalla(self.PANTALLA, self.tamaño_pantalla, self.vidas_spiderman)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.bandera_iniciar = False
             
                elif evento.type == pygame.KEYDOWN:
                    nombre = pygame.key.name(evento.key) 
                    if nombre == "return": # ENTER
                        # tiempo_inicial = pygame.time.get_ticks()
                        self.bandera_menu_principal = False
                        self.bandera_nivel_1 = True
                        self.heroe.rect.x = 55
                        self.heroe.rect.y = 554
                        self.set_imagen_fondo(fondo_nivel_1)
                        self.parar_musica()
                        self.set_musica(musica_nivel_1)
                        self.reproducir_musica()
            pygame.display.flip()
        pygame.quit()

    def get_pressed(self):
        self.pressed_keys = pygame.key.get_pressed()

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
            self.sonido_reta_vida.play()
            self.sonido_reta_vida.set_volume(0.2)
            self.vidas_spiderman -= 1
            if self.vidas_spiderman <= 0:
                self.vidas_spiderman = 0
                self.puntos += self.cant_enemigos_eliminados * 100
            else:
                self.heroe.rect.x = 55
                self.heroe.rect.y = 554
                self.sonido_reta_vida.play()
                self.sonido_reta_vida.set_volume(0.2)



















