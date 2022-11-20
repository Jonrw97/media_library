import functools
import mimetypes
import os
from os import path
from wsgiref import validate

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from wtforms import (
    FieldList,
    FormField,
    HiddenField,
    StringField,
    SelectField,
    TextAreaField,
)
from wtforms.validators import DataRequired

import plex.file_media_service as file_media_service
import plex.movies_das as movies_das
from plex.auth import login_required
from plex.db import get_db

bp = Blueprint("movies", __name__)


class ActorForm(FlaskForm):
    actor_name = StringField("Name")
    character = StringField("Character")
    actor_id = HiddenField("id")
    new_name = StringField("New Name")
    new_character = StringField("New Character")


class MovieForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    year = StringField("Year", validators=[DataRequired()])
    director = StringField("Director", validators=[DataRequired()])
    file = FileField(validators=[FileRequired()])
    movie_type = SelectField(label="Movie Type", choices=["portfolio", "other"])
    location = StringField("Location", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])

    actorsfields = FieldList(FormField((ActorForm)))


@bp.route("/")
def landing():

    media = movies_das.get_portfolio()
    media1 = media[0]
    media2 = media[1]
    media3 = media[2]
    return render_template(
        "portfolio/landing.html", media1=media1, media2=media2, media3=media3
    )


@bp.route("/library")
@login_required
def library():

    media = movies_das.list_all_movies()
    return render_template("movies/library.html", media=media)


@bp.route("/add_movie", methods=("GET", "POST"))
@login_required
def add_movie():
    movie_form = MovieForm()
    if request.method == "POST":
        result, error, mime_type, file_name = file_media_service.save_file(
            movie_form.file.data
        )
        if result == 0:
            result, error, id = movies_das.add_movie(
                movie_form.movie_title.data,
                movie_form.year.data,
                movie_form.director.data,
                file_name,
                mime_type,
                movie_form.movie_type.data,
            )

        flash(error)
        return redirect(url_for("library"))
    else:
        return render_template("movies/add_movie.html", movie_form=movie_form)


@bp.route("/details_view")
@login_required
def details_view():
    if request.method == "GET":
        id = request.args["id"]
        details_movies, details_actors = movies_das.get_movie_with_actors(id)

        return render_template(
            "movies/details_view.html",
            details_movies=details_movies,
            details_actors=details_actors,
        )

    if request.method == "POST":
        return render_template(
            "movies/details_view.html",
            details_movies=details_movies,
            details_actors=details_actors,
        )


@bp.route("/edit_view", methods=("GET", "POST"))
@login_required
def edit_view():
    movie_form = MovieForm()
    actor_form = ActorForm()
    if request.method == "GET":
        id = request.args["id"]
        details_movies, details_actors = movies_das.get_movie_with_actors(id)
        for actor in details_actors:
            movie_form.actorsfields.append_entry(ActorForm(actor))

    elif request.method == "POST":
        update_movie = 0
        id = request.args["id"]
        details_movies, details_actors = movies_das.get_movie_with_actors(id)

        if details_movies[4] == "portfolio":
            result, error, id = movies_das.update_movie(
                id,
                movie_form.movie_title.data,
                movie_form.year.data,
                movie_form.director.data,
                movie_form.movie_type.data,
                movie_form.location.data,
                movie_form.description.data,
            )

        for actorform in movie_form.actorsfields:

            if not actorform.actor_name.data and not actorform.character.data:
                result, error = movies_das.delete_actor(
                    actorform.actor_id.data, actorform.actor_name.data
                )

            else:
                result, error, id = movies_das.update_movie_with_actors(
                    id,
                    movie_form.movie_title.data,
                    movie_form.year.data,
                    movie_form.director.data,
                    movie_form.movie_type.data,
                    actorform.actor_name.data,
                    actorform.character.data,
                    actorform.actor_id.data,
                )

        if actor_form.new_name.data and actor_form.new_character.data:
            result, error, id = movies_das.add_actor(
                actor_form.new_name.data, actor_form.new_character.data, id
            )

        flash(error)
        return redirect(url_for("library"))

    return render_template(
        "movies/edit_view.html",
        details_movies=details_movies,
        details_actors=details_actors,
        movie_form=movie_form,
        actor_form=actor_form,
    )


# update_post


@bp.route("/video_player")
@login_required
def video_player():

    if request.method == "GET":
        id = request.args["id"]
        media = movies_das.get_file(id)
        print(media[1], media[2])
        return render_template("movies/video_player.html", media=media)

    if request.method == "POST":

        return render_template("movies/video_player.html", media=media)
