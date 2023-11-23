import pygame
from modulos.objetos_en_pantalla.clase_nivel import *
from modulos.objetos_en_pantalla.clase_objeto  import *

class Bala(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"imagenes\trampa\trampa_disparo.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class CreadorBalas():
    def __init__(self):
        self.ultimo_disparo = pygame.time.get_ticks()
        self.sonido_disparo = pygame.mixer.Sound(("musica/trampa_dispara.mp3"))
        self.bala = None
        self.pantalla = None
        self.velocidad = 5

    def crear_bala(self, posicion, pantalla, grupo_bala):
        self.pantalla = pantalla
        calculo = pygame.time.get_ticks()
        if calculo - self.ultimo_disparo > 1500 and len(pygame.sprite.Group.sprites(grupo_bala)) < 1:
            self.bala = Bala(posicion[0],posicion[1])
            grupo_bala.add(self.bala)
            self.sonido_disparo.play()
            self.sonido_disparo.set_volume(0.01)
            self.ultimo_disparo = calculo

    def animar(self, grupo_bala, arriba:bool=True, derecha:bool=False):
        grupo_bala.update(self.pantalla)
        grupo_bala.draw(self.pantalla)
        if arriba:
            self.bala.rect.y -= self.velocidad
        if derecha:
            self.bala.rect.left += self.velocidad
            self.bala.image = pygame.transform.rotate(pygame.image.load(r"imagenes\trampa\trampa_disparo.png"), 270)
        lista_balas = pygame.sprite.Group.sprites(grupo_bala)
        for i in range(len(lista_balas)):
            if (lista_balas[i].rect.y < 0 or lista_balas[i].rect.x > 880):
                pygame.sprite.Sprite.kill(lista_balas[i])
    


