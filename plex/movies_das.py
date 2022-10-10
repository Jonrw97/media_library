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

    error = None
    try:
        db.execute(
            "INSERT INTO movies (movie_title, year, director, file_name, mime_type) VALUES (?, ?, ?, ?, ?)",
            (movie_title, year, director, file_name, mime_type),
        )
        db.commit()
    except db.IntegrityError:
        error = f"Failed:{movie_title} is already added to the library."
    else:
        error = f"{movie_title} added to libary."

    return error, id  # return movie_id that was just inserted


def update_movie(id, movie_title, year, director):
    db = get_db()
    error = None
    try:
        db.execute("UPDATE movies SET movie_title=?, year=?, director=? WHERE id=?",
                   (movie_title, year, director, id))
        db.commit()
    except db.IntegrityError:
        error = f"Fail: {movie_title} updated unsuccessful."
    else:
        error = f"{movie_title} updated successful."

    return error, id


def get_actors_for_movie(movie_id):
    db = get_db()
    id = movie_id
    details_actors = db.execute(
        "SELECT id, name, character, movie_id FROM actors WHERE movie_id = ?", id).fetchall()
    return details_actors


def add_actor(new_name, new_character, movie_id):
    db = get_db()
    error = None
    try:
        db.execute("INSERT INTO actors (name, character, movie_id) VALUES (?,?,?)",
                   (new_name, new_character, movie_id))
        db.commit()
    except db.IntegrityError:
        error = f"Fail: Actor could not be added."
    else:
        error = "Actor added."
    return movie_id, error


def update_actor(name, character, actor):
    db = get_db()
    try:
        db.execute("UPDATE actors SET name=?, character=? WHERE id = ?",
                   (name, character, actor))
        db.commit()
    except db.IntegrityError:
        error = "Fail: actors update unsuccessful."
    else:
        error = "Actors update successful."

    return actor, error


def delete_actor(actor_id):
    db = get_db()
    try:
        db.execute("DELETE FROM actors WHERE id=?", (actor_id))
        db.commit()
    except db.IntegrityError:
        error = f"Fail: actor{actor_id} could not be deleted."
    else:
        error = f"Actor{actor_id} removed succesfully"
        return error


# ====================================================================================================================
# Part 2
# ====================================================================================================================

def get_movie_with_actors(movie_id):
    return None


def update_movie_with_actors(movie_id):
    return None
