

class CityIterator():
    def __init__(self,city):
        self.current = 0
        self.city = city
        self.high = len(city.bdg)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            self.current += 1
            return hash(self.city.bdg[self.current-1])
        else:
            raise StopIteration