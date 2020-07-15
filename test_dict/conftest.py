import pytest


@pytest.fixture(scope='function')
def create_data():
    test_dict = {"key1": "Первый ключ", "key2": "Второй ключ", "key3": "Третий ключ", "key4": "Четвертый ключ"}
    return test_dict
