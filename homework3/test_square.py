import pytest

from square import Square


def test_get_angle():
    sq = Square(3)
    assert sq.angles == 4


def test_get_name():
    sq = Square(3)
    assert sq.name == u'Квадрат'


@pytest.mark.parametrize("perimeter,a", [(12, 3), (20, 5)])
def test_perimeter(perimeter, a):
    sq = Square(a)
    assert sq.perimeter == perimeter


@pytest.mark.parametrize("area,a", [(9, 3), (100, 10)])
def test_area(area, a):
    sq = Square(a)
    assert sq.area == area


def test_add_square():
    sq1 = Square(3)
    sq2 = Square(4)
    assert (sq1.add_square(sq2)) == sq1.area + sq2.area
