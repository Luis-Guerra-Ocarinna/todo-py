import json
import os

from todo_py.models.user import User

PATH = 'eggs/todo-py-users.json'
os.makedirs(os.path.dirname(PATH), exist_ok=True)


def save(users):
    with open(PATH, 'w', encoding='utf-8') as file:
        json.dump(users, file,
                  default=lambda o: o.__dict__,
                  sort_keys=True,
                  indent=4)


def load():
    users = []

    try:
        with open(PATH, encoding='utf-8') as json_file:
            raw = json.load(json_file)

            if isinstance(raw, list):
                users = list(map(User.from_dict, raw))

    except (FileNotFoundError, json.JSONDecodeError):
        with open(PATH, 'w', encoding='utf-8') as json_file:
            json.dump([], json_file)

    return users


def add(user):
    users = load()

    users.append(user)

    return save(users)


def get_by_username(username):
    users = load()
    return next((user for user in users if user.username == username), None)


def update(user):
    pass


def delete(user):
    pass
