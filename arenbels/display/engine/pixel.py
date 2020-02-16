
class Pixel:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.size = -1
        self.renew_size = False

    def boundaries(self):
        return (self.x*self.size,(self.x+1)*self.size,self.y*self.size,(self.y+1)*self.size)