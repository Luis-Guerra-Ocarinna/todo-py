from flask import Blueprint, abort, redirect, render_template, request, url_for
from flask_login import current_user

from todo_py.models.task import Task
from todo_py.repositories import task_repo

TEMPLATE_SUB_FOLDER = '/main/'
main = Blueprint('main', __name__)


@main.before_request
def check_route_access():
    if not current_user.is_authenticated:  # type: ignore
        return redirect(url_for('web.auth.login'))
    return None


@main.route('/')
def home():
    tasks = task_repo.get_all(current_user)

    ctx = {
        'tasks': tasks,
    }
    return render_template(f'{TEMPLATE_SUB_FOLDER}index.html', **ctx)


@main.route('/add', methods=['POST'])
def create():
    title = request.form['title']
    description = request.form.get('description', None)

    task = Task(title, description)

    task_repo.add(task, current_user)

    return redirect(url_for('web.main.home'))


@main.route('/update/<int:item_id>', methods=['POST'])
def update(item_id):
    task = task_repo.get_by_id(item_id, current_user) or abort(404)

    task.title = request.form['title']
    task.description = request.form.get('description', None)
    task.done = 'done' in request.form

    task_repo.update(task, current_user)

    return redirect(url_for('web.main.home'))


@main.route('/delete/<int:item_id>', methods=['GET'])
def delete(item_id):
    task = task_repo.get_by_id(item_id, current_user) or abort(404)

    task_repo.delete(task, current_user)

    return redirect(url_for('web.main.home'))
