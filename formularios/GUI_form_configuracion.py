import pygame
import re
from pygame.locals import *

from formularios.UI.GUI_button_image import *
from formularios.UI.GUI_form import *
from formularios.UI.GUI_label import *
from formularios.UI.GUI_button import *
from formularios.UI.GUI_slider import *
from formularios.UI.GUI_textbox import *
from formularios.GUI_form_menu_score import *

        
class FormConfiguracion(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, path_image,musica, active = True):
        super().__init__(screen, x,y,w,h,color_background,color_border,active)
        self.imagen_fondo = path_image
        aux_image = pygame.image.load(self.imagen_fondo)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image
        self.lista_widgets = []
        self.lista_puntajes = []
        
        
        pygame.mixer.init()
        self.flag_play = True
        self.volumen = 0.1
        self.presiono_boton = True

        self.btn_play = Button(self._slave, x, y, 270, 90, 100, 50, "red", "blue", self.btn_play_click, "hola", "Pause", "Verdana", 15, "white")
        
        self.slider_volumen = Slider(self._slave, x, y, 190, 188, 150, 15, self.volumen, "red", "white")
        
        porcentaje_volumen = f"{self.volumen * 100}%"
        self.label_volumen = Label(self._slave, 365, 170, 100, 50, porcentaje_volumen, "Comic Sans MS", 15, "white", "formularios\Recursos\Table.png")
        
        self.btn_tabla = Button_Image(self._slave, x, y,  370, 250, 50, 50, "formularios\Recursos\Menu_BTN.png", self.btn_tabla_click, "")

        #Crear boton home
        self.boton_home = Button_Image(screen = self._slave, master_x = x, master_y = y, x = w -70, y = h -60, w = 40, h = 40, path_image= "formularios\Recursos\home.png", onclick= self.btn_home_click, onclick_param="")

        self.lista_widgets.append(self.boton_home)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(
            Label(screen=self._slave,
                  x=40,y=10,w=self._w-80,
                  h=35,text = "Configuración",
                  font="Verdana",
                  font_size=27,font_color=(255,255,255),path_image=r"formularios\Recursos\bar.png"))
        self.lista_widgets.append(
            Label(screen=self._slave,
                  x=120,y=95,w=150,
                  h=35,text = "Música:",
                  font="Verdana",
                  font_size=27,font_color=(255,255,255),path_image=r"formularios\Recursos\bar.png"))
        self.lista_widgets.append(
            Label(screen=self._slave,
                  x=30,y=173,w=150,
                  h=35,text = "Volumen:",
                  font="Verdana",
                  font_size=27,font_color=(255,255,255),path_image=r"formularios\Recursos\bar.png"))
        self.lista_widgets.append(
            Label(screen=self._slave,
                  x=60,y=253,w=300,
                  h=35,text = "Ranking Puntuación:",
                  font="Verdana",
                  font_size=27,font_color=(255,255,255),path_image=r"formularios\Recursos\bar.png"))

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
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
        return self.presiono_boton

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

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

    def btn_tabla_click(self, param):
        try:
            with open("data/registro_partidas.csv","r") as archivo:
                for linea in archivo:
                    numero_str = linea.replace(r"\n","")
                    numero_int = int(numero_str)
                    self.lista_puntajes.append(numero_int)
            self.lista_puntajes = self.ordenar_de_mayor_a_menor(self.lista_puntajes)
        except PermissionError:
            print("ERROR, el archivo de registro de partidas se encuentra abierto.")
        except Exception as ex:
            print(f"ERROR, se produjo un error del tipo: {type(ex)}")

        diccionario = [{"Puesto": "1ª", "Score": self.lista_puntajes[0] },
                      {"Puesto": "2ª", "Score": self.lista_puntajes[1] },
                      {"Puesto": "3ª", "Score": self.lista_puntajes[2] }]
        nuevo_form = FormMenuScore(screen = self._master, x = 190, y = 25, w = 500, h = 550, color_border = "red", color_background = "green", active = True, path_image = "formularios\Recursos\Window.png", scoreboard = diccionario, margen_x = 20, margen_y = 100, espacio = 10)
       
        self.show_dialog(nuevo_form)
    
    def ordenar_de_mayor_a_menor(self, lista):
        return sorted(lista, reverse=True)


