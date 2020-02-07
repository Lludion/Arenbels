from collections import defaultdict
from arenbels.game.tools.parse import grid_to_world

class World:

    def __init__(self):
        self.grid = [["" for _ in range(20)]for _ in range(20)]
        self.regions = []

    def from_grid(self,filename):
        self.l,self.h,self.grid = grid_to_world(filename)

    def get_regions(self):
        return regions

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