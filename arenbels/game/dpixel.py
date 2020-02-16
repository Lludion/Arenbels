from arenbels.display.engine import Pixel

GROUNDCOLOR = (150,120,90)
WATERCOLOR = (30,75,130)
MOUNTAINCOLOR = (230,240,250)

class DPixel(Pixel):

    def __init__(self,region=None,walk=True,swim=False,x=0,y=0):
        """ Data Pixel (DPixel) class"""
        super().__init__(x,y)
        self.walk = walk
        self.swim = swim
        self.region = region
        if region is None:
            self.regionName = ""
        else:
            self.regionName = region.name

    def __repr__(self):
        return "<%s>" % (self.region)

    def get_color(self):
        if self.swim:
            return WATERCOLOR
        elif self.walk:
            return GROUNDCOLOR
        else:
            return MOUNTAINCOLOR