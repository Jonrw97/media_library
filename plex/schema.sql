DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS actors;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_title VARCHAR(255) NOT NULL,
    year INTEGER,
    director VARCHAR(255),
    actor VARCHAR(255),
    file_name VARCHAR(255)
);

CREATE TABLE actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    actor_name VARCHAR(255) NOT NULL
); 

INSERT INTO movies(id, movie_title, year, director, actor, file_name)
    VALUES (1, "Allo Allo", 1982, "David Kroft", "Gorden Kaye", "Allo Allo.mkv");
INSERT INTO movies VALUES (2, "Batman: Christmas with Joker", 1992, "Kent Butterworth", "Kevin Conroy", "Batman Christmas wih Joker.mkv");
INSERT INTO movies VALUES (3, "American Dad", 2005, "Ron Hughart", "Seth MacFarlane", "American Dad.mp4");