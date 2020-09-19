import jsonschema
import pytest

schema_random_dog = {
    "type": "object",
    "required": [
        "message",
        "status"
    ],
    "properties": {
        "message": {
            "type": "string"
        },
        "status": {
            "type": "string"
        }
    }
}

schema_all_dogs = {
    "type": "object",
    "required": [
        "message",
        "status"
    ],
    "properties": {
        "message": {
            "type": "array",
            "miItems": 0,
            "items": [
                {
                    "type": "string"
                },
                {
                    "type": "string"
                },
                {
                    "type": "string"
                }
            ]
        },
        "status": {
            "type": "string"
        }}}

schema_all_sub_breeds = {
    "type": "object",
    "required": [
        "message",
        "status"
    ],
    "properties": {
        "message": {
            "type": "array",
            "items": [
                {
                    "type": "string"
                },
                {
                    "type": "string"
                },
                {
                    "type": "string"
                },
                {
                    "type": "string"
                },
                {
                    "type": "string"
                },
                {
                    "type": "string"
                },
                {
                    "type": "string"
                }
            ]
        },
        "status": {
            "type": "string"
        }
    }}


def test_get_random_img(api_client):
    response = api_client.get("/api/breed/hound/images/random")
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema_random_dog)


def test_get_all_img(api_client):
    response = api_client.get("/api/breed/hound/images")
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema_all_dogs)


@pytest.mark.parametrize("number", [2, 3, 4])
def test_get_some_dogs(api_client, number):
    response = api_client.get("/api/breed/hound/images/random/{}".format(number))
    assert response.status_code == 200
    assert len(response.json()['message']) == number
    jsonschema.validate(response.json(), schema_all_dogs)


def get_list_all_sub_breeds(api_client):
    response = api_client.get("/api/breed/hound/list")
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema_all_sub_breeds)


@pytest.mark.parametrize(("sub_breed", "number"), [("afghan", 239), ("basset", 175), ("blood", 187)])
def test_get_sub_breed(api_client, sub_breed, number):
    response = api_client.get("/api/breed/hound/{}/images".format(sub_breed))
    assert response.status_code == 200
    assert len(response.json()['message']) == number
