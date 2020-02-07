from collections import defaultdict

class World:

    def __init__(self):
        self.grid = [["" for _ in range(20)]for _ in range(20)]
        self.regions = []


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