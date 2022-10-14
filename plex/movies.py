import functools
import mimetypes
import os
from os import path
from wsgiref import validate

from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from wtforms import FieldList, FormField, HiddenField, StringField
from wtforms.validators import DataRequired

import plex.file_media_service as file_media_service
import plex.movies_das as movies_das
from plex.auth import login_required
from plex.db import get_db

bp = Blueprint('movies', __name__)


class AddMovieForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    year = StringField("Year", validators=[DataRequired()])
    director = StringField("Director", validators=[DataRequired()])
    file = FileField(validators=[FileRequired()])


class ActorForm(FlaskForm):
    actor_name = StringField("Name")
    character = StringField("Character")
    actor_id = HiddenField("id")


class EditMovieForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    year = StringField("Year", validators=[DataRequired()])
    director = StringField("Director", validators=[DataRequired()])
    actorsfields = FieldList(FormField((ActorForm)))
    new_name = StringField("New Name")
    new_character = StringField("New Character")


@bp.route('/')
@login_required
def library():

    media = movies_das.list_all_movies()
    return render_template('movies/library.html', media=media)


@bp.route('/add_movie', methods=('GET', 'POST'))
@login_required
def add_movie():
    form = AddMovieForm()
    if request.method == 'POST':
        result, error, mime_type, file_name = file_media_service.save_file(
            form.file.data)

        if result == 0:
            result, error, id = movies_das.add_movie(
                form.movie_title.data, form.year.data, form.director.data, file_name, mime_type)

        flash(error)
        return redirect(url_for('library'))
    else:
        return render_template('movies/add_movie.html', form=form)


@bp.route('/details_view')
@login_required
def details_view():
    if request.method == 'GET':
        id = request.args['id']
        details_movies, details_actors = movies_das.get_movie_with_actors(id)

        return render_template('movies/details_view.html', details_movies=details_movies, details_actors=details_actors)

    if request.method == 'POST':
        return render_template('movies/details_view.html', details_movies=details_movies, details_actors=details_actors)


@bp.route('/edit_view', methods=('GET', 'POST'))
@login_required
def edit_view():
    form = EditMovieForm()
    if request.method == 'GET':
        id = request.args['id']
        details_movies, details_actors = movies_das.get_movie_with_actors(id)
        for actor in details_actors:
            form.actorsfields.append_entry(ActorForm(actor))

    elif request.method == 'POST':
        update_movie = 0
        id = request.args['id']
        details_movies, details_actors = movies_das.get_movie_with_actors(id)

        for actorform in form.actorsfields:
            #name = request.form[f'name{actor[0]}']
            #character = request.form[f'character{actor[0]}']
            actor_id = actor[0]
            if not form.name.data and not form.character.data:
                result, error = movies_das.delete_actor(actor_id)

            else:
                result, error, id = movies_das.update_movie_with_actors(
                    update_movie, id, form.movie_title.data, form.year.data,
                    form.director.data, form.name.data, form.character.data, actor[0])

        if form.new_name.data and form.new_character.data:
            result, error, id = movies_das.add_actor(
                form.new_name.data, form.new_character.data, id)

        flash(error)
        return redirect(url_for('library'))

    return render_template('movies/edit_view.html', details_movies=details_movies, details_actors=details_actors, form=form)

# update_post


@bp.route('/video_player')
@login_required
def video_player():

    if request.method == 'GET':
        file_name = request.args['file_name']
        print("video_player", file_name)
        return render_template('movies/video_player.html', file_name=file_name)

    if request.method == 'POST':

        return render_template('movies/video_player.html', file_name=file_name)
