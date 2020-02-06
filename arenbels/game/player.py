from arenbels.game.state import State
from arenbels.game.building import *

class Character:

    def __init__(self,female=False):
        self.female = female

    def pronoun(self):
        if self.female:
            return "She"
        else:
            return "He"

class Player(Character):

    def __init__(self,name="Player",state=None):
        super().__init__()
        self.name = name
        self.state = state
        if self.state is None:
            self.state = State()
        self.counselor_explanation = ""
        self.female = False

    def __repr__(self):

        return "Player " + self.name + " of " + str(self.state)

    def play_turn(self,game):
        self.turn_execution(game)
        self.state.end_turn(game)
        self.counselor()

    def turn_execution(self,game):
        """ Execution of the chosen actions during a turn.

        Please take note of the fact that by default, it does nothing.
        (previously, it launched an AI)"""
        pass

    def counselor(self,game):

    def counselor(self):
            self.counselor_explanation = (self.name + " now has " + str(self.state.treasure) + " gold.\n")
            self.counselor_explanation += (self.pronoun() + " gained " + str(self.state.gain()) + " money last turn.\n")
            #self.counselor_explanation += ("Of which " + str(self.state.moneyFromTrade) + " came from Trade.\n")
            #self.counselor_explanation += (" Trade value : %s .\n" % str(self.state.trade))
            self.counselor_explanation += self.state.__repr__()

            for city in self.state.cities:

                #self.counselor_explanation += city.name + ", where " + str(city.pop) + " inhabitants live, has a happiness of " +  str(city.happiness)
                #self.counselor_explanation += ", compared to " + str(city.happiness - city.happy) + " last turn.\n"
                self.counselor_explanation += city.summary() + "\n"
            self.counselor_explanation += "\n"
            print(self.counselor_explanation)

