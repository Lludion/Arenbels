
from arenbels.game.tools import GridIterator

class Grid:

    def __init__(self,elts=None):
        if elts is None:
            elts = []
        self.elts = elts
        self.l = len(self.elts)
        if self.l > 0:
            self.h = len(self.elts[0])
        else:
            self.h = 0


    def __len__(self):
        return self.l*self.h

    def __iter__(self):
        ''' Returns the Iterator object GridIterator

        returns the hashes of the buildings in the city'''
        return GridIterator(self)