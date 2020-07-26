import pytest

from rectangle import Rectangle


def test_get_angle():
    rec = Rectangle(3, 4)
    assert rec.angles == 4


def test_get_name():
    rec = Rectangle(3, 4)
    assert rec.name == u'Прямоуглольник'


@pytest.mark.parametrize("perimeter,a,b", [(14, 3, 4), (22, 5, 6)])
def test_perimeter(perimeter, a, b):
    rec = Rectangle(a, b)
    assert rec.perimeter == perimeter


@pytest.mark.parametrize("area,a,b", [(12, 3, 4), (30, 5, 6)])
def test_area(area, a, b):
    rec = Rectangle(a, b)
    assert rec.area == area


def test_add_square():
    rec1 = Rectangle(3, 4)
    rec2 = Rectangle(4, 5)
    assert (rec1.add_square(rec2)) == rec1.area + rec2.area
