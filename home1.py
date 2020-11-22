from csv import DictReader
from json import loads, dumps

list_of_books = []
users = []
with open('books.csv') as f:
    reader = DictReader(f)
    for book in reader:
        list_of_books.append({'title': book['Title'], 'author': book['Author'], 'height': book['Height']})
with open('users.json', 'r') as file:
    j = file.read()
    list_of_users = loads(j)
    for el in list_of_users:
        users.append(
            {'name': el['name'], 'gender': el['gender'], 'address': el['address']})
b = len(users)
if len(users) > 0:
    i = 0
    for user in users:
        try:
            user['books'] = [list_of_books[i]]
        except IndexError:
            user['books'] = []
        b -= 1
        i += 1
with open('new_json.json', 'w') as file:
    s = dumps(users, indent=4)
    file.write(s)
