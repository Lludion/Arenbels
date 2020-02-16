

class CityIterator():
    def __init__(self,city):
        self.current = 0
        self.city = city
        self.size = len(city.bdg)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.size:
            self.current += 1
            return self.city.bdg[self.current-1].name
        else:
            raise StopIteration

class GridIterator():
    def __init__(self,grid):
        self.currentL = 0
        self.current = 0
        self.elts = grid.elts
        self.l = grid.l
        self.h = grid.h

    def __len__(self):
        return self.l*self.h

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current < self.l:
            self.current = 0
            self.currentL += 1
        if self.currentL < self.h:
            ret = self.elts[self.current][self.currentL]
            self.current += 1
            return ret
        else:
            raise StopIteration