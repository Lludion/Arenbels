from math import ceil

class Building:

    def __init__(self):
        self.name = "DefaultBuilding"
        self.type = "Building"
        self.pic = None
        self.required = []
        self.stackable = False
        self.cost = 1000

    def effect(self,state,city="DefaultCity"):
        """ Will be used by the different Building subclasses."""
        logger.info("No effect implemented. See building.py file.")

    def __repr__(self):
        return "Building " + str(self.__class__.__name__)

    def __hash__(self):
        return hash(self.name)

    def __iter__(self):
        return self

    def __getitem__(self, key):
        return self


class CityCenter(Building):
    def __init__(self):
        super().__init__()
        self.name = "City Center"
        self.type = ["State"]
        self.cost = 200

    def effect(self,state,city):
        city.pop += 1
        city.popOBJ += 10

class House(Building):

    def __init__(self):
        super().__init__()
        self.name = "House"
        self.type = ["Housing"]
        self.stackable = True
        self.cost = 300

    def effect(self,state,city):
        city.pop += 4
        city.popOBJ += 10
        city.health -= 1

class Quarter(Building):

    def __init__(self):
        super().__init__()
        self.name = "Quarter"
        self.type = ["Housing"]
        self.required = [House]
        self.cost = 900
        stackable = True

    def effect(self,state,city):
        city.popOBJ += 60
        city.happy -= 3
        city.health -= 5

class Inn(Building):

    def __init__(self):
        super().__init__()
        self.name = "Inn"
        self.type = ["Pub"]
        self.cost = 600

    def effect(self,state,city):
        city.localTrade += 10 + ceil(min(city.oldPop / 100,30))
        city.globalTrade += 20
        city.happy += 1
        city.pop += 2
        city.popOBJ += 5
        city.health -= 20

class Restaurant(Building):

    def __init__(self):
        super().__init__()
        self.name = "Restaurant"
        self.type = ["Pub"]
        self.required = [Inn]
        self.cost = 1300

    def effect(self,state,city):
        city.localTrade += 5
        city.globalTrade += 2 + ceil(max(0,min((city.oldPop - 2000)/ 200,28)))
        city.happy += 1
        city.pop += 2
        city.popOBJ += 5

class Stalls(Building):
    def __init__(self):
        super().__init__()
        self.name = "Stalls"
        self.type = ["Trade"]
        self.cost = 300

    def effect(self,state,city):
        city.localTrade += 2
        city.globalTrade += 5
        city.health -= 1

class Market(Building):
    def __init__(self):
        super().__init__()
        self.name = "Marketplace"
        self.type = ["Trade"]
        self.required = [Stalls]
        self.cost = 1100

    def effect(self,state,city):
        city.localTrade += 2
        city.globalTrade += 40
        city.health -= 1

class CoveredMarket(Building):
    def __init__(self):
        super().__init__()
        self.name = "Covered Market"
        self.type = ["Trade"]
        self.required = [Market,Inn]
        self.cost = 3000

    def effect(self,state,city):
        city.localTrade += 6
        city.globalTrade += 100
        city.happy -= 1

class Fields(Building):
    def __init__(self):
        super().__init__()
        self.name = "Fields"
        self.type = ["Agrarian"]
        self.stackable = True
        self.cost = 200

    def effect(self,state,city):
        city.agrarianWealth += 5
        city.popOBJ += 5
        city.health -= 5

class FlowerMeadows(Building):
    def __init__(self):
        super().__init__()
        self.name = "Flower Meadows"
        self.type = ["Agrarian","Environment"]
        self.cost = 200
        self.requirement = [Requirement(health=30)]

    def effect(self,state,city):
        state.treasure -= 15
        city.agrarianWealth += 5
        city.popOBJ += 10
        city.health += 5
        city.happy += 2

class Barn(Building):
    def __init__(self):
        super().__init__()
        self.name = "Barn"
        self.type = ["Agrarian"]
        self.required = [Fields]

    def effect(self,state,city):
        city.agrarianWealth += 15
        city.popOBJ += 10
        city.health -= 10

class IceHarvest(Building):
    def __init__(self):
        super().__init__()
        self.name = "Ice Harvest"
        self.type = ["Artisan"]

    def effect(self,state,city):
        state.treasure -= 1
        city.globalTrade += 2
        city.popOBJ += 20
        state.globHealth += 10

class IceHarvestResaler(Building):
    def __init__(self):
        super().__init__()
        self.name = "Ice Resaler"
        self.type = ["Trade","Sanitation"]
        self.cost = 2000

    def effect(self,state,city):
        city.globalTrade += 20
        city.popOBJ += 10
        city.health += 40

class Bakery(Building):
    def __init__(self):
        super().__init__()
        self.name = "Bakery"
        self.type = ["Artisan"]
        self.cost = 1200

    def effect(self,state,city):
        city.localTrade += 1
        city.globalTrade += 1
        city.pop += 5
        city.popOBJ += 5
        city.happy += 2

