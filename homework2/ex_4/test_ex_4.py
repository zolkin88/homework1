import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru")
    # parser.addoption("--status_code", default=200)


@pytest.fixture(scope="session")
def my_function(request):
    base_url = request.config.getoption("--url")
    # status_code = request.config.getoption("--status_code")
    # return base_url, status_code
    return base_url

def test_ex_4(api_client, my_function):
    base_url = my_function
    response = api_client.get(base_url)
    assert response.status_code == 200
