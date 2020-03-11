
from arenbels.game.worldRegion import WorldRegion

class Region(WorldRegion):

    def __init__(self,name="RegionName",game=None):
        super().__init__(name)
        self.name = name
        self.game = game

        #Bonus to agrarian wealth
        self.seasonBonus = 0
        self.winterBonus = -30
        self.springBonus = 0
        self.summerBonus = 30
        self.autumnBonus = 50

        self.seasonHappy = 0
        self.winterHappy = -2
        self.springHappy = 1
        self.summerHappy = 2
        self.autumnHappy = -1

    def set_seasonBonus(self,season):
        if season == 0:
            self.seasonBonus = self.springBonus
            self.seasonHappy = self.springHappy
        elif season == 1:
            self.seasonBonus = self.summerBonus
            self.seasonHappy = self.summerHappy
        elif season == 2:
            self.seasonBonus = self.autumnBonus
            self.seasonHappy = self.autumnHappy
        elif season == 3:
            self.seasonBonus = self.winterBonus
            self.seasonHappy = self.winterHappy

    def ruralSum(self):
        return self.springBonus + self.winterBonus + self.autumnBonus + self.summerBonus

    def __repr__(self):
        return self.name

class Sea(WorldRegion):

    def __init__(self,name="SeaName",game=None):
        super().__init__(name)
        self.sea = True
        self.name = name
        self.game = game

        #Bonus to maritime wealth
        self.seasonBonus = 0
        self.winterBonus = -50
        self.springBonus = 0
        self.summerBonus = 0
        self.autumnBonus = 0

        self.seasonHappy = 0
        self.winterHappy = 0
        self.springHappy = 0
        self.summerHappy = 0
        self.autumnHappy = 0

    def __repr__(self):
        return self.name


class Desertic(Region):
    """ Very hot summers. Good food production all year round."""

    def __init__(self,name="DeserticName",game=None):
        super().__init__(name,game)

        #Bonus to agrarian wealth
        self.winterBonus = 30
        self.springBonus = 10
        self.summerBonus = 30
        self.autumnBonus = 30

        self.winterHappy = 1
        self.springHappy = 1
        self.summerHappy = -3
        self.autumnHappy = 0

class Continental(Region):
    """ Sweltering summers, freezing winters, but good food prodution overall"""

    def __init__(self,name="ContinentalName",game=None):
        super().__init__(name,game)

        #Bonus to agrarian wealth
        self.winterBonus = -50
        self.springBonus = 10
        self.summerBonus = 30
        self.autumnBonus = 60

        self.winterHappy = -2
        self.springHappy = 2
        self.summerHappy = -1
        self.autumnHappy = 1

class Oceanic(Region):
    """ Not many seasonal changes. Mild winters & summers """

    def __init__(self,name="OceanicName",game=None):
        super().__init__(name,game)

        #Bonus to agrarian wealth
        self.winterBonus = -10
        self.springBonus = 10
        self.summerBonus = 20
        self.autumnBonus = 30

        self.winterHappy = -1
        self.springHappy = 0
        self.summerHappy = 1
        self.autumnHappy = 0

class Icy(Region):
    """ Happiness bonuses, but heavy maluses to agriculture"""

    def __init__(self,name="IcyName",game=None):
        super().__init__(name,game)

        #Bonus to agrarian wealth
        self.winterBonus = -50
        self.springBonus = -50
        self.summerBonus = -20
        self.autumnBonus = -30

        self.winterHappy = 2
        self.springHappy = 1
        self.summerHappy = 1
        self.autumnHappy = 1

class Tundra(Region):
    """ Rough winter, bad springs, happy summer& autumn"""

    def __init__(self,name="TundraName",game=None):
        super().__init__(name,game)

        #Bonus to agrarian wealth
        self.winterBonus = -30
        self.springBonus = -20
        self.summerBonus = 30
        self.autumnBonus = 30

        self.winterHappy = -2
        self.springHappy = 0
        self.summerHappy = 1
        self.autumnHappy = 1
