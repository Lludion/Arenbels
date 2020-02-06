from math import ceil
from arenbels.game.tools.increase import increase
from arenbels.game.region import Region
import numpy as np
from arenbels.game.tools.cost import cost
from arenbels.game.tools.pay import pay
from arenbels.game.building import *

class City:

    def __init__(self,name="CityName",region=None):
        self.name = name#It is important that this name stays unique during the whole game.
        self.pop = 0#population
        self.oldPop = 0#population at last turn
        self.oldPopBdg = 0#population at last turn due to buildings
        self.popOBJ = 0#population (Objective)
        self.bdg = []#buildings
        self.happiness = 0# in -100,+100
        self.happy = 0
        self.defaultHealth = 20
        self.health = self.defaultHealth
        self.moneyFromPop = 0
        self.localTrade = 0
        self.agrarianWealth = 0
        self.globalTrade = 0#contribution of the city to global TradeOBJ
        if region is None:
            self.region = Region()
        self.history = []

    def __repr__(self):
        return "City %s:" % self.name + str((self.bdg))

    def summary(self):
        txt = """ %s :
        pop : %s
        oldPop : %s
        popOBJ : %s
        bdg : %s
        hap : %s
        varHap : %s
        health : %s
        GlobTrade : %s
        $(pop) : %s
        $(agr) : %s
        $(tra) : %s""" % (self.name,self.pop,self.oldPop,self.popOBJ,self.bdg,self.happiness,self.happy,self.health,self.globalTrade,self.moneyFromPop,self.agrarianWealth,self.localTrade)
        return txt

    def send_info(self):
        """ returns:
        population
        happiness
        health
        GlobTrade
        $(pop)
        $(agr)
        $(tra)

        useful for numpy display"""

        return (self.pop,self.happiness,self.health,self.globalTrade,self.moneyFromPop,self.agrarianWealth,self.localTrade)

    def get_history(self):
        return np.array(self.history)

    def add_bdg(self,state,buil):
        #if build.stackable:
        if cost(state.treasure,buil):
            b = buil()
            if not b.stackable:
                if hash(b) in [hash(z) for z in self.bdg]:
                    return False
            self.bdg.append(b)
            pay(state,buil)
            return True
        else:
            return False

    def end_turn(self,state,game):

        self.happy = 0
        self.health = self.defaultHealth
        self.oldPop = self.pop
        self.oldPopOBJ = self.popOBJ
        self.pop = 0
        self.popOBJ = 0
        self.localTrade = 0
        self.globalTrade = 0
        self.agrarianWealth = 0

        for buil in self.bdg:
            buil.effect(state,self)

        self.globalTrade += ceil((self.happiness - 90)/100 * self.pop)
        state.tradeOBJ += self.globalTrade
        #here self.pop is only the population with buildings.
        popBdg = self.pop
        self.pop += self.oldPop - self.oldPopBdg
        self.oldPopBdg = popBdg

        #Population increase calculus
        self.pop += increase(self.pop, self.popOBJ, game.popChangeSpeed)
        #Overpopulation
        if self.popOBJ < self.pop - 10:
            self.happy -= min((self.pop - self.popOBJ)//10,10)

        #Season changes
        self.happy += self.region.seasonHappy
        self.agrarianWealth = ceil(self.agrarianWealth * ((100 + self.region.seasonBonus) /100))

        self.happiness += self.happy

        if self.happiness <= -100:
            self.happiness = -100
            print("City : %s has Unrest !" % self.name)
        else:
            if self.happiness >= 100:
                self.happiness = 100
                print("City : %s is Happy !" % self.name )

            #Adding money to the state
            state.treasure += self.localTrade
            state.treasure += self.agrarianWealth
            self.moneyFromPop = ceil(self.pop * ((self.happiness+300) /400))
            state.treasure += self.moneyFromPop

        self.history.append(self.send_info())
