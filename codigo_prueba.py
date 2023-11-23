# lista_imagenes_vida = lista_imagenes("imagenes/vida/0.png",12,(22,26))
# grupo_vidas_nivel_1 = pygame.sprite.Group()
# grupo_vidas_nivel_2 = pygame.sprite.Group()
# grupo_vidas_nivel_3 = pygame.sprite.Group()

# lista_imagenes_punto = lista_imagenes("imagenes/punto/0.png",16,(10,16))
# grupo_puntos_nivel_1 = pygame.sprite.Group()
# grupo_puntos_nivel_2 = pygame.sprite.Group()
# grupo_puntos_nivel_3 = pygame.sprite.Group()

# escala_enenigo = (65,46)
# lista_imagenes_enemigo_venom_derecha = lista_imagenes("imagenes/enemigo_venom/0.png",28,escala_enenigo)
# lista_imagenes_enemigo_venom_izquierda = lista_imagenes("imagenes/enemigo_venom/0.png",28,escala_enenigo,True)
# grupo_enemigos_nivel_1 = pygame.sprite.Group()
# grupo_enemigos_nivel_2 = pygame.sprite.Group()
# grupo_enemigos_nivel_3 = pygame.sprite.Group()

# escala_jefe_1 = (72,107)
# escala_jefe_2 = (127,162)
# lista_imagenes_jefe_venom_derecha = lista_imagenes("imagenes/venom/camina/0.png",7,escala_jefe_1,True)
# lista_imagenes_jefe_venom_izquierda = lista_imagenes("imagenes/venom/camina/0.png",7,escala_jefe_1)
# grupo_jefe = pygame.sprite.Group()
# lista_jefe = []

# class Objeto(pygame.sprite.Sprite):
#     def __init__(self,x,y, lista_imagenes, refrescar_animacion):
#         pygame.sprite.Sprite.__init__(self)
#         self.lista_imagenes = lista_imagenes
#         self.indice = 0
#         self.contador = 0
        
#         self.image = self.lista_imagenes[self.indice]
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.refrescar_animacion = refrescar_animacion

#     def update(self):
#         self.animar()

#     def animar(self, salta=False, desplazamiento_y=0, velocidad=0):
#         self.contador += 1
#         refrescar = self.refrescar_animacion
#         if self.contador > refrescar:
#             self.contador = 0
#             self.indice += 1
#             if salta and (desplazamiento_y < 0 or desplazamiento_y > 0):
#                 imagen_salta = pygame.image.load("imagenes/venom/salta/4.png") 
#                 if velocidad < 0:
#                     self.image = pygame.transform.scale(imagen_salta,escala_jefe_1)
#                 elif velocidad > 0:
#                     imagen_escalada = pygame.transform.scale(imagen_salta,escala_jefe_1)
#                     self.image = pygame.transform.flip(imagen_escalada,True,False)
#             else:
#                 if self.indice >= len(self.lista_imagenes):
#                     self.indice = 0
#                 self.image = self.lista_imagenes[self.indice]

# class ItemPunto(Objeto):
#     def __init__(self, x, y, lista_imagenes, refrescar_animacion):
#         super().__init__(x, y, lista_imagenes, refrescar_animacion)

# class ItemVida(Objeto):
#     def __init__(self, x, y, lista_imagenes, refrescar_animacion):
#         super().__init__(x, y, lista_imagenes, refrescar_animacion)

# class Enemigo(Objeto):
#     def __init__(self, x, y, lista_imagenes, refrescar_animacion,cuanto_camina, lista_imagenes_izquierda, lista_imagenes_derecha, velocidad):
#         super().__init__(x, y, lista_imagenes, refrescar_animacion)
#         pygame.sprite.Sprite.__init__(self)
#         self.velocidad = velocidad
#         self.contador_pasos = 0
#         self.cuanto_camina = cuanto_camina
#         self.lista_imagenes_izquierda = lista_imagenes_izquierda
#         self.lista_imagenes_derecha = lista_imagenes_derecha

