import requests


class Blog:
    def __init__(self, name):
        self.name = name

    def posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")

        return response.json()

    def users(self):
        response = requests.get("https://jsonplaceholder.typicode.com/users/1")
        return response.json()

    def create_user(self):
        response = requests.post("https://jsonplaceholder.typicode.com/users/1", data={
            "id": 101,
            "title": "foo",
            "body": "bar",
            "userId": 1
        })
        return response.status_code

    def __repr__(self):
        return '<Blog: {}>'.format(self.name)
