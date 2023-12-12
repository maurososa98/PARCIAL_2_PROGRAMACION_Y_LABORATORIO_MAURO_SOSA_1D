import pygame
from pygame.locals import *
from formularios.UI.GUI_button_image import *
from formularios.UI.GUI_form import *
from formularios.UI.GUI_label import *
from formularios.UI.GUI_button import *
from formularios.UI.GUI_slider import *
from formularios.UI.GUI_textbox import *
from formularios.GUI_form_menu_score import *
from formularios.GUI_form_configuracion import *
from formularios.GUI_form_menu_play import FormMenuPlay

class FormInicio(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, path_image, musica, active = True):
        super().__init__(screen, x,y,w,h,color_background,color_border,active)
        self.imagen_fondo = path_image
        aux_image = pygame.image.load(self.imagen_fondo)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image
        self.lista_widgets = []

        self.musica = musica
        self.pressed_keys = None
        
        pygame.mixer.init()
        pygame.mixer.music.load(musica)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        
        self.form_comenzar_juego = None

        self.btn_configuracion = Button_Image(self._slave, x, y,  810, 20, 50, 50, "formularios\Recursos\configuracion.png", self.btn_configuracion_click, "")

        self.btn_comenzar_juego = Button_Image(self._slave, x, y,  364, 300, 150, 112, "formularios\Recursos\play.png", self.btn_comenzar_juego_click, "")

        self.lista_widgets.append(self.btn_configuracion)
        self.lista_widgets.append(self.btn_comenzar_juego)

    def btn_home_click(self,parametro):
        self.presiono_boton = False
        self.end_dialog()

    def render(self):
        aux_image = pygame.image.load(self.imagen_fondo)
        aux_image = pygame.transform.scale(aux_image,(self._w , self._h))
        self._slave.blit(aux_image,(0,0))

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_play_click(self, param):
        if self.flag_play:
           pygame.mixer.music.pause()
           self.btn_play._color_background = "red"
           self.btn_play.set_text("Play")
        else:
           pygame.mixer.music.unpause()
           self.btn_play._color_background = "red"
           self.btn_play.set_text("Pause")
        self.flag_play = not self.flag_play

    def btn_configuracion_click(self, param):
       self.form_configuracion = FormConfiguracion(self._master, 190, 25, 500, 350, "blue", "black", "formularios\Recursos\Window.png", self.musica)
       self.show_dialog(self.form_configuracion)

    def btn_comenzar_juego_click(self, param):
       self.form_comenzar_juego = FormMenuPlay(self._master, 190, 25, 500, 350, "blue", "black", self.pressed_keys, active=True,  path_image = "formularios\Recursos\Window.png")
       self.show_dialog(self.form_comenzar_juego)

    def nivel_seleccionado(self):
        if self.form_comenzar_juego != None:
            return self.form_comenzar_juego.nivel_elegido()






