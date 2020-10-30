from collections.abc import ABCMeta, abstractmethod


class Parallelepiped():
    length: float
    width: float
    height: float


    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    @property
    def volume(self):
        V = self.length * self.width * self.height
        return V

    def __eq__(self, other):
        """ equal """
        return self.volume == other.volume
    def __ne__(self, other):
        """ not equal """
        return self.volume != other.volume
    def __gt__(self, other):
        """ greater """
        return self.volume > other.volume
    def __lt__(self, other):
        """ lower """
        return self.volume < other.volume

    def __str__(self):
        return f'Parallelepiped {self.length} x {self.width} x {self.height}'

class Volumetric(metaclass = ABCMeta):
    @abstractmethod
    def volume(self):
        pass

class Shape3D(metaclass = ABCMeta, Volumetric):
    @abstractmethod


a = Parallelepiped(1, 2, 3)
b = Parallelepiped(1, 2, 4)

print(Parallelepiped.__str__(b)) # Parallelepiped 1 x 2 x 4
