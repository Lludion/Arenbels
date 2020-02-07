from arenbels.game.tools.cost import cost
from arenbels.game.tools.pay import pay
from arenbels.game.tools.sort import unhappyfirst
from arenbels.tools.shuffled import shuffled
from arenbels.game.building import *
from arenbels.game.player import Player
from random import random,choice

class AI(Player):

    def __init__(self,name="AI",state=None):
        super().__init__(name=name,state=state)
        self.HAPPY_IMPROVE_LIST = [Inn,Bakery,FlowerMeadows,Restaurant,Chapel,Cathedral,HugePark,Monastery,Church]
        self.HEALTH_IMPROVE_LIST = [IceHarvest,MediumPark,Fountain,LittlePark,HugePark,IceHarvestResaler,Sewer,PavedRoads,Drains]
        self.WEALTH_IMPROVE_LIST = [Barn,Bakery,Forge,Factory,Stalls,Market,CoveredMarket,(House,Workshop,Workshop),Inn]
        self.HAPPY_DECREASE_LIST = [Barn,Forge,Factory,(Fields,Workshop,Workshop),Quarter]
        self.HEALTH_DECREASE_LIST = [Inn,Barn,Market,Stalls,Factory,Forge,(House,Fields,Workshop),Quarter]
        self.WEALTH_DECREASE_LIST = [Chapel,Fountain,LargeFountain,LittlePark,MediumPark,HugePark,PavedRoads,Sewer,Factory,Forge,Cathedral,CoveredMarket,(Quarter,House)]

    def ai_add_bdg(self,city,buil):
        """ Adds a building in a smart way (takes into account factors such as
        climate, etc ...
        """
        try:
            b = buil()
        except TypeError:
            buil = choice(buil)
            b = buil()
        if ["Agrarian"] == b.type :
            if city.region.ruralSum() <= 0:
                if random() < 0.95:
                    buil = (House, Market)
            elif city.region.ruralSum() <= 20:
                if random() < 0.5:
                    buil = (House, Market)
        return city.add_bdg(self.state,buil)

    def turn_execution(self,game):
        """ Execution of the chosen actions during a turn."""

        for city in unhappyfirst(self.state.cities):
            if city.happiness < -30 or city.happy < -4 or (city.happy < -1 and city.happiness < 50) or (city.happy < 0 and city.happiness < 10):
                for b in self.HAPPY_IMPROVE_LIST:
                    self.ai_add_bdg(city,b)
            else:#Enforcing a stronger priority for this type of buildings
                if city.health < -20:
                    for b in self.HEALTH_IMPROVE_LIST:
                        self.ai_add_bdg(city,b)
                if self.state.gain() < 100:
                    for b in self.WEALTH_IMPROVE_LIST:
                        self.ai_add_bdg(city,b)
                if not (city.health < -20 or self.state.treasure < 2000):#other priority
                    if city.happiness > 80:
                        if random()>0.9:
                            for b in self.HAPPY_DECREASE_LIST:
                                self.ai_add_bdg(city,b)
                            else:
                                return
                    if city.health > 40:
                        for b in self.HEALTH_DECREASE_LIST:
                            self.ai_add_bdg(city,b)
                    if self.state.treasure > 20000:
                        for b in self.WEALTH_DECREASE_LIST:
                            self.ai_add_bdg(city,b)

