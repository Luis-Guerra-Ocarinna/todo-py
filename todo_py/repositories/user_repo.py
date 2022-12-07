import json

from todo_py.models.user import User

PATH = 'todo-py-users.json'


def save(user):
    pass


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
    pass


def get_by_username(username):
    users = load()
    return next((user for user in users if user.username == username), None)


def update(user):
    pass


def delete(user):
    pass
