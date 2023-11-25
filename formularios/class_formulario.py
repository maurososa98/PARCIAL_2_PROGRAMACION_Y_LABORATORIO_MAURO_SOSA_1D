import pygame
import sys
class Formulario:
    def __init__(self, imagen, tamaño, posicion,texto):
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, tamaño)
        self.posicion = posicion
        fuente = pygame.font.SysFont("Ravie",20)
        self.texto_escrito = texto
        self.texto = fuente.render(texto, True, "White")
        self.title_rect = self.texto.get_rect(center=(self.posicion[0]+200,self.posicion[1]+70))

        fuente_boton = pygame.font.SysFont("Arial", 20)
        self.boton_deslizante = BotonDeslizante((posicion[0]+30, posicion[1]+150), self.imagen.get_width()-80, "white", "red")
        self.boton = Boton((posicion[0]+30, posicion[1]+100), (100, 30), "Pausa", r"formularios\Recursos\Table.png", fuente_boton)
        self.btn_volver = Boton((posicion[0]+300, posicion[1]+200), (50, 50), "", r"formularios\Recursos\Menu_BTN.png", fuente_boton)
        self.botonMenuPrincipal = Boton((posicion[0]+30, posicion[1]+200), (150, 30), "Menu Principal", r"formularios\Recursos\home.png", fuente_boton)
        self.btn_reintentar = Boton((posicion[0]+30, posicion[1]+150), (200, 40), "Reintentar", r"formularios\Recursos\Table.png", fuente_boton)
        self.btn_siguiente_nivel = Boton((posicion[0]+30, posicion[1]+100), (200, 40), "Sig. Nivel", r"formularios\Recursos\Table.png", fuente_boton)

        border_width = 2
        self.border_surface = fuente.render(texto, True, "black")
        self.border_rects = [
            self.title_rect.move(-border_width, -border_width),
            self.title_rect.move(-border_width, border_width),
            self.title_rect.move(border_width, -border_width),
            self.title_rect.move(border_width, border_width)
        ]
            
        

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.posicion)
        for border_rect in self.border_rects:
            pantalla.blit(self.border_surface, border_rect)
        pantalla.blit(self.texto,self.title_rect)
        if self.texto_escrito == "Pausa":
            self.boton.dibujar(pantalla)
            self.botonMenuPrincipal.dibujar(pantalla)
            self.boton_deslizante.dibujar(pantalla)
            self.btn_volver.dibujar(pantalla)
        elif self.texto_escrito == "Perdiste":
            self.botonMenuPrincipal.dibujar(pantalla)
            self.btn_reintentar.dibujar(pantalla)
        elif self.texto_escrito == "Ganaste":
            self.botonMenuPrincipal.dibujar(pantalla)
            self.btn_reintentar.dibujar(pantalla)
            self.btn_siguiente_nivel.dibujar(pantalla)
        else:
            self.boton.dibujar(pantalla)
            self.btn_volver.dibujar(pantalla)
            self.boton_deslizante.dibujar(pantalla)


    def ejecutar(self,pantalla):
        self.flag = True
        while self.flag:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.texto_escrito == "Pausa":
                        if self.btn_volver.rectangulo.collidepoint(pygame.mouse.get_pos()):
                            self.flag = False
                        if self.botonMenuPrincipal.rectangulo.collidepoint(pygame.mouse.get_pos()):
                            self.flag = False
                            return True
                        if self.boton.rectangulo.collidepoint(pygame.mouse.get_pos()):
                            self.boton.cambiar_texto()
                        if pygame.mouse.get_pressed()[0]:
                            x, y = evento.pos
                            if self.boton_deslizante.posicion[0] <= x <= self.boton_deslizante.posicion[0] + self.boton_deslizante.longitud and self.boton_deslizante.posicion[1] - 15 <= y <= self.boton_deslizante.posicion[1] + 5:
                                self.boton_deslizante.mover_boton = True
                    elif self.texto_escrito == "Perdiste":
                        if self.btn_reintentar.rectangulo.collidepoint(pygame.mouse.get_pos()):
                            self.flag = False
                            return False
                        if self.botonMenuPrincipal.rectangulo.collidepoint(pygame.mouse.get_pos()):
                            self.flag = False
                            return True
                    elif self.texto_escrito == "Ganaste":
                        if self.btn_reintentar.rectangulo.collidepoint(pygame.mouse.get_pos()):
                            self.flag = False
                            return False
                        if self.botonMenuPrincipal.rectangulo.collidepoint(pygame.mouse.get_pos()):
                            self.flag = False
                            return True
                        if self.btn_siguiente_nivel.rectangulo.collidepoint(pygame.mouse.get_pos()):
                            self.flag = False
                            return "Siguiente"
                    else:
                        if self.btn_volver.rectangulo.collidepoint(pygame.mouse.get_pos()):
                            self.flag = False
                        if self.boton.rectangulo.collidepoint(pygame.mouse.get_pos()):
                            self.boton.cambiar_texto()
                        if pygame.mouse.get_pressed()[0]:
                            x, y = evento.pos
                            if self.boton_deslizante.posicion[0] <= x <= self.boton_deslizante.posicion[0] + self.boton_deslizante.longitud and self.boton_deslizante.posicion[1] - 15 <= y <= self.boton_deslizante.posicion[1] + 5:
                                self.boton_deslizante.mover_boton = True
                elif evento.type == pygame.MOUSEBUTTONUP:
                    self.boton_deslizante.mover_boton = False
                elif evento.type == pygame.MOUSEMOTION:
                    if self.boton_deslizante.mover_boton:
                        x = evento.pos[0] - self.boton_deslizante.posicion[0]
                        volumen = max(0, min(x / self.boton_deslizante.longitud, 1))
                        self.boton_deslizante.musica.set_volume(volumen)
                self.boton_deslizante.manejar_eventos(pygame.event.get())
            self.dibujar(pantalla)
            pygame.display.update()

