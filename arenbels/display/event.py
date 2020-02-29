import pygame
from arenbels.display import Displayer
from arenbels.display.tools import xyinbounds

class EventHandler(Displayer):

    def __init__(self):
        super().__init__()

    def catchWm(self):
        """ catches events on the worldMap """
        grid = self.world.grid
        pygame.time.Clock().tick(self.options["FPS"])
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.stop()
                if event.key == pygame.K_s:
                    if keys[pygame.K_RCTRL]:
                        print("Save will be implemented!")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if event.button == 1:
                    for p in grid:
                        if xyinbounds(mx,my,p):
                            print(mx,my,p.x*p.size,p.y*p.size,p.region.name)
    def stop(self):
        self.cont = False
        self.close()

    def main_loop(self):
        self.cont = True
        while self.cont:
            self.catchWm()