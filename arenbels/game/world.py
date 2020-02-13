
from arenbels.game.tools.parse import grid_to_world
from arenbels.debug import logging
from arenbels.game.region import Region,Sea

class World:

    def __init__(self):
        self.grid = []
        self.regions = []
        self.game = None

    def from_grid(self,filename):
        self.l,self.h,self.grid = grid_to_world(filename)
        self.regions_from_grid()

    def in_regions(self,name):
        for reg in self.regions:
            if reg.name == name:
                return reg
        return None

    def regions_from_grid(self):
        for line in self.grid:
            for p in line:
                (type,name) = p.region
                reg = self.in_regions(name)
                if reg is None:
                    if type == "sea":
                        newreg = Sea(name)
                    elif type == "reg":
                        newreg = Region(name)
                    else:
                        logging.warning("Unknown region type.")
                        newreg = Region(name)
                    self.add_region(newreg)
                    p.region = newreg
                else:
                    p.region = reg

    def get_regions(self):
        return self.regions

    def add_region(self,region):
        """ Adds one region to the World """
        region.game = self.game
        if region not in self.regions:
            self.regions.append(region)

    def add_regions(self,*args):
        """ Adds the regions in argument """
        for region in args:
            if type(region) == type([]):
                for r in region:
                    self.add_region(r)
            else:
                self.add_region(region)
