PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS actors;

CREATE TABLE IF NOT EXISTS user (
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
    mime_type VARCHAR(255),
    movie_type VARCHAR(255),
    location VARCHAR(255),
    description VARCHAR(255)
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

INSERT OR IGNORE INTO movies(id, movie_title, year, director, file_name, mime_type, movie_type, location, description)
    VALUES (1, "Allo Allo", 1982, "David Kroft", "Allo_Allo.mkv", "video/mkv", "other","","");
INSERT OR IGNORE INTO movies VALUES (2, "Batman: Christmas with Joker", 1992, "Kent Butterworth", "Batman_Christmas_wih_Joker.mkv", "video/mkv", "other","","");
INSERT OR IGNORE INTO movies VALUES (3, "American Dad", 2005, "Ron Hughart", "American_Dad.mp4", "video/mp4", "other","","");
INSERT OR IGNORE INTO movies VALUES (4, "Walking Safari", 2017, "Jonathan Watkins", "https://jon-media-library-2022.s3.eu-west-1.amazonaws.com/libary-1/portfolio-videography/walking_safari.mp4", "video/mp4", "portfolio", "Mfuwe Lodge", "A Trip through South Luangwa on foot.");
INSERT OR IGNORE INTO movies VALUES (5, "Luangwa in a Minute", 2017, "Jonathan Watkins", "https://jon-media-library-2022.s3.eu-west-1.amazonaws.com/libary-1/portfolio-videography/wildlife_2.mp4", "video/mp4", "portfolio", "Mfuwe Lodge", "See the sights of South Luangwa in a minute.");
INSERT OR IGNORE INTO movies VALUES (6, "Life in Luangwa", 2017, "Jonathan Watkins", "https://jon-media-library-2022.s3.eu-west-1.amazonaws.com/libary-1/portfolio-videography/wildlife_1.mp4", "video/mp4", "portfolio", "Mfuwe Lodge", "A glimplse into the wildlife of South Luangwa.");

INSERT INTO actors(id ,name, character, movie_id)
    VALUES(1, "Gorden Kaye", "Rene Artois", 1);
INSERT INTO actors VALUES(2, "Kevin Conroy", "Batman", 2);
INSERT INTO actors VALUES(3, "Seth Macfarlane", "Rodger", 3);
INSERT INTO actors VALUES(4, "Bob Jones", "Smith", 3);
