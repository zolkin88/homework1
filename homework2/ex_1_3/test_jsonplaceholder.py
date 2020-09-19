import jsonschema
import pytest

schema_all_posts = {
    "type": "array",
    "items": {
        "type": "object",
        "required": [
            "userId",
            "id",
            "title",
            "body"
        ],
        "properties": {
            "userId": {
                "type": "integer"
            },
            "id": {
                "type": "integer"
            },
            "title": {
                "type": "string"
            },
            "body": {
                "type": "string"
            }
        }
    }
}

schema_user = {
    "type": "object",
    "required": [
        "id",
        "name",
        "username",
        "email",
        "address",
        "phone",
        "website",
        "company"
    ],
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "username": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "address": {
            "type": "object",
            "required": [
                "street",
                "suite",
                "city",
                "zipcode",
                "geo"
            ],
            "properties": {
                "street": {
                    "type": "string"
                },
                "suite": {
                    "type": "string"
                },
                "city": {
                    "type": "string"
                },
                "zipcode": {
                    "type": "string"
                },
                "geo": {
                    "type": "object",
                    "required": [
                        "lat",
                        "lng"
                    ],
                    "properties": {
                        "lat": {
                            "type": "string"
                        },
                        "lng": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "phone": {
            "type": "string"
        },
        "website": {
            "type": "string"
        },
        "company": {
            "type": "object",
            "required": [
                "name",
                "catchPhrase",
                "bs"
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "catchPhrase": {
                    "type": "string"
                },
                "bs": {
                    "type": "string"
                }
            }
        }
    }
}

data_post = {
    "id": 101,
    "title": "foo",
    "body": "bar",
    "userId": 1
}


def test_get_all_posts(api_client):
    response = api_client.get("/posts")
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema_all_posts)


@pytest.mark.parametrize("id_user", [1, 2, 3])
def test_get_all_users(api_client, id_user):
    response = api_client.get("/users/{}".format(id_user))
    assert response.status_code == 200
    jsonschema.validate(response.json(), schema_user)


@pytest.mark.parametrize("id_post", [1, 2, 3])
def test_get_posts_by_id(api_client, id_post):
    response = api_client.get("/posts".format(id_post))
    assert response.status_code == 200


def test_create_post(api_client):
    response = api_client.post("/posts", params=data_post)
    assert response.status_code == 201


def test_delete_post(api_client):
    response = api_client.delete("/posts/1", params=data_post)
    assert response.status_code == 200
    assert response.json() == {}
