import functools, mimetypes, os
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
    media = cur.execute("SELECT id, movie_title, year, director, actor FROM movies").fetchall()
    return render_template('movies/library.html', media = media)

@bp.route('/add_movie', methods=('GET', 'POST'))
@login_required
def add_movie():

    if request.method == 'POST':

        db = get_db()
        error = None
        movie_title = request.form['movie_title']
        year = request.form['year']
        director = request.form['director']
        actor = request.form['actor']
        f = request.files['myfile']
        f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),'static/sync',secure_filename(f.filename)))
        file_name = f.filename
        mime_tuple = mimetypes.guess_type(file_name)
        mime_type, mime_encoding = mime_tuple
       
        if path.exists(f'static/sync/{file_name}'):  
            error = "Upload Fail: File already exists"
        

        if error is None:

            try:
                db.execute(
                    "INSERT INTO movies (movie_title, year, director, actor, file_name, mime_type) VALUES (?, ?, ?, ?, ?, ?)",
                    (movie_title, year, director, actor, file_name, mime_type),
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
        movie_id = request.args['id']
        details = db.execute("SELECT id, movie_title, year, director, actor, file_name FROM movies where id = ?", movie_id).fetchone()
        print("details", details[5])
        return render_template('movies/details_view.html', details = details)

    if request.method == 'POST':
        return render_template('movies/details_view.html', details = details)

@bp.route('/edit_view', methods=('GET', 'POST'))
@login_required
def edit_view(): 
    db = get_db()  
    if request.method == 'GET':
        movie_id = request.args['id']
        details = db.execute("SELECT id, movie_title, year, director, actor, file_name FROM movies WHERE id = ?", movie_id).fetchone()

    
    elif request.method == 'POST':
        error = None
        movie_id = request.args['id']
        movie_title = request.form['movie_title']
        year = request.form['year']
        director = request.form['director']
        actor = request.form['actor']
        f = request.files['myfile']
        f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),'static/sync',secure_filename(f.filename)))
        file_name = f.filename
        mime_tuple = mimetypes.guess_type(file_name)
        mime_type, mime_encoding = mime_tuple

        #if path.exists(f'static/sync/{file_name}'):  
            #flash("Upload Fail: File already exists")
            #return redirect(url_for('library'))

        try:
            edit = db.execute(
                "UPDATE movies SET movie_title=?, year=?, director=?, actor=?, file_name=?, mime_type=? WHERE id=?",
                (movie_title, year, director, actor, file_name, mime_type, movie_id))
            db.commit()
        except Exception:
            flash("update failed")
        else:
            flash("update succseful")
        finally:
            flash
            return redirect(url_for('library'))

    return render_template('movies/edit_view.html', details = details)

@bp.route('/video_player')
@login_required
def video_player():

    if request.method == 'GET':
        db = get_db()
        file_name = request.args['file_name']
        print("video_player", file_name)
        return render_template('movies/video_player.html', file_name = file_name)

    if request.method == 'POST':

        return render_template('movies/video_player.html', file_name = file_name)



