from plex.db import get_db

# ====================================================================================================================
# Part 1
# ====================================================================================================================


def list_all_movies():

    db = get_db()
    cur = db.cursor()
    media = cur.execute(
        """SELECT id, movie_title, year, director FROM movies""").fetchall()
    return media


def get_movie(movie_id):
    db = get_db()
    id = movie_id
    details_movies = db.execute(
        "SELECT id, movie_title, year, director, file_name FROM movies where id = ?", id).fetchone()
    return details_movies


def add_movie(movie_title, year, director, file_name, mime_type):
    db = get_db()
    result = 0
    error = None
    try:
        db.execute(
            "INSERT INTO movies (movie_title, year, director, file_name, mime_type) VALUES (?, ?, ?, ?, ?)",
            (movie_title, year, director, file_name, mime_type),
        )
        db.commit()
    except db.IntegrityError:
        error = f"Failed:{movie_title} is already added to the library."
        result = 1
    else:
        error = f"{movie_title} added to libary."

    return result, error, id


def update_movie(id, movie_title, year, director):
    db = get_db()
    result = 0
    error = None
    try:
        db.execute("UPDATE movies SET movie_title=?, year=?, director=? WHERE id=?",
                   (movie_title, year, director, id))
        db.commit()
    except db.IntegrityError:
        error = f"Fail: {movie_title} updated unsuccessful."
        result = 1
    else:
        error = f"{movie_title} updated successful."

    return result, error, id


def get_actors_for_movie(movie_id):
    db = get_db()
    id = movie_id
    details_actors = db.execute(
        "SELECT id, name, character, movie_id FROM actors WHERE movie_id = ?", id).fetchall()
    return details_actors


def add_actor(new_name, new_character, movie_id):
    db = get_db()
    result = 0
    error = None
    try:
        db.execute("INSERT INTO actors (name, character, movie_id) VALUES (?,?,?)",
                   (new_name, new_character, movie_id))
        db.commit()
    except db.IntegrityError:
        error = f"Fail: Actor could not be added."
        result = 1
    else:
        error = "Actor added."
        result = 0
    return result, error, movie_id


def update_actor(name, character, actor):
    db = get_db()
    result = 0
    error = None
    try:
        db.execute("UPDATE actors SET name=?, character=? WHERE id = ?",
                   (name, character, actor))
        db.commit()
    except db.IntegrityError:
        error = "Fail: actors update unsuccessful."
        result = 1
    else:
        error = "Actors update successful."

    return result, error, actor


def delete_actor(actor_id):
    db = get_db()
    result = 0
    error = None
    try:
        db.execute("DELETE FROM actors WHERE id=?", (actor_id,))
        db.commit()
    except db.IntegrityError:
        error = f"Fail: actor{actor_id} could not be deleted."
        result = 1
    else:
        error = f"Actor{actor_id} removed succesfully"
        return result, error


# ====================================================================================================================
# Part 2
# ====================================================================================================================

def get_movie_with_actors(movie_id):
    db = get_db()
    id = movie_id
    details_movies = db.execute(
        "SELECT id, movie_title, year, director, file_name FROM movies where id = ?", id).fetchone()
    details_actors = db.execute(
        "SELECT id, name, character, movie_id FROM actors WHERE movie_id = ?", id).fetchall()
    return details_movies, details_actors


def update_movie_with_actors(update_movie, id, movie_title, year, director, name, character, actor):
    db = get_db()
    result = 0
    error = None
    try:
        db.execute("UPDATE actors SET name=?, character=? WHERE id = ?",
                   (name, character, actor))
    except db.IntegrityError:
        error = f"Fail: actor{actor} update unsuccessful."
        result = 1
    else:
        error = f"{movie_title} and its Actors updated successfully."

    if update_movie == result and result == 0:
        try:
            db.execute("UPDATE movies SET movie_title=?, year=?, director=? WHERE id=?",
                       (movie_title, year, director, id))
        except db.IntegrityError:
            error = f"Fail: {movie_title} update unsuccessful."
            result = 1
        else:
            error = f"{movie_title} update successful."
    db.commit()
    return result, error, id
