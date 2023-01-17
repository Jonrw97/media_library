import mimetypes
from plex.db import get_db


def add_actor(new_name, new_character, movie_id):
    db, cur = get_db()
    result = 0
    error = None
    try:
        cur.execute(
            "INSERT INTO actors (name, character, movie_id) VALUES (%s, %s, %s)",
            (new_name, new_character, movie_id),
        )
        db.commit()
        cur.close()
        db.close()
    except db.IntegrityError:
        error = f"Fail: Actor could not be added."
        result = 1
    # except:

    finally:
        error = "Actor added."
        result = 0
    return result, error, movie_id


def add_movie(movie_title, year, director, file_name, movie_type, publish, featured):
    mime_tuple = mimetypes.guess_type(file_name)
    mime_type, mime_encoding = mime_tuple
    db, cur = get_db()
    result = 0
    error = None
    try:
        cur.execute(
            "INSERT INTO movies (movie_title, year, director, file_name, mime_type, movie_type, publish, featured) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (
                movie_title,
                year,
                director,
                file_name,
                mime_type,
                movie_type,
                publish,
                featured,
            ),
        )
        db.commit()
        cur.close()
        db.close()
    except db.IntegrityError:
        error = f"Failed:{movie_title} could not be added to the library."
        result = 1
    else:
        error = f"{movie_title} added to libary."

    return result, error, id


def delete_actor(actor_id, name):
    db, cur = get_db()
    result = 0
    error = None
    try:
        cur.execute("DELETE FROM actors WHERE id=%s", (actor_id,))
        db.commit()
    except db.IntegrityError:
        error = f"Fail: Actor {name} could not be deleted."
        result = 1
    else:
        error = f"Actor {name} removed succesfully"
        return result, error


def get_actors_for_movie(movie_id):

    db, cur = get_db()
    cur.execute(
        "SELECT id, name, character, movie_id FROM actors WHERE movie_id = %s",
        (movie_id,)
    )
    details_actors = cur.fetchall()
    return details_actors


def get_file(movie_id):

    db, cur = get_db()
    cur.execute(
        "SELECT id, file_name, movie_type FROM movies where id =  %s",
        (movie_id,)
    )
    details_movies = cur.fetchone()
    return details_movies


def get_movie(movie_id):

    db, cur = get_db()
    cur.execute(
        "SELECT id, movie_title, year, director, file_name FROM movies where id =  %s",
        (movie_id,)
    )
    details_movies = cur.fetchone()
    return details_movies


def get_movie_with_actors(movie_id):
    db, cur = get_db()

    cur.execute(
        "SELECT id, name, character, movie_id FROM actors WHERE movie_id =  %s",
        (movie_id,)
    )
    details_actors = cur.fetchall()

    cur.execute(
        "SELECT id, movie_title, year, director, movie_type, location, description FROM movies where id =  %s",
        (movie_id,)
    )
    details_movies = cur.fetchone()

    return details_movies, details_actors


def get_portfolio():
    db, cur = get_db()
    cur.execute(
        """SELECT movie_title, file_name, location, description FROM movies where publish = '1' AND featured = '0' ORDER by year;"""
    )
    details_movies = cur.fetchall()

    cur.execute(
        """SELECT movie_title, file_name, location, description FROM movies where publish = '1' AND featured = '1';"""
    )
    f_movies = cur.fetchall()

    return details_movies, f_movies


def list_all_movies():
    db, cur = get_db()
    cur.execute(
        """SELECT id, movie_title, year, director FROM movies ORDER BY id"""
    )
    media = cur.fetchall()
    return media


def update_actor(name, character, id):
    db, cur = get_db()
    result = 0
    error = None
    try:
        cur.execute(
            "UPDATE actors SET name=%s, character=%s WHERE id = %s",
            (name, character, id),
        )
        db.commit()
    except db.IntegrityError:
        error = "Fail: actors update unsuccessful."
        result = 1
    else:
        error = "Actors update successful."

    return result, error, id


def update_movie(
    id,
    movie_title,
    year,
    director,
    movie_type,
    location,
    description,
    publish,
    featured,
):
    db, cur = get_db()
    result = 0
    error = None
    try:
        cur.execute(
            "UPDATE movies SET movie_title=%s, year=%s, director=%s, movie_type=%s, location=%s, description=%s, publish=%s, featured=%s WHERE id=%s",
            (
                movie_title,
                year,
                director,
                movie_type,
                location,
                description,
                publish,
                featured,
                id,
            ),
        )
        db.commit()
    except db.IntegrityError:
        error = f"Fail: {movie_title} updated unsuccessful."
        result = 1
    else:
        error = f"{movie_title} updated successful."

    return result, error, id


def update_movie_with_actors(
    id,
    movie_title,
    year,
    director,
    movie_type,
    publish,
    featured,
    name,
    character,
    actor,
):
    db, cur = get_db()
    result = 0
    error = None
    try:
        cur.execute(
            "UPDATE actors SET name=%s, character=%s, movie_id=%s WHERE id = %s",
            (name, character, id, actor),
        )
    except db.IntegrityError:
        error = f"Fail: actor{actor} update unsuccessful."
        result = 1
        result, error, id
    else:
        error = f"{movie_title} and its Actors updated successfully."

    try:
        cur.execute(
            "UPDATE movies SET movie_title=%s, year=%s, director=%s, movie_type=%s, publish=%s, featured=%s WHERE id=%s",
            (movie_title, year, director, movie_type, publish, featured, id),
        )
    except db.IntegrityError:
        error = f"Fail: {movie_title} update unsuccessful."
        result = 1
    else:
        error = f"{movie_title} update successful."
    db.commit()
    return result, error, id
