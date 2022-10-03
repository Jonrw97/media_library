PRAGMA foreign_keys = ON;
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
    file_name VARCHAR(255),
    mime_type VARCHAR(255)
);

CREATE TABLE actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    character VARCHAR(255),
    movie_id INTEGER NOT NULL,
    FOREIGN KEY (movie_id) 
    REFERENCES movies (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
); 

INSERT INTO movies(id, movie_title, year, director, file_name, mime_type)
    VALUES (1, "Allo Allo", 1982, "David Kroft", "Allo_Allo.mkv", "video/mkv");
INSERT INTO movies VALUES (2, "Batman: Christmas with Joker", 1992, "Kent Butterworth", "Batman_Christmas_wih_Joker.mkv", "video/mkv");
INSERT INTO movies VALUES (3, "American Dad", 2005, "Ron Hughart", "American_Dad.mp4", "video/mp4");

INSERT INTO actors(id ,name, character, movie_id)
    VALUES(1, "Gorden Kaye", "Rene Artois", 1);
INSERT INTO actors VALUES(2, "Kevin Conroy", "Batman", 2);
INSERT INTO actors VALUES(3, "Seth Macfarlane", "Rodger", 3);
INSERT INTO actors VALUES(4, "Bob Jones", "Smith", 3);