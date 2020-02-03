
class Region:

    def __init__(self,name="RegionName",game=None):
        self.name = name
        self.game = game
        self.seasonBonus = 0
        self.winterBonus = -30
        self.springBonus = 0
        self.summerBonus = 30
        self.autumnBonus = 50

    def set_seasonBonus(self,season):
        if season == 0:
            self.seasonBonus = self.springBonus
        elif season == 1:
            self.seasonBonus = self.summerBonus
        elif season == 2:
            self.seasonBonus = self.autumnBonus
        elif season == 3:
            self.seasonBonus = self.winterBonus
