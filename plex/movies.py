import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from plex.auth import login_required
from plex.db import get_db

bp = Blueprint('movies', __name__)

@bp.route('/')
@login_required
def library():

    db = get_db()
    cur = db.cursor()
    media = cur.execute("SELECT id, movie_title, year, director, actor FROM movies").fetchall()
    return render_template('movies/library.html', media = media)

@bp.route('/add_movie', methods=('GET', 'POST'))
@login_required
def add_movie():

    if request.method == 'POST':
        movie_title = request.form['movie_title']
        year = request.form['year']
        director = request.form['director']
        actor = request.form['actor']
        db = get_db()
        error = None

        if not movie_title:
            error = 'Movie Title is required.'

        else:

            if error is None:
                try:
                    db.execute(
                        "INSERT INTO movies (movie_title, year, director, actor) VALUES (?, ?, ?, ?)",
                        (movie_title, year, director, actor),
                    )
                    db.commit()
                except db.IntegrityError:
                    error = f"User {movie_title} is already added to the libary."
                    
                return redirect(url_for('library'))

        flash(error)
    else:
        return render_template('movies/add_movie.html')

@bp.route('/details_view')
@login_required

def details_view():
    db = get_db()
    movie_id = request.args['id']
    details = db.execute("SELECT id, movie_title, year, director, actor FROM movies where id = ?", movie_id).fetchone()
    return render_template('movies/details_view.html', details = details)

@bp.route('/edit_view')
@login_required

def edit_view():    
    if request.method == 'GET':
        db = get_db()
        movie_id = request.args['id']
        details = db.execute("SELECT movie_title, year, director, actor FROM movies where id = ?", movie_id).fetchone()

    
    elif request.method == 'POST':
        movie_title = request.form['movie_title']
        year = request.form['year']
        director = request.form['director']
        actor = request.form['actor']
        #db = get_db()
        #movie_id = request.args['id']
        #details = db.execute("SELECT movie_title, year, director, actor FROM movies where id = ?", movie_id).fetchone()
        try:
            edit = db.execute(
                "INSERT OR REPLACE INTO movies (movie_title, year, director, actor) VALUES(?,?,?,?)",
                (movie_title, year, director, actor))
        except:
            flash("update failed")
            return redirect(url_for('library'))
        flash("update succseful")
    return render_template('movies/edit_view.html', details = details)


