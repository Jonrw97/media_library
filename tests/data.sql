INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT OR IGNORE INTO movies(id, movie_title, year, director, file_name, mime_type, movie_type, location, description)
    VALUES (1, "Allo Allo", 1982, "David Kroft", "Allo_Allo.mkv", "video/mkv", "other","","");
INSERT OR IGNORE INTO movies VALUES (2, "Batman: Christmas with Joker", 1992, "Kent Butterworth", "Batman_Christmas_wih_Joker.mkv", "video/mkv", "other","","");
INSERT OR IGNORE INTO movies VALUES (3, "American Dad", 2005, "Ron Hughart", "American_Dad.mp4", "video/mp4", "other","","");
INSERT OR IGNORE INTO movies VALUES (4, "Walking Safari", 2017, "Jonathan Watkins", "https://jon-media-library-2022.s3.eu-west-1.amazonaws.com/libary-1/portfolio-videography/walking_safari.mp4", "video/mp4", "portfolio", "Mfuwe Lodge", "A Trip through South Luangwa on foot.");
INSERT OR IGNORE INTO movies VALUES (5, "Luangwa in a Minute", 2017, "Jonathan Watkins", "https://jon-media-library-2022.s3.eu-west-1.amazonaws.com/libary-1/portfolio-videography/wildlife_2.mp4", "video/mp4", "portfolio", "Mfuwe Lodge", "See the sights of South Luangwa in a minute.");
INSERT OR IGNORE INTO movies VALUES (6, "Life in Luangwa", 2017, "Jonathan Watkins", "https://jon-media-library-2022.s3.eu-west-1.amazonaws.com/libary-1/portfolio-videography/wildlife_1.mp4", "video/mp4", "portfolio", "Mfuwe Lodge", "A glimplse into the wildlife of South Luangwa.");

INSERT OR IGNORE INTO actors(id ,name, character, movie_id)
    VALUES(1, "Gorden Kaye", "Rene Artois", 1);
INSERT OR IGNORE INTO actors VALUES(2, "Kevin Conroy", "Batman", 2);
INSERT OR IGNORE INTO actors VALUES(3, "Seth Macfarlane", "Rodger", 3);
INSERT OR IGNORE INTO actors VALUES(4, "Bob Jones", "Smith", 3);