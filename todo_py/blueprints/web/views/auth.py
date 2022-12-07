from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from todo_py.repositories import user_repo

from todo_py.models.user import User

TEMPLATE_SUB_FOLDER = '/auth/'
auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if not current_user.is_authenticated:  # type: ignore
        if request.method == 'GET':
            return render_template(TEMPLATE_SUB_FOLDER + 'register.html')

        username = request.form['username']

        if user_repo.get_by_username(username):
            flash('Username already taken')
            return redirect(request.url)

        password = generate_password_hash(request.form['password'])

        new_user = User(username, password)

        user_repo.add(new_user)

        login_user(new_user, remember=True)

    return redirect(url_for('web.main.home'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if not current_user.is_authenticated:  # type: ignore

        if request.method == 'GET':
            return render_template(TEMPLATE_SUB_FOLDER + 'login.html')

        username = request.form['username']
        password = request.form['password']

        user = user_repo.get_by_username(username)

        if not user:
            flash('No user found')
            return redirect(request.url)

        if not check_password_hash(user.password, password):
            flash('Wrong password')
            return redirect(request.url)

        login_user(user, remember=True)

    return redirect(url_for('web.main.home'))


@auth.route('/logout')
def logout():
    logout_user()

    return redirect(url_for('web.auth.login'))
