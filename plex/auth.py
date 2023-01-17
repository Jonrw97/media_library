import functools

from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from plex.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, cur = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                cur.execute(
                    "INSERT INTO user_account (user_name, password) VALUES (%s, %s);",
                    (username, generate_password_hash(password)))
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))
        flash(error)
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, cur = get_db()
        error = None
        cur.execute(
            'SELECT * FROM user_account WHERE user_name = %s', (username,)
        )
        user = cur.fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user[2], password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = user[0]
            return redirect(url_for('library'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    db, cur = get_db()
    if user_id is None:
        g.user = None
    else:
        cur.execute(
            'SELECT * FROM user_account WHERE id = %s', (user_id,)
        )
        g.user = cur.fetchone()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('movies.landing'))

        return view(**kwargs)

    return wrapped_view


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('library'))
