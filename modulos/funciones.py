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

