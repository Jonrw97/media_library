import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from plex.db import get_db

bp = Blueprint('movies', __name__, url_prefix='/movies')

@bp.route('/library')
def library():

    db = get_db()
    return render_template('movies/library.html')