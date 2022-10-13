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
import plex.movies_das as movies_das
import plex.file_media_service as file_media_service

bp = Blueprint('movies', __name__)


@bp.route('/')
@login_required
def library():

    media = movies_das.list_all_movies()
    return render_template('movies/library.html', media=media)


@bp.route('/add_movie', methods=('GET', 'POST'))
@login_required
def add_movie():

    if request.method == 'POST':

        movie_title = request.form['movie_title']
        year = request.form['year']
        director = request.form['director']
        f = request.files['myfile']

        result, error, mime_type, file_name = file_media_service.save_file(f)

        if result == 0:
            result, error, id = movies_das.add_movie(
                movie_title, year, director, file_name, mime_type)

        flash(error)
        return redirect(url_for('library'))
    else:
        return render_template('movies/add_movie.html')


@bp.route('/details_view')
@login_required
def details_view():
    if request.method == 'GET':
        id = request.args['id']
        details_movies = movies_das.get_movie(id)
        details_actors = movies_das.get_actors_for_movie(id)

        return render_template('movies/details_view.html', details_movies=details_movies, details_actors=details_actors)

    if request.method == 'POST':
        return render_template('movies/details_view.html', details_movies=details_movies, details_actors=details_actors)


@bp.route('/edit_view', methods=('GET', 'POST'))
@login_required
def edit_view():
    db = get_db()
    if request.method == 'GET':
        id = request.args['id']
        details_movies = movies_das.get_movie(id)
        details_actors = movies_das.get_actors_for_movie(id)

    elif request.method == 'POST':
        error = None
        result = 0
        id = request.args['id']
        movie_title = request.form['movie_title']
        year = request.form['year']
        director = request.form['director']
        details_actors = movies_das.get_actors_for_movie(id)
        result, error, id = movies_das.update_movie(
            id, movie_title, year, director)
        if result == 1:
            flash(error)
            return redirect(url_for('library'))

        for actor in details_actors:
            name = request.form[f'name{actor[0]}']
            character = request.form[f'character{actor[0]}']
            actor_id = actor[0]
            if not name:
                result, error = movies_das.delete_actor(actor_id)

            result, error, id = movies_das.update_actor(
                name, character, actor[0])
            print(f"Update {actor[0]}")

        new_name = request.form['name-new']
        new_character = request.form['character-new']
        if new_name and new_character:
            result, error, id = movies_das.add_actor(
                new_name, new_character, id)

        flash(error)
        return redirect(url_for('library'))

    return render_template('movies/edit_view.html', details_movies=details_movies, details_actors=details_actors)


@bp.route('/video_player')
@login_required
def video_player():

    if request.method == 'GET':
        file_name = request.args['file_name']
        print("video_player", file_name)
        return render_template('movies/video_player.html', file_name=file_name)

    if request.method == 'POST':

        return render_template('movies/video_player.html', file_name=file_name)
