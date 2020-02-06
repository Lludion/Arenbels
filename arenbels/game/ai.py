from arenbels.game.tools.cost import cost
from arenbels.game.tools.pay import pay
from arenbels.game.tools.sort import unhappyfirst
from arenbels.tools.shuffled import shuffled
from arenbels.game.building import *
from arenbels.game.player import Player
from random import random

class AI(Player):

    def __init__(self,name="AI",state=None):
        super().__init__(name=name,state=state)
        self.HAPPY_IMPROVE_LIST = [Inn,Bakery,FlowerMeadows,Restaurant,Chapel,HugePark]
        self.HEALTH_IMPROVE_LIST = [IceHarvest,MediumPark,Fountain,LittlePark,HugePark,IceHarvestResaler,Sewer,PavedRoads,Drains]
        self.WEALTH_IMPROVE_LIST = [Market,Barn,Bakery,House]
        self.HAPPY_DECREASE_LIST = [Barn,Quarter,Fields]
        self.HEALTH_DECREASE_LIST = [Inn,Barn,Fields]
        self.WEALTH_DECREASE_LIST = [Chapel,Fountain,LittlePark,MediumPark,HugePark,PavedRoads,Drains]

    def turn_execution(self,game):
        """ Execution of the chosen actions during a turn."""

        for city in unhappyfirst(self.state.cities):
            if city.happy < -30:
                list_bdg = self.HAPPY_IMPROVE_LIST
            elif city.health < -20:
                list_bdg = self.HEALTH_IMPROVE_LIST
            elif self.state.treasure < 2000:
                list_bdg = self.WEALTH_IMPROVE_LIST
            elif city.happy > 80:
                list_bdg = self.HAPPY_DECREASE_LIST
            elif city.health > 40:
                list_bdg = self.HEALTH_DECREASE_LIST
            elif self.state.treasure > 20000:
                list_bdg = self.WEALTH_DECREASE_LIST
            else:
                list_bdg = self.WEALTH_IMPROVE_LIST

            for b in list_bdg:
                city.add_bdg(self.state,b)

