import json
from flask import Blueprint, current_app, redirect, render_template, request, url_for

bp = Blueprint('main', __name__)

todos = []


@bp.before_request
def load():
    global todos  # pylint: disable=global-statement,invalid-name

    storage_file = current_app.config['STORAGE_FILE']

    try:
        with open(storage_file, encoding='utf-8') as file:
            todos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(storage_file, 'w', encoding='utf-8') as file:
            json.dump([], file)


@bp.after_request
def save(response):
    with open(current_app.config['STORAGE_FILE'], 'w', encoding='utf-8') as file:
        json.dump(todos, file)
    return response


@bp.route('/')
def home():
    return render_template('index.html', todos=todos)


@bp.route('/add', methods=['POST'])
def create():
    title = request.form['title']
    todos.append({'title': title, 'done': False})
    return redirect(url_for('web.main.home'))


@bp.route('/update/<int:item_id>', methods=['POST'])
def update(item_id):
    todos[item_id]['title'] = request.form['title']
    todos[item_id]['done'] = 'done' in request.form
    return redirect(url_for('web.main.home'))


@bp.route('/delete/<int:item_id>', methods=['GET'])
def delete(item_id):
    del todos[item_id]
    return redirect(url_for('web.main.home'))
