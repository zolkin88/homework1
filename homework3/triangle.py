import math

from figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c, angles=3, name=u'Треугольник'):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__angles = angles
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def angles(self):
        return self.__angles

    @property
    def perimeter(self):
        return self.__a + self.__b + self.__c

    @property
    def area(self):
        p_perimeter = self.perimeter / 2
        return math.sqrt(p_perimeter * (p_perimeter - self.__a) * (p_perimeter - self.__b) * (
                p_perimeter - self.__c))


tri = Triangle(3, 4, 5)
tri2 = Triangle(4, 5, 6)
print(tri.area)
print(tri2.area)
print(tri.add_square(tri2))
