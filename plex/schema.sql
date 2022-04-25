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
    actor VARCHAR(255)
);

CREATE TABLE actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    actor_name VARCHAR(255) NOT NULL
); 

INSERT INTO movies(id, movie_title, year, director, actor)
    VALUES (1, "Matrix", 1999, "Wachoski Brothers", "Keanu Reeves");
INSERT INTO movies VALUES (2, "The Batman", 2022, "Matt Reeves", "Robert Pattinson");
INSERT INTO movies VALUES (3, "Deadpool", 2016, "Tim Miller", "Ryan Renolds");