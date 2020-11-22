def test_string_capitalize():
    string = 'zolkin'
    new_str = string.capitalize()
    assert new_str[0] == 'Z'


def test_delete_spaces_from_string():
    string = '   Zolkin   '
    new_str = string.strip()
    assert ' ' not in new_str


def test_length_string():
    string = 'Zolkin Dmitriy'
    assert len(string) == 14


def test_split_string():
    string = 'apple,lemon,orange'
    assert type(string.split()) == list


def test_isdigit_string():
    string = 'Zolkin Dmitriy'
    assert string.isdigit() is False
