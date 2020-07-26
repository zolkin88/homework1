from figure import Figure


class Square(Figure):
    def __init__(self, a, angles=4, name=u'Квадрат'):
        self.__a = a
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
        return 4 * self.__a

    @property
    def area(self):
        return self.__a * self.__a


sq = Square(5)
print(sq.area)
print(sq.perimeter)
