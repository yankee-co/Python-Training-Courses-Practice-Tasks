from abc import ABC, abstractmethod
import math

class Volumetric(ABC):
    @abstractmethod
    def volume(self):
        pass

class Area(ABC):
    @abstractmethod
    def area(self):
        pass

class Shape3D(Volumetric, Area, ABC):
    @abstractmethod
    def __eq__(self, other):
        pass
    def __ne__(self, other):
        pass
    def __gt__(self, other):
        pass
    def __lt__(self, other):
        pass

class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius
        self.V = 4/3 * math.pi * self.radius**3

    def area(self):
        S = 4*math.pi*pov(self.radius, 2)

class Shape2D(Area, ABC):
    @abstractmethod
    def __eq__(self, other):
        pass
    def __ne__(self, other):
        pass
    def __gt__(self, other):
        pass
    def __lt__(self, other):
        pass

class Parallelepiped(Shape3D):
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

    @property
    def area(self):
        A = 2*(self.length + self.width + self.height)
        return A

    def __str__(self):
        return f'Parallelepiped {self.length} x {self.width} x {self.height}'

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



class Parallelogram(Shape2D):
    def __init__(self, a, b, A):
        self.a = a
        self.b = b
        self.A = A

    @staticmethod
    def sinus(self):
        sinA = math.sin(self.A*(math.pi / 180))
        return round(sinA, 3)

    @property
    def area(self):
        S = self.a * self.b * self.sinus
        return S

    def __eq__(self, other):
        """ equal """
        return self.area == other.area
    def __ne__(self, other):
        """ not equal """
        return self.area != other.area
    def __gt__(self, other):
        """ greater """
        return self.area > other.area
    def __lt__(self, other):
        """ lower """
        return self.area < other.area

a = Parallelepiped(5, 10, 30)
b = Parallelogram(10, 15, 30)
