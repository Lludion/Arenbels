

class Unit:

    def __init__(self):
        self.name = "DefaultUnit"
        self.cost = 10
        self.hp = 100
        self.maxhp = 100
        self.pow = 10


class Pikemen(Unit):

    def __init__(self):
        super().__init__()
        self.cost = 5
        self.hp = 90
        self.maxhp = 90
        self.pow = 8

class Peasant(Unit):

    def __init__(self):
        super().__init__()
        self.cost = 2
        self.hp = 60
        self.maxhp = 60
        self.pow = 7