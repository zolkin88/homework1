import pytest


def test_add_to_list():
    test_list = []
    test_list.append(1)
    assert len(test_list) == 1


@pytest.mark.parametrize("remove, expected", [(1, 2), (2, 1), (3, 1)])
def test_remove_from_list(remove, expected):
    test_list = [1, 2, 3]
    test_list.remove(remove)
    assert expected in test_list


def test_extend_list():
    test_list1 = [1, 2]
    test_list2 = [3, 4]
    test_list1.extend(test_list2)
    assert len(test_list1) == 4


@pytest.mark.parametrize("number, expected", [(2, 4), (3, 2)])
def test_count_in_list(number, expected):
    test_list1 = [1, 2, 4, 2, 2, 3, 3, 2]
    assert test_list1.count(number) == expected


def test_reverse_list():
    test_list1 = [1, 2, 3, 4, 5, 6]
    test_list1.reverse()
    assert test_list1[0] == 6
