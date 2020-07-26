from figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height, angles=4, name=u'Прямоуглольник'):
        self.__width = width
        self.__height = height
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
        return self.__width * self.__height

    @property
    def perimeter(self):
        return 2 * (self.__width + self.__height)


r = Rectangle(5, 6)
area = r.area
perimeter = r.perimeter
print(area)
print(perimeter)
