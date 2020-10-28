import random

class RangeIter():

    def __init__(self, start, stop):
        self._start = start
        self._stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        return random.randint(self._start, self._stop)
    
obj = RangeIter(1, 39)
it = iter(obj)
while True:
    try:
        v = next(it)
        print(v)
        if v % 17 == 0:
            break
    except StopIteration:
        break
