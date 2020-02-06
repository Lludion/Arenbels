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
        self.HAPPY_IMPROVE_LIST = [Inn,Bakery,FlowerMeadows,Restaurant,Chapel,Cathedral,HugePark,Monastery,Church]
        self.HEALTH_IMPROVE_LIST = [IceHarvest,MediumPark,Fountain,LittlePark,HugePark,IceHarvestResaler,Sewer,PavedRoads,Drains]
        self.WEALTH_IMPROVE_LIST = [Market,Barn,Bakery,Forge,Factory,(House,Workshop,Workshop)]
        self.HAPPY_DECREASE_LIST = [Barn,Quarter,Forge,Factory,(Fields,Workshop,Workshop)]
        self.HEALTH_DECREASE_LIST = [Inn,Barn,Factory,Forge,Fields]
        self.WEALTH_DECREASE_LIST = [Chapel,Fountain,LittlePark,MediumPark,HugePark,PavedRoads,Sewer,Factory,Forge,Cathedral,House]

    def turn_execution(self,game):
        """ Execution of the chosen actions during a turn."""

        for city in unhappyfirst(self.state.cities):
            if city.happiness < -30:
                for b in self.HAPPY_IMPROVE_LIST:
                    city.add_bdg(self.state,b)
            if city.health < -20:
                for b in self.HEALTH_IMPROVE_LIST:
                    city.add_bdg(self.state,b)
            if self.state.treasure < 2000:
                for b in self.WEALTH_IMPROVE_LIST:
                    city.add_bdg(self.state,b)
            if city.happiness > 80:
                for b in self.HAPPY_DECREASE_LIST:
                    city.add_bdg(self.state,b)
            if city.health > 40:
                for b in self.HEALTH_DECREASE_LIST:
                    city.add_bdg(self.state,b)
            if self.state.treasure > 20000:
                for b in self.WEALTH_DECREASE_LIST:
                    city.add_bdg(self.state,b)
            for b in self.HAPPY_IMPROVE_LIST:
                city.add_bdg(self.state,b)

