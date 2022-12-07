# refact

import json
import os

from todo_py.models.task import Task

PATH = 'eggs/todo-py-{user}-tasks.json'
os.makedirs(os.path.dirname(PATH), exist_ok=True)


def save(tasks, user):
    with open(PATH.format(user=user.username), 'w', encoding='utf-8') as file:
        json.dump(tasks, file,
                  default=lambda o: o.__dict__,
                  sort_keys=True,
                  indent=4)


def load(user):
    tasks = []

    try:
        with open(PATH.format(user=user.username), encoding='utf-8') as json_file:
            raw = json.load(json_file)

            if isinstance(raw, list):
                tasks = list(map(Task.from_dict, raw))

    except (FileNotFoundError, json.JSONDecodeError):
        with open(PATH.format(user=user.username), 'w', encoding='utf-8') as json_file:
            json.dump([], json_file)

    return tasks


def add(task, user):
    tasks = load(user)

    tasks.append(task)

    return save(tasks, user)


def get_all(user):
    return load(user)


def get_by_id(task_id, user) -> Task | None:
    tasks = load(user)
    return next((task for task in tasks if task.id == task_id), None)


def update(task, user):
    tasks = load(user)

    for i, t in enumerate(tasks):
        if t.id == task.id:
            tasks[i] = task
            break

    return save(tasks, user)


def delete(task, user):
    tasks = load(user)

    for i, t in enumerate(tasks):
        if t.id == task.id:
            del tasks[i]
            break

    return save(tasks, user)
