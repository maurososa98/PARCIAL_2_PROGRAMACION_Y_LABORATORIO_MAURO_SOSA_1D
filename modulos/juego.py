from modulos.objetos_en_pantalla.clase_heroe import *
from modulos.objetos_en_pantalla.clase_creador_nivel import *
from modulos.objetos_en_pantalla.clase_enemigo import *
from modulos.objetos_en_pantalla.clase_jefe import *
from modulos.objetos_en_pantalla.clase_bala import *
from modulos.objetos_en_pantalla.clase_nivel_actual import *
from modulos.valores.colores import *
from modulos.valores.niveles import *
from modulos.configuracion import *
from modulos.funciones import *
from formularios.GUI_form_inicio import *
import pygame

class Juego(Configuracion):
    def __init__(self, tamaño_pantalla: tuple, FPS: int, titulo_pantalla: str, icono: str, imagen_fondo: str, fuente: str, musica: str):
        super().__init__(tamaño_pantalla, FPS, titulo_pantalla, icono, imagen_fondo, fuente)
        self.bandera_menu_principal = True
        self.bandera_nivel_1 = False
        self.paso_nivel_1 = False

        self.bandera_nivel_2 = False
        self.paso_nivel_2 = False

        self.bandera_nivel_3 = False
        self.paso_nivel_3 = False

        self.musica = musica

        self.puntos = 0
        self.vidas_spiderman = 3

        self.INICIA_CONTADOR = pygame.USEREVENT
        pygame.time.set_timer(self.INICIA_CONTADOR, 1000) # temposrizador
        self.contador_tiempo = 60

        self.pressed_keys = None
        self.fin_juego = 1
        self.reinicia_nivel = False
        self.sumar_puntos_enemigos_eliminados = False

        self.nivel = NivelActual(fondo_nivel_1, self.PANTALLA, self.tamaño_pantalla)
        self.form_inicio = FormInicio(self.PANTALLA, 0, 0, 880, 660, "blue", "black", r"imagenes\fondo\menu_principal.png", self.musica)
        
        imagen_game_over = pygame.image.load("imagenes/game_over.png")
        self.imagen_game_over = pygame.transform.scale(imagen_game_over, (520,390))
        self.bandera_game_over = False

        imagen_juego_ganado = pygame.image.load("imagenes/juego_ganado.png")
        self.imagen_juego_ganado = pygame.transform.scale(imagen_juego_ganado, (425,440))

    def texto_en_pantalla(self, texto, color, x, y):
        texto_en_pantalla = self.fuente.render(texto, True, color)
        self.PANTALLA.blit(texto_en_pantalla, (x,y))

    def init(self):
        pygame.init()
        while self.bandera_iniciar:
            self.reloj.tick(self.FPS)
            eventos = pygame.event.get()
            self.pressed_keys = pygame.key.get_pressed()

            self.puntos = self.nivel.puntos
            self.vidas_spiderman = self.nivel.vidas_spiderman

            if self.bandera_menu_principal:
                self.contador_tiempo = 60
                fondo = pygame.image.load(fondo_menu_principal)
                self.fondo = pygame.transform.scale(fondo, self.tamaño_pantalla)
                self.PANTALLA.blit(self.fondo,(0,0))
                self.form_inicio.update(eventos)

                if self.form_inicio.nivel_seleccionado() == "1":
                    self.contador_tiempo = 60
                    self.bandera_menu_principal = False
                    self.bandera_nivel_1 = True
                    self.bandera_nivel_2 = False
                    self.bandera_nivel_3 = False
                    self.nivel.heroe.rect.x = 55
                    self.nivel.heroe.rect.y = 554
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(musica_nivel_1)
                    pygame.mixer.music.play(-1)
                    self.nivel.set_imagen_fondo(fondo_nivel_1)
                elif self.form_inicio.nivel_seleccionado() == "2" and self.paso_nivel_1:
                    self.contador_tiempo = 60
                    self.bandera_menu_principal = False
                    self.bandera_nivel_1 = False
                    self.bandera_nivel_2 = True
                    self.bandera_nivel_3 = False
                    self.nivel.heroe.rect.x = 55
                    self.nivel.heroe.rect.y = 554
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(musica_nivel_2)
                    pygame.mixer.music.play(-1)
                    self.nivel.set_imagen_fondo(fondo_nivel_2)
                elif self.form_inicio.nivel_seleccionado() == "3" and self.paso_nivel_2:
                    self.contador_tiempo = 60
                    self.bandera_menu_principal = False
                    self.bandera_nivel_1 = False
                    self.bandera_nivel_2 = False
                    self.bandera_nivel_3 = True
                    self.nivel.heroe.rect.x = 55
                    self.nivel.heroe.rect.y = 554
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(musica_nivel_3)
                    pygame.mixer.music.play(-1)
                    self.nivel.set_imagen_fondo(fondo_nivel_3)

            if self.bandera_nivel_1:
                if self.contador_tiempo > 0:
                    self.nivel.update_nivel_uno(self.pressed_keys)
                    self.fin_juego = self.nivel.registro_nivel()
                if self.contador_tiempo <= 0 or self.fin_juego == 0:
                    self.PANTALLA.blit(self.imagen_game_over, (180,135))
                    self.bandera_game_over = True

                if self.fin_juego == 2:
                    self.paso_nivel_1 = True
                    self.contador_tiempo = 60
                    self.bandera_nivel_1 = False
                    self.bandera_nivel_2 = True
                    self.nivel.heroe.rect.x = 55
                    self.nivel.heroe.rect.y = 554
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(musica_nivel_2)
                    pygame.mixer.music.play(-1)
                    self.nivel.set_imagen_fondo(fondo_nivel_2)

            if self.bandera_nivel_2:
                if self.contador_tiempo > 0:
                    self.nivel.update_nivel_dos(self.pressed_keys)
                    self.fin_juego = self.nivel.registro_nivel()
                if self.contador_tiempo <= 0 or self.fin_juego == 0:
                    self.PANTALLA.blit(self.imagen_game_over, (180,135))
                    self.bandera_game_over = True

                if self.fin_juego == 3:
                    self.paso_nivel_2 = True
                    self.contador_tiempo = 60
                    self.bandera_nivel_2 = False
                    self.bandera_nivel_3 = True
                    self.nivel.heroe.rect.x = 55
                    self.nivel.heroe.rect.y = 554
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(musica_nivel_3)
                    pygame.mixer.music.play(-1)
                    self.nivel.set_imagen_fondo(fondo_nivel_3)

            if self.bandera_nivel_3:
                if self.nivel.jefe_muerto == False:
                    if self.contador_tiempo > 0:
                        self.nivel.update_nivel_tres(self.pressed_keys, self.reinicia_nivel)
                        self.fin_juego = self.nivel.registro_nivel()
                    if self.contador_tiempo <= 0 or self.fin_juego == 0:
                        self.PANTALLA.blit(self.imagen_game_over, (180,135))
                        self.bandera_game_over = True
                else:
                    # if self.sumar_puntos_enemigos_eliminados == False:
                    #     print("HolaaAAAAAAAAAAAAAAAA")
                    #     self.puntos += self.nivel.cant_enemigos_eliminados * 100
                    #     self.sumar_puntos_enemigos_eliminados = True
                    self.paso_nivel_3 = True
                    grupo_jefe.draw(self.PANTALLA)
                    self.PANTALLA.blit(self.imagen_juego_ganado, (227,0))
                    self.bandera_game_over = True
                    self.texto_en_pantalla(f"{self.puntos}", NEGRO,410,200)

            self.texto_en_pantalla(f"PUNTOS: {self.puntos}", NEGRO, self.tamaño_pantalla[0] - 200, self.tamaño_pantalla[1] -35)

            self.nivel.heroe.vidas_en_pantalla(self.PANTALLA, self.tamaño_pantalla, self.vidas_spiderman)

            pygame.draw.circle(self.PANTALLA, ROJO, (440,635), 20)
            texto_contador_tiempo = self.fuente.render(f"{(self.contador_tiempo):.0f}",False,BLANCO)
            self.PANTALLA.blit(texto_contador_tiempo, (430,625))

            for evento in eventos:
                if evento.type == pygame.QUIT:
                    self.bandera_iniciar = False
                elif (evento.type == self.INICIA_CONTADOR and (self.bandera_nivel_1 or self.bandera_nivel_2 or self.bandera_nivel_3) and self.bandera_game_over == False):
                    if self.contador_tiempo >= -1:
                        self.contador_tiempo -= 1
                elif evento.type == pygame.KEYDOWN:
                    nombre = pygame.key.name(evento.key) 
                    if (nombre == "return" and self.bandera_game_over) and self.paso_nivel_3 == False:# reset si pierde en nivel 1 - 2 - 3
                        self.reset_valores()

                    if (nombre == "return" and self.bandera_game_over) and self.paso_nivel_3:# reset si gana el nivel 3
                        # CARGA DE DATOS CSV: ------------------------
                        try:
                            with open("data/registro_partidas.csv","a") as archivo:
                                fila_dato = f"{self.puntos}\n"
                                archivo.write(fila_dato)
                        except PermissionError:
                            print("ERROR, el archivo de registro de partidas se encuentra abierto.")
                        except Exception as ex:
                            print(f"ERROR, se produjo un error del tipo: {type(ex)}")
                        # --------------------------------------------

                        self.paso_nivel_1 = False
                        self.paso_nivel_2 = False
                        self.paso_nivel_3 = False
                        self.nivel.jefe_muerto = False
                        
                        self.reset_valores()
            pygame.display.flip()
        pygame.quit()
    
    def eliminar_objetos_nivel(self):
        pygame.sprite.Group.empty(grupo_enemigos_nivel_1)
        pygame.sprite.Group.empty(grupo_vidas_nivel_1)
        pygame.sprite.Group.empty(grupo_puntos_nivel_1)
        pygame.sprite.Group.empty(grupo_salida_nivel_1)
        self.nivel.nivel_1.eliminar_plataformas()
        
        pygame.sprite.Group.empty(grupo_enemigos_nivel_2)
        pygame.sprite.Group.empty(grupo_vidas_nivel_2)
        pygame.sprite.Group.empty(grupo_puntos_nivel_2)
        pygame.sprite.Group.empty(grupo_salida_nivel_2)
        self.nivel.nivel_2.eliminar_plataformas()
        
        pygame.sprite.Group.empty(grupo_enemigos_nivel_3)
        pygame.sprite.Group.empty(grupo_vidas_nivel_3)
        pygame.sprite.Group.empty(grupo_puntos_nivel_3)
        pygame.sprite.Group.empty(grupo_salida_nivel_3)
        pygame.sprite.Group.empty(grupo_jefe)
        lista_jefe.clear()
        self.nivel.nivel_3.eliminar_plataformas()
    
    def rellenar_objetos_nivel(self):
        self.nivel.nivel_1.rellenar_diccionario_nivel("imagenes/fondo/piso.png",
                                        "imagenes/fondo/plataforma.png",
                                        "imagenes/fondo/plataforma_edificio.png",
                                        "imagenes/trampa/trampa_piso.png",
                                        "imagenes/trampa/trampa_pared.png",
                                        "imagenes/trampa/trampa_techo.png",1)
        self.nivel.nivel_2.rellenar_diccionario_nivel("imagenes/fondo/piso.png",
                                        "imagenes/fondo/plataforma.png",
                                        "imagenes/fondo/plataforma_edificio.png",
                                        "imagenes/trampa/trampa_piso.png",
                                        "imagenes/trampa/trampa_pared.png",
                                        "imagenes/trampa/trampa_techo.png",2)
        self.nivel.nivel_3.rellenar_diccionario_nivel("imagenes/fondo/piso.png",
                                        "imagenes/fondo/plataforma.png",
                                        "imagenes/fondo/plataforma_edificio.png",
                                        "imagenes/trampa/trampa_piso.png",
                                        "imagenes/trampa/trampa_pared.png",
                                        "imagenes/trampa/trampa_techo.png",3)
    
    def reset_valores(self):
        self.nivel.cant_enemigos_eliminados = 0
        self.nivel.heroe.cantidad_colisiones = 0
        self.nivel.heroe.fin_del_juego = 1
        self.nivel.vidas_spiderman = 3
        self.reinicia_nivel = True
        self.nivel.heroe.vidas_jefe = 28

        self.nivel.puntos = 0
        self.bandera_menu_principal = True
        self.bandera_nivel_1 = False
        self.bandera_nivel_2 = False
        self.bandera_nivel_3 = False
        self.form_inicio.form_comenzar_juego.seleccion_nivel = "0"
        self.bandera_game_over = False

        self.eliminar_objetos_nivel()
        self.rellenar_objetos_nivel()























