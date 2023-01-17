DROP TABLE IF EXISTS movies CASCADE;
DROP TABLE IF EXISTS actors;

CREATE TABLE if not exists user_account (
    id SERIAL NOT NULL PRIMARY KEY,
    user_name VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE movies (
    id SERIAL NOT NULL PRIMARY KEY,
    movie_title VARCHAR(255) NOT NULL,
    year INTEGER,
    director VARCHAR(255),
    file_name VARCHAR(255),
    mime_type VARCHAR(255),
    movie_type VARCHAR(255),
    location VARCHAR(255),
    description VARCHAR(255),
    featured INTEGER,
    publish INTEGER
);

CREATE TABLE actors (
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(255),
    character VARCHAR(255),
    movie_id INTEGER NOT NULL,
    FOREIGN KEY (movie_id) 
    REFERENCES movies (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
); 

INSERT INTO 
    movies(movie_title, year, director, file_name, mime_type, movie_type, location, description, featured, publish)
    VALUES ('Walking Safari', 2018, 'Jonathan Watkins', 'https://jon-media-library-2022.s3.eu-west-1.amazonaws.com/libary-1/portfolio-videography/walking_safari.mp4', 'video/mp4', 'portfolio', 'Mfuwe Lodge', 'A Trip through South Luangwa on foot.', 0, 1),
('Luangwa in a Minute', 2017, 'Jonathan Watkins', 'https://jon-media-library-2022.s3.eu-west-1.amazonaws.com/libary-1/portfolio-videography/wildlife_2.mp4', 'video/mp4', 'portfolio', 'Mfuwe Lodge', 'See the sights of South Luangwa in a minute.', 0, 1),
('Life in Luangwa', 2017, 'Jonathan Watkins', 'https://jon-media-library-2022.s3.eu-west-1.amazonaws.com/libary-1/portfolio-videography/wildlife_1.mp4', 'video/mp4', 'portfolio', 'Mfuwe Lodge', 'A glimplse into the wildlife of South Luangwa.', 1, 1),
('Clean Water', 2018, 'Jonathan Watkins', 'https://jon-media-library-2022.s3.eu-west-1.amazonaws.com/libary-1/portfolio-videography/clean_water.mp4', 'video/mp4', 'portfolio', 'Mfuwe Lodge', 'The impact that the clean water intiative has.', 0, 1),
('Pizza Time', 2019, 'Jonathan Watkins', 'https://jon-media-library-2022.s3.eu-west-1.amazonaws.com/libary-1/portfolio-videography/pizza_time.mp4', 'video/mp4', 'portfolio', 'Mfuwe Lodge', 'Making your own pizza at Mfuwe Lodge.', 0, 1),
('Sausage Tree', 2017, 'Jonathan Watkins', 'https://jon-media-library-2022.s3.eu-west-1.amazonaws.com/libary-1/portfolio-videography/sausage_tree.mp4', 'video/mp4', 'portfolio', 'Mfuwe Lodge', 'See all the good work Sausage Tree has done for the town of Mfuwe Lodge.', 0, 1),
('Wild Dogs', 2019, 'Jonathan Watkins', 'https://jon-media-library-2022.s3.eu-west-1.amazonaws.com/libary-1/portfolio-videography/wild_dogs.mp4', 'video/mp4', 'portfolio', 'Mfuwe Lodge', 'All the things a pack of wild dogs can get up to.', 0, 1);

INSERT INTO actors(name, character, movie_id)
    VALUES('Gorden Kaye', 'Rene Artois', 1),
('Kevin Conroy', 'Batman', 2),
('Seth Macfarlane', 'Rodger', 3),
('Bob Jones', 'Smith', 3);









