from math import ceil
from arenbels.game.tools.increase import increase
import numpy as np

class State:

    def __init__(self,name="StateName"):
        self.leaderTitle = "LeaderTitleM"
        self.leaderName = "LeaderName"
        self.name = name

        #List of the Cities controlled by the State
        self.cities = []

        #Money the State currently possesses.
        self.treasure = 1000
        #Money it had last turn
        self.old_t = 1000

        #Base Trade objective. Might depend on the type of the state.
        self.baseTradeOBJ = 1000

        #Current Trade objective. Depends on the buildings in your cities.
        self.tradeOBJ = 1000

        #Current trade value. An indicator of the economic wealth of the country
        self.trade = 1000

        #Current trade imposition value
        self.tradeImposition = 1

        #values used for explain where does the money come from
        #money from Trade
        self.moneyFromTrade = 0

        #Global bonus value for health in cities of this state
        self.globHealth = 0

        #History
        self.history = []


    def __repr__(self):
        txt = """
        State Name : %s
        Treasure: %s
        Cities : %s
        Trade : %d
        TradeOBJ : %d
        MoneyFromTrade : %d
        globhealth :%d
        """ % (self.name,str(self.treasure),str(self.cities),self.trade,self.tradeOBJ,self.moneyFromTrade,self.globHealth)
        return txt

    def send_info(self):
        """ returns:
        Treasure
        Trade
        GlobHealth
        Gain"""
        return (self.treasure,self.trade,self.globHealth,self.gain())

    def get_history(self):
        return np.array(self.history)

    def gain(self):
        return self.treasure - self.old_t

    def add_city(self,city):
        city.owner = self
        if city not in self.cities:
            self.cities.append(city)

    def add_cities(self,*args):
        """ Adds the cities in argument """
        for city in args:
            if type(city) == type([]):
                for c in city:
                    self.add_city(c)
            else:
                self.add_city(city)

    def renew_tradeOBJ(self):
        #self.tradeOBJ = ceil(self.baseTradeOBJ * 0.1 + self.tradeOBJ * 0.9)
        pass

    def renew_globHealth(self):
        self.oldGlobHealth = self.globHealth
        self.globHealth = 0

    def update_globHealth(self):
        self.globHealth = ceil((self.globHealth * 9 - self.oldGlobHealth) / 10)

    def end_turn(self,game):
        self.old_t = self.treasure
        self.renew_tradeOBJ()
        self.renew_globHealth()

        for city in self.cities:
            city.end_turn(self,game)

        for region in game.world.regions:
            ok = False
            for city in region.cities:
                if city.owner is self:
                    ok = True
                    region.happiness[self] += city.happy
            if ok:
                city.region.happiness[self] += city.region.seasonHappy

        for city in self.cities:
            city.add_money(self)

        self.trade += increase(self.trade,self.tradeOBJ,game.tradeChangeSpeed)
        self.trade = max(self.trade,0)

        self.update_globHealth()

        self.moneyFromTrade = ceil(self.trade*(self.tradeImposition)/100)
        self.treasure += self.moneyFromTrade

        self.history.append(self.send_info())