import jsonschema
import pytest

schema_all_breweries = {
    "type": "array",
    "items": {
        "type": "object",
        "required": [
            "id",
            "name",
            "brewery_type",
            "street",
            "city",
            "state",
            "postal_code",
            "country",
            "longitude",
            "latitude",
            "phone",
            "website_url",
            "updated_at"
        ],
        "properties": {
            "id": {
                "type": "integer"
            },
            "name": {
                "type": "string"
            },
            "brewery_type": {
                "type": "string"
            },
            "street": {
                "type": "string"
            },
            "city": {
                "type": "string"
            },
            "state": {
                "type": "string"
            },
            "postal_code": {
                "type": "string"
            },
            "country": {
                "type": "string"
            },
            "longitude": {
                "type": "string"
            },
            "latitude": {
                "type": "string"
            },
            "phone": {
                "type": "string"
            },
            "website_url": {
                "type": "string"
            },
            "updated_at": {
                "type": "string"
            }
        }}
}


def test_get_all_breweries(api_client):
    response = api_client.get("/breweries")
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema_all_breweries)


def test_filter_by_city(api_client):
    response = api_client.get("/breweries", params={'by_city': 'san_diego'})
    assert response.status_code == 200
    assert len(response.json()) == 20


@pytest.mark.parametrize(("id_brewery", "brewery_type"), [(5494, "regional"), (344, "micro"), (338, "large")])
def test_get_breweries_by_id(api_client, id_brewery, brewery_type):
    response = api_client.get("/breweries/{}".format(id_brewery))
    assert response.status_code == 200
    assert response.json()["brewery_type"] == brewery_type


@pytest.mark.parametrize(("word", "number"), [("Avondale", 2), ("Moody", 5)])
def test_search_breweries_by_word(api_client, word, number):
    response = api_client.get("/breweries/search", params={"query": word})
    assert response.status_code == 200
    assert len(response.json()) == number


def test_filter_by_state(api_client):
    response = api_client.get("/breweries", params={'by_state': 'ohio'})
    assert response.status_code == 200
    states = []
    for el in response.json():
        states.append(el['state'])
    assert "Ohio" in states
    assert len(states) == 20
