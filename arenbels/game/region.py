
class Region:

    def __init__(self,name="RegionName",game=None):
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
