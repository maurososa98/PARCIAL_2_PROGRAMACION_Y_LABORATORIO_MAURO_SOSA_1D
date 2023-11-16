from modulos.objetos_en_pantalla.clase_heroe import *
from modulos.objetos_en_pantalla.clase_nivel import *
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

# NIVELES -----------------------------------------------------
nivel_0 = Nivel(datos_nivel_0, 55)
nivel_0.rellenar_diccionario_nivel("imagenes/fondo/piso.png",
                                   "imagenes/fondo/plataforma.png",
                                   "imagenes/fondo/plataforma_edificio.png",
                                   "imagenes/trampa/trampa_piso.png",
                                   "imagenes/trampa/trampa_pared.png",
                                   "imagenes/trampa/trampa_techo.png")

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

bala_1 = CreadorBalas()
bala_2 = CreadorBalas()
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

    def set_heroe(self):
        # posicion_inicial_x = 55
        # posicion_inicial_y = 554
        posicion_inicial_x = 55
        posicion_inicial_y = 0
        self.heroe = Heroe(lista_camina_derecha,lista_camina_izquierda,(posicion_inicial_x,posicion_inicial_y),6,self.PANTALLA,self.tamaño_pantalla[0])

    def mover_heroe(self, nivel):
        self.heroe.mover(self.pressed_keys, nivel) 

    def blit_fondo(self):
        self.PANTALLA.blit(self.fondo,(0,0))
        self.PANTALLA.get_width()

    def init(self):
        pygame.init()
        while self.bandera_iniciar:
            self.reloj.tick(self.FPS)

            if self.bandera_menu_principal:
                self.blit_fondo()
                nivel_0.dibujar_plataformas(self.PANTALLA)

                self.get_pressed()
                self.mover_heroe(nivel_0)

            if self.bandera_nivel_1:
                self.blit_fondo()
                nivel_1.dibujar_plataformas(self.PANTALLA)
                nivel_1.dibujar_salida(lista_imagenes_salida, self.PANTALLA, (825,55))

                grupo_enemigos_nivel_1.update()
                grupo_enemigos_nivel_1.draw(self.PANTALLA)
                
                grupo_puntos_nivel_1.update()
                grupo_puntos_nivel_1.draw(self.PANTALLA)
                
                grupo_vidas_nivel_1.update()
                grupo_vidas_nivel_1.draw(self.PANTALLA)
                
                bala_1.crear_bala((190,425))
                bala_1.dibujar_bala(self.PANTALLA, self.tamaño_pantalla[0])

                bala_2.crear_bala((405,270))
                bala_2.dibujar_bala(self.PANTALLA, self.tamaño_pantalla[0])

                bala_3.crear_bala((625,535))
                bala_3.dibujar_bala(self.PANTALLA, self.tamaño_pantalla[0])

                self.get_pressed()
                self.mover_heroe(nivel_1)

            if self.bandera_nivel_2:
                
                self.blit_fondo()
                nivel_2.dibujar_plataformas(self.PANTALLA)
                nivel_2.dibujar_salida(lista_imagenes_salida, self.PANTALLA, (825,550))
                
                grupo_enemigos_nivel_2.update()
                grupo_enemigos_nivel_2.draw(self.PANTALLA)
                
                grupo_puntos_nivel_2.update()
                grupo_puntos_nivel_2.draw(self.PANTALLA)
                
                grupo_vidas_nivel_2.update()
                grupo_vidas_nivel_2.draw(self.PANTALLA)
                
                
                bala_1.crear_bala((350,550))
                bala_1.dibujar_bala(self.PANTALLA, self.tamaño_pantalla[0])

                bala_2.crear_bala((535,350))
                bala_2.dibujar_bala(self.PANTALLA, self.tamaño_pantalla[0], True)

                bala_3.crear_bala((55,130))
                bala_3.dibujar_bala(self.PANTALLA, self.tamaño_pantalla[0], True)

                self.get_pressed()
                self.mover_heroe(nivel_2)

            if self.bandera_nivel_3:
                self.blit_fondo()
                nivel_3.dibujar_plataformas(self.PANTALLA)
                
                grupo_enemigos_nivel_3.update()
                grupo_enemigos_nivel_3.draw(self.PANTALLA)
                
                grupo_puntos_nivel_3.update()
                grupo_puntos_nivel_3.draw(self.PANTALLA)
                
                grupo_vidas_nivel_3.update()
                grupo_vidas_nivel_3.draw(self.PANTALLA)
                
                #grupo_jefe.update()
                lista_jefe[0].animar_salto(nivel_3)
                grupo_jefe.draw(self.PANTALLA)
                
                bala_1.crear_bala((55,195))
                bala_1.dibujar_bala(self.PANTALLA, self.tamaño_pantalla[0], True)

                bala_2.crear_bala((185,535))
                bala_2.dibujar_bala(self.PANTALLA, self.tamaño_pantalla[0])

                bala_3.crear_bala((680,535))
                bala_3.dibujar_bala(self.PANTALLA, self.tamaño_pantalla[0])

                self.get_pressed()
                self.mover_heroe(nivel_3)

            if self.bandera_menu_pausa:
                pass

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.bandera_iniciar = False
             
                elif evento.type == pygame.KEYDOWN:
                    nombre = pygame.key.name(evento.key) 
                    if nombre == "return": # ENTER
                        # tiempo_inicial = pygame.time.get_ticks()
                        self.bandera_menu_principal = False
                        self.bandera_nivel_1 = True
                        self.heroe.rectangulo.x = 55
                        self.heroe.rectangulo.y = 554
                        self.set_imagen_fondo(fondo_nivel_1)
                        self.parar_musica()
                        self.set_musica(musica_nivel_1)
                        self.reproducir_musica()
                # elif evento.type == pygame.MOUSEBUTTONDOWN and self.bandera_juego:
                #     pos_x = evento.pos[0]
                #     pos_y = evento.pos[1]
                #     if (pos_x >= 15 and pos_x <= (15 + 285) and # NIVEL 1
                #         pos_y >= 400 and pos_y <= (400 + 75)):
                #         pass
                #     if (pos_x >= 15 and pos_x <= (15 + 285) and # NIVEL 2
                #         pos_y >= 400 and pos_y <= (400 + 75)):
                #         pass
                #     if (pos_x >= 15 and pos_x <= (15 + 285) and # NIVEL 3
                #         pos_y >= 400 and pos_y <= (400 + 75)):
                #         pass

            pygame.display.flip()

        pygame.quit()

    def get_pressed(self):
        self.pressed_keys = pygame.key.get_pressed()
