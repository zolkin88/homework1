def test_union_set():
    a = {1, 2, 3, 4}
    b = {4, 5, 6, 7}
    for el in [1, 2, 3, 4, 5, 6, 7]:
        assert el in a.union(b)


def test_intersection_set():
    a = {1, 2, 3, 4}
    b = {4, 5, 6, 7}
    assert 4 in a.intersection(b)


def test_difference_set():
    a = {1, 2, 3, 4}
    b = {4, 5, 6, 7}
    assert 4 not in a.difference(b)


def test_symmetric_difference_set():
    a = {1, 2, 3, 4}
    b = {4, 5, 6, 7}
    assert 4 not in a.symmetric_difference(b)
    for el in [1, 2, 3, 5, 6, 7]:
        assert el in a.symmetric_difference(b)


def test_issubset_set():
    a = {1, 2, 3, 4}
    b = {4, 5, 6, 7, 1, 2, 3}
    assert a.issubset(b)