class LittlePark(Building):
    def __init__(self):
        super().__init__()
        self.name = "Little Park"
        self.type = ["Environment"]
        self.cost = 200

    def effect(self,state,city):
        state.treasure -= 5
        city.happy += 1

class MediumPark(Building):
    def __init__(self):
        super().__init__()
        self.name = "Medium Park"
        self.type = ["Environment"]
        self.required = [LittlePark]
        self.cost = 1000

    def effect(self,state,city):
        state.treasure -= 15
        city.globalTrade += 1
        city.happy += 2
        city.health += 10

class HugePark(Building):
    def __init__(self):
        super().__init__()
        self.name = "Huge Park"
        self.type = ["Environment"]
        self.required = [MediumPark]
        self.cost = 3000

    def effect(self,state,city):
        state.treasure -= 50
        city.globalTrade += 4
        city.happy += 6
        city.health += 50

class Fountain(Building):
    def __init__(self):
        super().__init__()
        self.name = "Fountain"
        self.type = ["Environment","Sanitation"]
        self.stackable = False

    def effect(self,state,city):
        state.treasure -= 2
        city.globalTrade += 2
        city.happy += 1
        city.health += 20

class LargeFountain(Building):
    def __init__(self):
        super().__init__()
        self.name = "Fountain"
        self.type = ["Environment","Sanitation"]
        self.stackable = False
        self.required = [Fountain,PavedRoads]
        self.cost = 2500

    def effect(self,state,city):
        state.treasure -= 3
        city.globalTrade += 8
        city.popOBJ += 10
        city.happy += 1
        city.health += 30


class Drains(Building):
    def __init__(self):
        super().__init__()
        self.name = "Drains"
        self.type = ["Sanitation"]
        self.stackable = True

    def effect(self,state,city):
        state.treasure -= 40
        city.popOBJ += 10
        city.health += 100

class Sewer(Building):
    def __init__(self):
        super().__init__()
        self.name = "Sewer"
        self.type = ["Sanitation"]
        self.required = [Drains]

    def effect(self,state,city):
        state.treasure -= 100 + ceil(city.oldPop/100)
        city.popOBJ += 20
        city.health += 150 + ceil(city.oldPop/100)

class PavedRoads(Building):
    def __init__(self):
        super().__init__()
        self.name = "Paved Roads"
        self.type = ["Sanitation","State","Trade"]
        self.required = [CityCenter]
        cost = 10000

    def effect(self,state,city):
        state.treasure -= 5
        city.popOBJ += 20
        city.localTrade += 5
        city.globalTrade += min(ceil(city.oldPop/10),100)
        city.health += ceil(city.oldPop/20)

class Chapel(Building):
    def __init__(self):
        super().__init__()
        self.name = "Chapel"
        self.type = ["Religious"]

    def effect(self,state,city):
        state.treasure -= 20
        city.happy += 2

class Church(Building):
    def __init__(self):
        super().__init__()
        self.name = "Church"
        self.type = ["Religious"]
        self.required = [Chapel]
        self.cost = 1500
        self.stackable = True

    def effect(self,state,city):
        state.treasure -= 50
        city.happy += 4

class Monastery(Building):
    def __init__(self):
        super().__init__()
        self.name = "Monastery"
        self.type = ["Religious"]
        self.required = [Chapel]
        self.cost = 1100

    def effect(self,state,city):
        state.treasure -= 40
        city.happy += 1
        city.globalTrade += 40
        city.popOBJ += 20
        city.health += 5


class Cathedral(Building):
    def __init__(self):
        super().__init__()
        self.name = "Cathedral"
        self.type = ["Religious"]
        self.required = [Church,PavedRoads,Drains,Quarter]
        self.cost = 22000

    def effect(self,state,city):
        state.treasure -= 200
        city.happy += 10
        city.globalTrade += 50

class Forge(Building):
    def __init__(self):
        super().__init__()
        self.name = "Forge"
        self.type = ["Industry"]
        self.required = [Requirement(pop=200,health=0)]

    def effect(self,state,city):
        city.industry += 50
        city.happy -= 2

class Workshop(Building):
    def __init__(self):
        super().__init__()
        self.name = "Workshop"
        self.type = ["Industry"]
        self.stackable = True
        self.cost = 2000

    def effect(self,state,city):
        city.industry += 100
        city.happy -= 4
        city.health -= 10

class Factory(Building):
    def __init__(self):
        super().__init__()
        self.name = "Factory"
        self.type = ["Industry"]
        self.cost = 8000
        self.required = [Workshop,Forge]

    def effect(self,state,city):
        city.industry += 500
        city.globalTrade += 100
        city.happy -= 15
        city.health -= 50

class No(Building):
    """ Used in AI to say: do not build anything. Used with random.choose"""
    def __init__(self):
        super().__init__()
        self.required = [Requirement(impossible=True)]

class Requirement:

    def __init__(self,pop=0,health=-99999,impossible=False):
        self.pop_req = pop
        self.health_req = health
        self.impossible = impossible

    def fails_requirement(self,city):
        if city.pop < self.pop_req:
            return False
        if city.health < self.health_req:
            return False
        if self.impossible:
            return False
        return True

