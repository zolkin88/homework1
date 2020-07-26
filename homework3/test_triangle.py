import pytest

from triangle import Triangle


def test_get_angle():
    tri = Triangle(3, 4, 5)
    assert tri.angles == 3


def test_get_name():
    tri = Triangle(3, 4, 5)
    assert tri.name == u'Треугольник'


@pytest.mark.parametrize("perimeter,a,b,c", [(12, 3, 4, 5), (18, 5, 6, 7)])
def test_perimeter(perimeter, a, b, c):
    tri = Triangle(a, b, c)
    assert tri.perimeter == perimeter


def test_area():
    tri = Triangle(3, 4, 5)
    assert tri.area == 6.0


def test_add_square():
    tri = Triangle(3, 4, 5)
    tri2 = Triangle(4, 5, 6)
    assert (tri.add_square(tri2)) == tri.area + tri2.area
