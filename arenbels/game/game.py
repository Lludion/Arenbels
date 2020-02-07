from arenbels.game.world import World
from arenbels.debug.debug import logger,f

class Game:

    def __init__(self):
        self.new_game()
        self.set_parameters()

    def new_game(self):
        self.players = []
        self.world = World()
        self.turn = 1
        self.season = 0


    def set_parameters(self):
        #Whether it prints things.
        self.verbose = False
        #Name of the infos in the city_history panel
        self.city_info = ["Population","Happiness","Health","Global Trade","$(pop)","$(agr)","$(tra)"]
        #Name of the infos in the state_history panel
        self.state_info = ["Treasure","Trade","Global Health","Gain"]
        #Number of turns it takes to reach the actual tradeOBJ value
        self.tradeChangeSpeed = 10
        #Number of turns it takes to reach the actual popOBJ value
        self.popChangeSpeed = 12

    def play(self,lastturn=11):
        while self.turn < lastturn:
            self.play_turn()

    def play_turn(self):
        logger.info("Turn "+str(self.turn))
        for player in self.players:
            player.play_turn(self)
        self.changeSeason()
        self.turn += 1

    def get_scores(self):
        scores = []
        for player in self.players:
            logger.info((player.name))
            poptot = 0
            happytot = 0
            for city in player.state.cities:
                poptot += city.pop
                happytot += city.happiness
            logger.info(f("Population",poptot))
            logger.info(f("Treasure : ",player.state.treasure))
            logger.info(f("Last gain : ",player.state.gain()))
            logger.info(f("Happiness : ",int(happytot/len(player.state.cities))))

            score = int((poptot*100*((900+happytot/len(player.state.cities))/1000) + player.state.treasure + player.state.gain()*100) /1000)
            logger.info(f("SCORE: ",score))

            scores.append((score))
        return sum(scores)

    def changeSeason(self):
        """ changes the season.
        0 : spring
        1 : summer
        2 : fall/autumn
        3 : winter
        """
        self.season = (self.season + 1) % 4

        for player in self.players:
            for city in player.state.cities:
                city.region.set_seasonBonus(self.season)


