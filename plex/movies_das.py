from plex.db import get_db

# ====================================================================================================================
# Part 1
# ====================================================================================================================


def list_all_movies():
    return []


def get_movie(movie_id):
    return None


def add_movie(movie_title, year, director, file_name, mime_type):
    db = get_db()

    error = None
    result = 0
    try:
        db.execute(
            "INSERT INTO movies (movie_title, year, director, file_name, mime_type) VALUES (?, ?, ?, ?, ?, ?)",
            (movie_title, year, director, file_name, mime_type),
        )
        db.commit()
    except db.IntegrityError:
        error = f"User {movie_title} is already added to the library."
        result = 1

    return result, error, movie_id # return movie_id that was just inserted


def update_movie(movie_id, movie_title, year, director, file_name, mime_type):
    db = get_db()

    # Stuff happens

    db.commit()
    return None


def get_actors_for_movie(movie_id):
    return []


def update_actor(actor_id, name, character):
    db = get_db()

    # Stuff happens

    db.commit()
    return None


def delete_actor(actor_id):
    return None


# ====================================================================================================================
# Part 2
# ====================================================================================================================

def get_movie_with_actors(movie_id):
    return None


def update_movie_with_actors(movie_id):
    return None
