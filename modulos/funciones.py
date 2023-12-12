import pygame
import re

def lista_imagenes(ruta:str, cantidad_imagenes:int, escala:tuple, voltear:bool=False)-> list:
    """
    La funcion se encarga de tomar la ruta de un solo sprite de una serie de sprites numericos
    y guarda las superficies en una lista.
    Args:
        ruta (str): Ruta del sprite.
        cantidad_imagenes (int): Cantidad de sprites.
        escala (tuple): Tupla que represente la escala de los sprites.
        voltear (bool, optional): Booleano que indique si se requiere voltear el sprite. Por defecto False.
    Returns:
        list: Retorna la lista de superficies.
    """
    lista_imagenes = []
    for i in range(0,cantidad_imagenes):
        ruta_imagen = re.sub("[0-9.]+", f"{i}.", ruta)
        imagen = pygame.image.load(ruta_imagen)
        imagen = pygame.transform.scale(imagen,escala)
        if voltear:
            imagen = pygame.transform.flip(imagen,True,False)
        lista_imagenes.append(imagen)
    return lista_imagenes

lista_imagenes_vida = lista_imagenes("imagenes/vida/0.png",12,(22,26))
grupo_vidas_nivel_1 = pygame.sprite.Group()
grupo_vidas_nivel_2 = pygame.sprite.Group()
grupo_vidas_nivel_3 = pygame.sprite.Group()

lista_imagenes_punto = lista_imagenes("imagenes/punto/0.png",16,(10,16))
grupo_puntos_nivel_1 = pygame.sprite.Group()
grupo_puntos_nivel_2 = pygame.sprite.Group()
grupo_puntos_nivel_3 = pygame.sprite.Group()

lista_imagenes_salida = lista_imagenes("imagenes/salida/0.png",12,(50,50))
grupo_salida_nivel_1 = pygame.sprite.Group()
grupo_salida_nivel_2 = pygame.sprite.Group()
grupo_salida_nivel_3 = pygame.sprite.Group()

escala_jefe = (72,107)
lista_imagenes_jefe_venom_derecha = lista_imagenes("imagenes/venom/camina/0.png",7,escala_jefe,True)
lista_imagenes_jefe_venom_izquierda = lista_imagenes("imagenes/venom/camina/0.png",7,escala_jefe)
grupo_jefe = pygame.sprite.Group()
lista_jefe = []

escala_enenigo = (65,46)
lista_imagenes_enemigo_venom_derecha = lista_imagenes("imagenes/enemigo_venom/0.png",28,escala_enenigo)
lista_imagenes_enemigo_venom_izquierda = lista_imagenes("imagenes/enemigo_venom/0.png",28,escala_enenigo,True)
grupo_enemigos_nivel_1 = pygame.sprite.Group()
grupo_enemigos_nivel_2 = pygame.sprite.Group()
grupo_enemigos_nivel_3 = pygame.sprite.Group()

# HEROE -----------------------------------------------------
escala_heroe = (38,50)
lista_camina_derecha = lista_imagenes("imagenes/spiderman/camina/0.png",11,escala_heroe)
lista_camina_izquierda = lista_imagenes("imagenes/spiderman/camina/0.png",11,escala_heroe,True)

lista_camina_derecha_poder = lista_imagenes("imagenes/spiderman_poder/camina/0.png",8,escala_heroe)
lista_camina_izquierda_poder = lista_imagenes("imagenes/spiderman_poder/camina/0.png",8,escala_heroe,True)

# MUSICA -----------------------------------------------------
musica_menu_inicial = "musica/menu_inicial.mp3"
musica_menu_pausa = "musica/menu_pausa.mp3"
musica_nivel_1 = "musica/nivel_1.mp3"
musica_nivel_2 = "musica/nivel_2.mp3"
musica_nivel_3 = "musica/nivel_3.mp3"


lista_imagenes_salida = lista_imagenes("imagenes/salida/0.png", 12, (45,45))

fondo_menu_principal = "imagenes/fondo/menu_principal.png"
fondo_menu_pausa = "imagenes/fondo/menu_pausa.png"
fondo_nivel_1 = "imagenes/fondo/fondo_1.png"
fondo_nivel_2 = "imagenes/fondo/fondo_2.png"
fondo_nivel_3 = "imagenes/fondo/fondo_3.png"



