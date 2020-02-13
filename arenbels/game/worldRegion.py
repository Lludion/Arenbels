from collections import defaultdict

class WorldRegion:

    def __init__(self,name="WorldRegion"):
        """ A region on the map."""

        #set of coordinates
        self.coordinates = {}
        self.pop = 0
        self.happiness = defaultdict(int)
        self.cities = []
        self.sea = False
        self.name = name

    def set_pop(self):
        self.pop = 0
        for city in self.cities:
            self.pop += city.pop
