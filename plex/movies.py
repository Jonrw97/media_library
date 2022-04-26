import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from plex.db import get_db

bp = Blueprint('movies', __name__, url_prefix='/movies')

@bp.route('/library')
def library():

    db = get_db()
    cur = db.cursor()
    media = cur.execute("SELECT * FROM movies").fetchall()
    
    for row in media:
        print("<<<<<<media", row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])
        print("details")


    return render_template('movies/library.html')