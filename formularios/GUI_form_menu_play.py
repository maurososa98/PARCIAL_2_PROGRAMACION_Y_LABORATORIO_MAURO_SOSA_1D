import pygame
from pygame.locals import *

from formularios.UI.GUI_button_image import *
from formularios.UI.GUI_form import *
from formularios.UI.GUI_label import *
from formularios.UI.GUI_button import *
from formularios.UI.GUI_slider import *
from formularios.UI.GUI_textbox import *
from formularios.GUI_form_menu_score import *

class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, pressed_keys, path_image, active = True):
        super().__init__(screen, x,y,w,h,color_background,color_border,active)
        self.teclas_presionadas = pressed_keys
        self.imagen_fondo = path_image
        aux_image = pygame.image.load(self.imagen_fondo)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image
        self.lista_widgets = []
        self.presiono_boton = True
        self.seleccion_nivel = None

        self.boton_home = Button_Image(screen = self._slave, master_x = x, master_y = y, x = w -70, y = h -60, w = 40, h = 40, path_image= "formularios\Recursos\home.png", onclick= self.btn_home_click, onclick_param="")
        
        self.label_nivel_1 = Label(screen=self._slave,x=100,y=80,w=300,h=70,text = "NIVEL 1",font="Verdana",font_size=35,font_color=(255,255,255),path_image=r"formularios\Recursos\Table.png")
        self.boton_nivel_1 = Button_Image(screen = self._slave, master_x = x, master_y = y, x=100, y=80, w=300, h=70, path_image= r"formularios\Recursos\bar.png", onclick= self.entrar_nivel, onclick_param="1")

        self.label_nivel_2 = Label(screen=self._slave,x=100,y=160,w=300,h=70,text = "NIVEL 2",font="Verdana",font_size=35,font_color=(255,255,255),path_image=r"formularios\Recursos\Table.png")
        self.boton_nivel_2 = Button_Image(screen = self._slave, master_x = x, master_y = y, x=100, y=160, w=300, h=70, path_image= r"formularios\Recursos\bar.png", onclick= self.entrar_nivel, onclick_param="2")

        self.label_nivel_3 = Label(screen=self._slave,x=100,y=240,w=300,h=70,text = "NIVEL 3",font="Verdana",font_size=35,font_color=(255,255,255),path_image=r"formularios\Recursos\Table.png")
        self.boton_nivel_3 = Button_Image(screen = self._slave, master_x = x, master_y = y, x=100, y=240, w=300, h=70, path_image= r"formularios\Recursos\bar.png", onclick= self.entrar_nivel, onclick_param="3")

        self.lista_widgets.append(self.boton_home)
        self.lista_widgets.append(self.label_nivel_1)
        self.lista_widgets.append(self.boton_nivel_1)
        
        self.lista_widgets.append(self.label_nivel_2)
        self.lista_widgets.append(self.boton_nivel_2)
        
        self.lista_widgets.append(self.label_nivel_3)
        self.lista_widgets.append(self.boton_nivel_3)
        self.lista_widgets.append(
            Label(screen=self._slave,
                  x=40,y=10,w=self._w-80,
                  h=35,text = "NIVELES",
                  font="Verdana",
                  font_size=27,font_color=(255,255,255),path_image=r"formularios\Recursos\bar.png"))

    def entrar_nivel(self, numero_nivel):
        self.seleccion_nivel = numero_nivel

    def nivel_elegido(self):
        return self.seleccion_nivel

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
        return self.presiono_boton

