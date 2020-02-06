from arenbels.game.tools.cost import cost
from arenbels.game.tools.pay import pay
from arenbels.tools.shuffled import shuffled
from arenbels.game.building import *
from arenbels.game.player import Player

class AI(Player):

    def __init__(self,name="AI",state=None):
        super().__init__(name=name,state=state)

    def turn_execution(self,game):
        """ Execution of the chosen actions during a turn."""
        if cost(self.state.treasure,House):
            for city in shuffled(self.state.cities):
                city.bdg.append(House())
                pay(self.state,House)