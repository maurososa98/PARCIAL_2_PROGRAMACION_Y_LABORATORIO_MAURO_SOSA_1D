   # PAR CIAL_2_PROGRAMACION_Y_LABORATORIO_MAURO_SOSA_1D
from modulos.juego import *

tamaño_pantalla = (880,660)
FPS = 30
titulo = "SPIDER-MAN"
icono = "imagenes/spiderman/camina/1.png"
fuente = "Swis721 Blk BT"
musica_menu_inicial = "musica/menu_inicial.mp3"
fondo_menu_principal = "imagenes/fondo/menu_principal.png"
fondo_nivel_1 = "imagenes/fondo/fondo_1.png"

juego = Juego(tamaño_pantalla, FPS, titulo, icono, fondo_nivel_1, fuente,musica_menu_inicial)
juego.init()


