from flask import Blueprint, abort, redirect, render_template, request, url_for
from todo_py.models.task import Task

from todo_py.repositories import user_repo, task_repo

TEMPLATE_SUB_FOLDER = '/main/'
main = Blueprint('main', __name__)

user = user_repo.get_by_username('admin')


@main.route('/')
def home():
    tasks = task_repo.get_all(user)

    ctx = {
        'tasks': tasks,
    }
    return render_template(f'{TEMPLATE_SUB_FOLDER}index.html', **ctx)


@main.route('/add', methods=['POST'])
def create():
    title = request.form['title']
    description = request.form.get('description', None)

    task = Task(title, description)

    task_repo.add(task, user)

    return redirect(url_for('web.main.home'))


@main.route('/update/<int:item_id>', methods=['POST'])
def update(item_id):
    task = task_repo.get_by_id(item_id, user) or abort(404)

    task.title = request.form['title']
    task.description = request.form.get('description', None)
    task.done = 'done' in request.form

    task_repo.update(task, user)

    return redirect(url_for('web.main.home'))


@main.route('/delete/<int:item_id>', methods=['GET'])
def delete(item_id):
    task = task_repo.get_by_id(item_id, user) or abort(404)

    task_repo.delete(task, user)

    return redirect(url_for('web.main.home'))
