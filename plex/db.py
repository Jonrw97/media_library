import os
import psycopg2

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
        host="/var/run/postgresql",
        database="media_library",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
        
    db = g.db
    cur = db.cursor()

    return g.db, cur


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    conn, cur = get_db()
    with current_app.open_resource('schema.sql') as f:
        cur.execute(f.read().decode('utf8'))

    conn.commit()

    cur.close()
    conn.close()
        


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
