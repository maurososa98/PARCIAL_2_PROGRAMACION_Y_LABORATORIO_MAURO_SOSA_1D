from nivel  import *
from class_plataformas import *

class NivelDos(Nivel):
    def __init__(self, pantalla, personaje_principal, lista_plataformas, imagen_fondo):
        W = pantalla.get_width()
        H = pantalla.get_height()
        
        #FONDO
        fondo = pygame.image.load("")
        fondo = pygame.transform.scale(fondo, (W,H))
        
        #PERSONAJE
        posicion = (H/2 -300, 650)
        tamaño = (75, 85)
        
        #ANIMACIONES
        
        
        #PLATAFORMAS
        #Piso
        
        #Plataformas
        
        #Lista plataformas
        super().__init__(pantalla, personaje_principal, lista_plataformas, imagen_fondo)
        
        
        
        
        