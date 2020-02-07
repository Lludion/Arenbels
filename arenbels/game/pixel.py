

GROUNDCOLOR = (150,120,90)
WATERCOLOR = (30,75,130)
MOUNTAINCOLOR = (230,240,250)

class Pixel:

    def __init__(self,region=None,walk=True,swim=False,x=0,y=0):
        self.walk = walk
        self.swim = swim
        self.region = region
        if region is None:
            self.regionName = ""
        else:
            self.regionName = region.name
        self.x = x
        self.y = y

    def __repr__(self):
        return "(%s)" % (self.region)

    def get_color(self):
        if self.swim:
            return WATERCOLOR
        elif self.walk:
            return GROUNDCOLOR
        else:
            return MOUNTAINCOLOR