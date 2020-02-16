import pygame
import json
from shutil import copy2
from arenbels.display.camera import Camera
from arenbels.display.engine import Vector
from arenbels.tools import create_img
from arenbels.display.tools import blitpix
class Displayer:

    def __init__(self,redirect=False):
        self.options = {}
        self._window = None
        self.world = None

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
                self.options["DISPLAYSIZE_Y"] = min(height,self.options["DISPLAYSIZE_Y"])
                self.options["DISPLAYSIZE_X"] = min(width,self.options["DISPLAYSIZE_Y"])
                with open("arenbels/data/json/options.json","w") as f:
                    f.write(json.dumps(self.options))

        pygame.display.set_caption("Arenbels")
        pygame.display.set_icon(pygame.image.load("arenbels/data/img/icon.ico"))
        self._window = pygame.display.set_mode((self.options["DISPLAYSIZE_X"], self.options["DISPLAYSIZE_Y"]),self.options["modeECRAN"])#1920*1080 for instance
        self._window.set_alpha(None) #To speed things up


    def init_images(self):
        """loads all images into self.dict_img, blits the first background"""
        #Images
        with open("arenbels/data/json/img.json", "r") as read_file:
            self.dict_img = json.load(read_file,object_hook=create_img)
        #self._window.blit(self.dict_img["img_background"],(0,0))
        self.flip()

    def close(self):
        if pygame.display.get_init():
            self._window = None
            pygame.display.quit()
            pygame.quit()
        else:
            self._window = None

    def reopen(self):
        """ To reopen the window after a self.close() """
        self._window = pygame.display.set_mode((self.options["DISPLAYSIZE_X"], self.options["DISPLAYSIZE_Y"]),self.options["modeECRAN"])#1920*1080 for instance

    def link_world(self,w):
        """ loads the world """
        self.world = w

    def display_world(self):
        for p in self.world.grid:
            blitpix(self,p)
        self.flip()

    def init_camera(self):
        self.cam = Camera()
        self.cam.set_dimension(Vector(1000,1000))
        self.cam.set_win(self._window)
        self.cam.link_world(self.world)

    def flip(self):
        pygame.display.flip()

