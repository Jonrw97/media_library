import functools
import mimetypes
import os
from os import path

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from plex.auth import login_required
from plex.db import get_db

bp = Blueprint('movies', __name__)


@bp.route('/')
@login_required
def library():

    db = get_db()
    cur = db.cursor()
    media = cur.execute("""SELECT movies.id, movies.movie_title, movies.year, movies.director, 
                            actors.id, actors.name, actors.character, actors.movie_id 
                            FROM movies, actors WHERE movies.id = actors.movie_id""").fetchall()
    return render_template('movies/library.html', media_movies=media)


@bp.route('/add_movie', methods=('GET', 'POST'))
@login_required
def add_movie():

    if request.method == 'POST':

        db = get_db()
        error = None
        movie_title = request.form['movie_title']
        year = request.form['year']
        director = request.form['director']
        f = request.files['myfile']
        f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
               'static/sync', secure_filename(f.filename)))
        file_name = f.filename
        mime_tuple = mimetypes.guess_type(file_name)
        mime_type, mime_encoding = mime_tuple

        if error is None:

            try:
                db.execute(
                    "INSERT INTO movies (movie_title, year, director, file_name, mime_type) VALUES (?, ?, ?, ?, ?, ?)",
                    (movie_title, year, director, file_name, mime_type),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {movie_title} is already added to the libary."

            return redirect(url_for('library'))

        flash(error)
        return redirect(url_for('library'))

    else:
        return render_template('movies/add_movie.html')


@bp.route('/details_view')
@login_required
def details_view():
    if request.method == 'GET':
        db = get_db()
        id = request.args['id']
        details_movies = db.execute(
            "SELECT id, movie_title, year, director, file_name FROM movies where id = ?", id).fetchone()
        details_actors = db.execute(
            "SELECT id, name, character, movie_id FROM actors WHERE movie_id = ?", id).fetchall()
        return render_template('movies/details_view.html', details_movies=details_movies, details_actors=details_actors)

    if request.method == 'POST':
        return render_template('movies/details_view.html', details_movies=details_movies, details_actors=details_actors)


@bp.route('/edit_view', methods=('GET', 'POST'))
@login_required
def edit_view():
    db = get_db()
    if request.method == 'GET':
        id = request.args['id']
        details = db.execute(
            "SELECT id, movie_title, year, director, file_name FROM movies WHERE movies.id = ? ", id).fetchone()
        actor_details = db.execute(
            "SELECT id, name, character, movie_id FROM actors WHERE movie_id = ?", id)

    elif request.method == 'POST':
        print(request.form)
        error = None
        id = request.args['id']
        movie_title = request.form['movie_title']
        year = request.form['year']
        director = request.form['director']
        actor_details = db.execute(
            "SELECT id, name, character, movie_id FROM actors WHERE movie_id = ?", id)

        movie_id = request.args['id']
        f = request.files['myfile']
        f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
               'static/sync', secure_filename(f.filename)))
        file_name = f.filename
        mime_tuple = mimetypes.guess_type(file_name)
        mime_type, mime_encoding = mime_tuple

        try:
            edit = db.execute(
                "UPDATE movies SET movie_title=?, year=?, director=?, file_name=?, mime_type=? WHERE id=?",
                (movie_title, year, director, file_name, mime_type, id))
            for actor in actor_details:
                name = request.form[f'name{actor[0]}']
                character = request.form[f'character{actor[0]}']
                edit_actors = db.execute(
                    "UPDATE actors SET name=?, character=? WHERE id = ?",
                    (name, character, actor[0]))
            new_name = request.form['name-new']
            new_character = request.form['character-new']
            if new_name and new_character:
                db.execute("INSERT INTO actors (name, character, movie_id) VALUES (?,?,?)",(new_name, new_character, id))
            db.commit()
        except Exception as e:
            print(e)
            flash("update failed")
        else:
            flash("update succseful")
        finally:
            flash
            return redirect(url_for('library'))

    return render_template('movies/edit_view.html', details=details, actor_details=actor_details)


@bp.route('/video_player')
@login_required
def video_player():

    if request.method == 'GET':
        db = get_db()
        file_name = request.args['file_name']
        print("video_player", file_name)
        return render_template('movies/video_player.html', file_name=file_name)

    if request.method == 'POST':

        return render_template('movies/video_player.html', file_name=file_name)
