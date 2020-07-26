import math

from figure import Figure


class Circle(Figure):
    def __init__(self, radius, angles=0, name=u'Круг'):
        self.__radius = radius
        self.__angles = angles
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def angles(self):
        return self.__angles

    @property
    def area(self):
        return math.pi * self.__radius * self.__radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.__radius


r = Circle(5)
print(r.area)
print(r.perimeter)
