# PARCIAL_2_PROGRAMACION_Y_LABORATORIO_MAURO_SOSA_1D

from modulos.juego import *

tamaño_pantalla = (880,660)
FPS = 30
titulo = "SPIDER-MAN"
icono = "imagenes/spiderman/camina/1.png"
fuente = "Swis721 Blk BT"

musica_menu_inicial = "musica/menu_inicial.mp3"
musica_menu_pausa = "musica/menu_pausa.mp3"
musica_nivel_1 = "musica/nivel_1.mp3"
musica_nivel_2 = "musica/nivel_2.mp3"
musica_nivel_3 = "musica/nivel_3.mp3"

fondo_menu_principal = "imagenes/fondo/menu_principal.png"
fondo_menu_pausa = "imagenes/fondo/menu_pausa.png"
fondo_nivel_1 = "imagenes/fondo/fondo_1.png"
fondo_nivel_2 = "imagenes/fondo/fondo_2.png"
fondo_nivel_3 = "imagenes/fondo/fondo_3.png"


juego = Juego(tamaño_pantalla, FPS, titulo, icono, fondo_menu_principal, fuente, musica_menu_inicial)
juego.init()