class Boton:
    def __init__(self, posicion, tamaño, texto, imagen, fuente):
        self.posicion = posicion
        self.tamaño = tamaño
        self.texto = texto
        self.imagen_normal = pygame.image.load(imagen)
        self.imagen_normal = pygame.transform.scale(self.imagen_normal, tamaño)
        self.imagen_hover = pygame.transform.scale(self.imagen_normal, (tamaño[0]+10, tamaño[1]+10))
        self.rectangulo = pygame.Rect(self.posicion, self.tamaño)
        self.fuente = fuente
        self.musica = pygame.mixer.music
        self.clickeado = False

    def dibujar(self, pantalla):
        if self.rectangulo.collidepoint(pygame.mouse.get_pos()):
            pantalla.blit(self.imagen_hover, self.posicion)
            self.fuente = pygame.font.SysFont("Arial", 25)
        else:
            pantalla.blit(self.imagen_normal, self.posicion)
            self.fuente = pygame.font.SysFont("Arial", 20)
        texto_renderizado = self.fuente.render(self.texto, True, "black")
        texto_rect = texto_renderizado.get_rect(center=self.rectangulo.center)
        if texto_rect.width > self.tamaño[0]:
            texto_renderizado = pygame.transform.scale(texto_renderizado, (self.tamaño[0], texto_rect.height))
            texto_rect = texto_renderizado.get_rect(center=self.rectangulo.center)
        pantalla.blit(texto_renderizado, texto_rect)


    def cambiar_texto(self):
        if self.texto != "":
            if self.texto == "Pausa":
                self.texto = "Reproducir"
                self.fuente = pygame.font.SysFont("Arial", 15)
                pygame.mixer.music.pause()
            else:
                self.texto = "Pausa"
                self.fuente = pygame.font.SysFont("Arial", 20)
                pygame.mixer.music.unpause()
            
            
class BotonDeslizante:
    def __init__(self, posicion, longitud, color_boton, color_barra):
        self.posicion = posicion
        self.longitud = longitud
        self.color_boton = color_boton
        self.color_barra = color_barra
        self.musica = pygame.mixer.music
        self.mover_boton = False

    def dibujar(self, pantalla):
        # Dibujar la barra
        pygame.draw.rect(pantalla, self.color_barra, (self.posicion[0], self.posicion[1], self.longitud, 10))

        # Calcular la posición del botón en función del volumen y dibujarlo
        volumen = self.musica.get_volume()
        x = int(self.posicion[0] + self.longitud * volumen)
        y = int(self.posicion[1] - 5)
        pygame.draw.circle(pantalla, self.color_boton, (x, y), 10)

    def manejar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x, y = evento.pos
                    if self.posicion[0] <= x <= self.posicion[0] + self.longitud and self.posicion[1] - 15 <= y <= self.posicion[1] + 5:
                        self.mover_boton = True
            elif evento.type == pygame.MOUSEBUTTONUP:
                self.mover_boton = False
            elif evento.type == pygame.MOUSEMOTION:
                if self.mover_boton:
                    x = evento.pos[0] - self.posicion[0]
                    volumen = max(0, min(x / self.longitud, 1))
                    self.musica.set_volume(volumen)
        
pygame.init()
# Configuración de la fuente
pygame.font.init()
fuente_boton = pygame.font.SysFont("Arial", 20)
pygame.mixer.music.load("musica/menu_pausa.mp3")

# Crear un formulario con un cuadro utilizando una imagen, un tamaño de escalado y una posición
formulario = Formulario(r"imagenes/fondo/menu_pausa.png", (400, 300), (200, 150), "FORMULARIO")

# Crear el botón deslizante


# Reproducir la música en bucle
pygame.mixer.music.play(-1)

# Ejecutar el formulario
formulario.ejecutar()