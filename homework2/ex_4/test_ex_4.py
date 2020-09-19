import pytest
from .api_client import APIClient


def test_ex_4(url, status):
    api_client = APIClient(url)
    response = api_client.get()
    assert response.status_code == int(status)
