from arenbels.game.world import World

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
        #Number of turns it takes to reach the actual tradeOBJ value
        self.tradeChangeSpeed = 10
        #Number of turns it takes to reach the actual popOBJ value
        self.popChangeSpeed = 12

    def play(self,lastturn=11):
        while self.turn < lastturn:
            self.play_turn()

    def play_turn(self):
        print("Turn ",self.turn)
        for player in self.players:
            player.play_turn(self)
        self.changeSeason()
        self.turn += 1

    def changeSeason(self):
        """ changes the season.
        0 : spring
        1 : summer
        2 : fall/autumn
        3 : winter
        """
        self.season = (self.season + 1) % 4


