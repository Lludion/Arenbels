from math import ceil
from arenbels.game.tools.increase import increase
from arenbels.game.region import Region
import numpy as np
from arenbels.game.tools.cost import cost
from arenbels.game.tools.pay import pay
from arenbels.game.building import *
from arenbels.game.tools.iterators import CityIterator
from random import choice
from collections import defaultdict

class City:

    def __init__(self,name="CityName",region=None):
        self.name = name#It is important that this name stays unique during the whole game.
        self.pop = 0#population
        self.oldPop = 0#population at last turn
        self.oldPopBdg = 0#population at last turn due to buildings
        self.popOBJ = 0#population (Objective)
        self.bdg = [CityCenter()]#buildings
        self.happiness = 0# in -100,+100
        self.happy = 0
        self.defaultHealth = 20
        self.health = self.defaultHealth
        self.moneyFromPop = 0
        self.localTrade = 0
        self.agrarianWealth = 0
        self.globalTrade = 0#contribution of the city to global TradeOBJ
        self.alreadybuilt = False# renews on each turn.
        if region is None:
            self.region = Region()
        self.history = []
        self.owner = None

    def __iter__(self):
        ''' Returns the Iterator object CityIterator

        returns the hashes of the buildings in the city'''
        return CityIterator(self)

    def __repr__(self):
        dict = defaultdict(int)
        for b in self.bdg:
            dict[b.name] += 1
        return "City %s:" % self.name + str((dict))

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
        $(ind)

        useful for numpy display"""

        return (self.pop,self.happiness,self.health,self.globalTrade,self.moneyFromPop,self.agrarianWealth,self.localTrade,self.industry,self.happy)

    def get_history(self):
        return np.array(self.history)

    def set_region(self,region):
        self.region = region
        if self not in region.cities:
            region.cities.append(self)

    def add_bdg(self,state,buil):
        """ One can construct up to one building per city per turn."""
        if not self.alreadybuilt:
            try:
                b = buil()
            except TypeError:
                buil = choice(buil)
                b = buil()
            if cost(state.treasure,buil):
                if not b.stackable:
                    if b.name in self:
                        return False
                for req in b.required:
                    if type(req) != type(Requirement()):
                        if req().name not in self:
                            return False
                    elif req.fails_requirement(self):
                        return False
                self.bdg.append(b)
                pay(state,buil)
                self.alreadybuilt = True
                if b.name == "Cathedral" or b.name == "Factory":
                    print(self.name,"built",b.name)
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
        self.industry = 0

        for buil in self.bdg:
            buil.effect(state,self)

        self.globalTrade += max(-100,ceil((self.region.happiness[self.owner] - 90)/100 * self.pop))
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

        #Diseases
        if self.health < 0:
            self.happy += self.health//10
            self.pop += self.health//20 + 1
        if self.health >= 20:
            self.happy += 1

        #Season changes
        self.agrarianWealth = ceil(self.agrarianWealth * ((100 + self.region.seasonBonus) /100))


    def add_money(self,state):
        """ To be executed after all cities of the region that are controlled by
        this player have added their happiness"""

        if self.region.happiness[self.owner] <= -100:
            self.region.happiness[self.owner] = -100
            print("City : %s has Unrest !" % self.name)
        else:
            if self.region.happiness[self.owner] >= 100:
                self.region.happiness[self.owner] = 100
                #print("City : %s is Happy !" % self.name )

            #Adding money to the state
            state.treasure += self.localTrade
            state.treasure += self.agrarianWealth
            state.treasure += self.industry
            self.moneyFromPop = ceil(self.pop * ((self.region.happiness[self.owner]+300) /400) / 10)
            state.treasure += self.moneyFromPop

        self.happiness = self.region.happiness[self.owner]
        self.history.append(self.send_info())
        self.alreadybuilt = False
