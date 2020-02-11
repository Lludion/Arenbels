from collections import defaultdict
from arenbels.game.tools.parse import grid_to_world

class World:

    def __init__(self):
        self.grid = []
        self.regions = []

    def from_grid(self,filename):
        self.l,self.h,self.grid = grid_to_world(filename)

    def get_regions(self):
        return self.regions

    def add_region(self,region):
        """ Adds one region to the World """
        region.game = self
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

class WorldRegion:

    def __init__(self):
        """ A region on the map."""

        #set of coordinates
        self.coordinates = {}
        self.pop = 0
        self.happiness = defaultdict(int)
        self.cities = []

    def set_pop(self):
        self.pop = 0
        for city in self.cities:
            self.pop += city.pop