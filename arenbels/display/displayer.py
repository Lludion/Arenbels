import pygame
import json
from shutil import copy2

class Displayer:

    def __init__(self,redirect=False):
        self.options = {}
        self._window = None
        if redirect: self.redirect()
        self.init_window()

    def load_options(self):
        """ Initializes self.options """
        try:
            with open("arenbels/data/json/options.json","r") as file:
                self.options = json.load(file)
                #self.options["modeECRAN"]  = 0 ou FULLSCREEN

            #to test if new options have been added (by a push) to default_options
            with open("arenbels/data/json/default_options.json","r") as file:
                opt = json.load(file)
            if len(self.options) < len(opt):
                self.options = opt

        except FileNotFoundError:
            with open("arenbels/data/json/default_options.json","r") as file:
                self.options = json.load(file)
            copy2("arenbels/data/json/default_options.json","arenbels/data/json/options.json")

    def redirect(self):
        #Redirecting stdout
        from sys import stdout as sysout
        sysout = open('arenbels/doc/log.log', 'w')

    def init_window(self):
        """
        initializes a window, pygame graphics, and options
        returns the display window
        """
        #Display
        pygame.init()
        self.load_options()


        #FR: Cas de la trop faible résolution de l'écran
        #EN: If the screen is too small
        i = pygame.display.Info()
        width = i.current_w
        height = i.current_h
        if width < self.options["DISPLAYSIZE_X"] or height < self.options["DISPLAYSIZE_Y"]:
                self.options["DISPLAYSIZE_Y"] = height
                self.options["DISPLAYSIZE_X"] = width
                with open("arenbels/data/json/options.json","w") as f:
                    f.write(json.dumps(self.options))

        pygame.display.set_caption("Arenbels")
        pygame.display.set_icon(pygame.image.load("arenbels/data/img/icon.ico"))
        self._window = pygame.display.set_mode((self.options["DISPLAYSIZE_X"], self.options["DISPLAYSIZE_Y"]),self.options["modeECRAN"])#1920*1080 for instance
        self._window.set_alpha(None) #To speed things up

    def close(self):
        if pygame.display.get_init():
            self._window = None
            pygame.display.quit()
            pygame.quit()
        else:
            self._window = None