#     def update(self):
#         self.rect.x += self.velocidad
#         self.contador_pasos += 1
#         if self.velocidad < 0:
#             self.lista_imagenes = self.lista_imagenes_izquierda
#         elif self.velocidad > 0:
#             self.lista_imagenes = self.lista_imagenes_derecha
#         if abs(self.contador_pasos) > self.cuanto_camina:
#             self.velocidad *= -1
#             self.contador_pasos = 0
#         self.animar()

# class Jefe(Enemigo):
#     def __init__(self, x, y, lista_imagenes, refrescar_animacion, cuanto_camina, lista_imagenes_izquierda, lista_imagenes_derecha, velocidad):
#         super().__init__(x, y, lista_imagenes, refrescar_animacion, cuanto_camina, lista_imagenes_izquierda, lista_imagenes_derecha, velocidad)
#         self.ultimo_salto = pygame.time.get_ticks()
#         self.calculo = 0
        
#         self.width = self.image.get_width()
#         self.height = self.image.get_height()

#         self.desplazamiento_y = 0
#         self.contador_salto = 0

#         self.velocidad_salto = 0
#         self.esta_saltando = False
#         self.giro = False

#     def animar_salto(self, nivel):
#         self.desplazamiento_y = 0

#         self.contador_pasos += 1
#         if self.velocidad < 0:
#             self.lista_imagenes = lista_imagenes_jefe_venom_izquierda
#         elif self.velocidad > 0:
#             self.lista_imagenes = lista_imagenes_jefe_venom_derecha
#         if abs(self.contador_pasos) > self.cuanto_camina:
#             self.velocidad *= -1
#             self.contador_pasos = 0
#         self.desplazamiento_x = self.velocidad

#         # self.contador_salto +=1
#         # if self.contador_salto > 50 and self.esta_saltando == False:
#         #     self.contador_salto = 0
#         #     self.velocidad_salto = -16
#         #     self.esta_saltando = True

#         # Grabedad
#         self.velocidad_salto += 1
#         if self.velocidad_salto > 20:
#             self.velocidad_salto = 20
#         self.desplazamiento_y += self.velocidad_salto

#         for rectangulo_plataforma in nivel.lista_img_rect:
#             if rectangulo_plataforma[1].colliderect(self.rect.x + self.velocidad, self.rect.y, self.width, self.height):
#                 self.desplazamiento_x = 0

#             if rectangulo_plataforma[1].colliderect(self.rect.x, self.rect.y + self.desplazamiento_y, self.width, self.height):
#                 if self.velocidad_salto < 0: # SUBIENDO
#                     self.desplazamiento_y = rectangulo_plataforma[1].bottom - self.rect.top
#                     self.velocidad_salto = 0
#                 if self.velocidad_salto >= 0: # BAJANDO
#                     self.desplazamiento_y = rectangulo_plataforma[1].top - self.rect.bottom
#                     self.velocidad_salto = 0
#                     self.esta_saltando = False

#         if self.rect.left < 0:
#             self.rect.left = 0
#             self.desplazamiento_x = 0
#         if self.rect.right > 880:
#             self.rect.right = 880
#             self.desplazamiento_x = 0

#         self.rect.y += self.desplazamiento_y
#         self.rect.x += self.desplazamiento_x

#         self.animar(self.esta_saltando,self.desplazamiento_y,self.velocidad)
import pygame

class Bala(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"imagenes\trampa\trampa_disparo.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
bala_1 = Bala(0,0)
bala_2 = Bala(0,0)
bala_3 = Bala(0,0)
grupo_bala_1 = pygame.sprite.Group()

grupo_bala_1.add(bala_1)
grupo_bala_1.add(bala_2)
grupo_bala_1.add(bala_3)
print(pygame.sprite.Group.sprites(grupo_bala_1))