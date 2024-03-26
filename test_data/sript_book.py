import json
import csv


with open('books.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    books = [row for row in reader]

with open('users.json', 'r') as jsonfile:
    users = json.load(jsonfile)


books_per_user = len(books) // len(users)
remaining_books = len(books) % len(users)

for user in users:
    user['books'] = [books.pop(0) for _ in range(books_per_user)]
    if remaining_books > 0:
        user['books'].append(books.pop(0))
        remaining_books -= 1


with open('result.json', 'w') as jsonfile:
    json.dump(users, jsonfile)