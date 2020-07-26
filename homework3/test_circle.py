import math

from circle import Circle


def test_get_angle():
    cir = Circle(3)
    assert cir.angles == 0


def test_get_name():
    cir = Circle(3, 4)
    assert cir.name == u'Круг'


def test_perimeter():
    cir = Circle(3)
    assert cir.perimeter == 2 * math.pi * 3


def test_area():
    cir = Circle(3)
    assert cir.area == math.pi * 3 * 3


def test_add_square():
    cir1 = Circle(4)
    cir2 = Circle(5)
    assert (cir1.add_square(cir2)) == cir1.area + cir2.area
