
from modulos.objetos_en_pantalla.clase_bala import *

from modulos.valores.niveles import *

from modulos.funciones import *
from modulos.objetos_en_pantalla.clase_nivel import *

class NivelActual(Niveles):
    def __init__(self, imagen_fondo, pantalla, tamaño_pantalla):
        super().__init__(imagen_fondo, pantalla, tamaño_pantalla)
        self.nivel_1 = CrearNivel(datos_nivel_1, 55)
        self.nivel_1.rellenar_diccionario_nivel("imagenes/fondo/piso.png",
                                        "imagenes/fondo/plataforma.png",
                                        "imagenes/fondo/plataforma_edificio.png",
                                        "imagenes/trampa/trampa_piso.png",
                                        "imagenes/trampa/trampa_pared.png",
                                        "imagenes/trampa/trampa_techo.png",1)
        self.nivel_2 = CrearNivel(datos_nivel_2, 55)
        self.nivel_2.rellenar_diccionario_nivel("imagenes/fondo/piso.png",
                                        "imagenes/fondo/plataforma.png",
                                        "imagenes/fondo/plataforma_edificio.png",
                                        "imagenes/trampa/trampa_piso.png",
                                        "imagenes/trampa/trampa_pared.png",
                                        "imagenes/trampa/trampa_techo.png",2)
        self.nivel_3 = CrearNivel(datos_nivel_3, 55)
        self.nivel_3.rellenar_diccionario_nivel("imagenes/fondo/piso.png",
                                        "imagenes/fondo/plataforma.png",
                                        "imagenes/fondo/plataforma_edificio.png",
                                        "imagenes/trampa/trampa_piso.png",
                                        "imagenes/trampa/trampa_pared.png",
                                        "imagenes/trampa/trampa_techo.png",3)

    def update_nivel_uno(self,pressed_keys):
        self.pressed_keys = pressed_keys
        self.blit_fondo()
        self.nivel_1.dibujar_plataformas(self.pantalla)

        grupo_enemigos_nivel_1.update()
        grupo_puntos_nivel_1.update()
        grupo_vidas_nivel_1.update()
        grupo_salida_nivel_1.update()

        grupo_enemigos_nivel_1.draw(self.pantalla)
        grupo_puntos_nivel_1.draw(self.pantalla)
        grupo_vidas_nivel_1.draw(self.pantalla)
        grupo_salida_nivel_1.draw(self.pantalla)
        
        bala_1.crear_bala((190,425),self.pantalla,grupo_bala_1)
        bala_1.animar(grupo_bala_1, True, False)
        
        bala_2.crear_bala((405,270),self.pantalla,grupo_bala_2)
        bala_2.animar(grupo_bala_2, True, False)

        bala_3.crear_bala((625,535),self.pantalla,grupo_bala_3)
        bala_3.animar(grupo_bala_3, True, False)
        
        self.mover_heroe(self.nivel_1, grupo_enemigos_nivel_1, grupo_salida_nivel_1,grupo_bala_1, grupo_bala_2, grupo_bala_3)
        self.recolectar_puntos(grupo_puntos_nivel_1)
        self.recolectar_vidas(grupo_vidas_nivel_1)
        self.registro_colisiones(grupo_enemigos_nivel_1, grupo_bala_1, grupo_bala_2, grupo_bala_3)

    def update_nivel_dos(self, pressed_keys):
        self.pressed_keys = pressed_keys
        self.blit_fondo()
        self.nivel_2.dibujar_plataformas(self.pantalla)

        grupo_enemigos_nivel_2.update()
        grupo_puntos_nivel_2.update()
        grupo_vidas_nivel_2.update()
        grupo_salida_nivel_2.update()
        
        grupo_enemigos_nivel_2.draw(self.pantalla)
        grupo_puntos_nivel_2.draw(self.pantalla)
        grupo_vidas_nivel_2.draw(self.pantalla)
        grupo_salida_nivel_2.draw(self.pantalla)
        
        bala_1.crear_bala((350,550),self.pantalla,grupo_bala_1)
        bala_1.animar(grupo_bala_1, True, False)
        
        bala_2.crear_bala((535,350),self.pantalla,grupo_bala_2)
        bala_2.animar(grupo_bala_2, False, True)

        bala_3.crear_bala((55,130),self.pantalla,grupo_bala_3)
        bala_3.animar(grupo_bala_3, False, True)
        
        self.mover_heroe(self.nivel_2, grupo_enemigos_nivel_2, grupo_salida_nivel_2,grupo_bala_1, grupo_bala_2, grupo_bala_3)
        self.recolectar_puntos(grupo_puntos_nivel_2)
        self.recolectar_vidas(grupo_vidas_nivel_2)
        self.registro_colisiones(grupo_enemigos_nivel_2, grupo_bala_1, grupo_bala_2, grupo_bala_3)
    
    def update_nivel_tres(self, pressed_keys, reinicia_nivel):
        self.pressed_keys = pressed_keys
        self.blit_fondo()
        self.nivel_3.dibujar_plataformas(self.pantalla)

        grupo_enemigos_nivel_3.update()
        grupo_puntos_nivel_3.update()
        grupo_vidas_nivel_3.update()
        grupo_salida_nivel_3.update()
        
        grupo_enemigos_nivel_3.draw(self.pantalla)
        grupo_puntos_nivel_3.draw(self.pantalla)
        grupo_vidas_nivel_3.draw(self.pantalla)
        grupo_salida_nivel_3.draw(self.pantalla)
        grupo_jefe.draw(self.pantalla)

        bala_1.crear_bala((55,195),self.pantalla,grupo_bala_1)
        bala_1.animar(grupo_bala_1, False, True)

        bala_2.crear_bala((185,535),self.pantalla,grupo_bala_2)
        bala_2.animar(grupo_bala_2, True, False)
        
        bala_3.crear_bala((680,535),self.pantalla,grupo_bala_3)
        bala_3.animar(grupo_bala_3, True, False)

        if (self.vidas_jefe >= 14) and reinicia_nivel == False:
            grupo_jefe.update()
        elif (self.vidas_jefe < 14 and self.vidas_jefe > 0 and reinicia_nivel == False) or (self.vidas_jefe > 0 and reinicia_nivel):
            lista_jefe[0].animar_salto(self.nivel_3)
        elif self.vidas_jefe == 0 and self.jefe_muerto == False:
            lista_jefe[0].rect.y += 62
            lista_jefe[0].image = pygame.image.load("imagenes/venom/muere/6.png")
            self.jefe_muerto = True
        lista_jefe[0].vidas_en_pantalla(self.pantalla, self.tamaño_pantalla, self.vidas_jefe)

        self.mover_heroe(self.nivel_3, grupo_enemigos_nivel_3, grupo_salida_nivel_3,grupo_bala_1, grupo_bala_2, grupo_bala_3, grupo_jefe)
        self.recolectar_puntos(grupo_puntos_nivel_3)
        self.recolectar_vidas(grupo_vidas_nivel_3)
        self.registro_colisiones(grupo_enemigos_nivel_3, grupo_bala_1, grupo_bala_2, grupo_bala_3, grupo_jefe)


  


    










































