import pytest


@pytest.mark.parametrize("number,key", [(0, 'key1'), (1, 'key2'), (2, 'key3'), (3, 'key4')])
def test_get_keys(create_data, number, key):
    keys = list(create_data.keys())
    keys.sort()
    assert keys[number] == key


def test_get_items(create_data):
    keys_value = create_data.items()
    for el in keys_value:
        assert type(el) == tuple


@pytest.mark.parametrize("key,value", [('key1', 'Первый ключ'), ('key2', 'Второй ключ'), ('key3', 'Третий ключ'),
                                       ('key4', 'Четвертый ключ')])
def test_method_get(create_data, key, value):
    val = create_data.get(key)
    assert val == value


def test_clear_dict(create_data):
    create_data.clear()
    assert create_data == {}


def test_method_pop(create_data):
    val = create_data.pop('key1')
    assert val == 'Первый ключ'
    assert 'key1' not in create_data
