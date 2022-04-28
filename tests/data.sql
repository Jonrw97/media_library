INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO movies(id, movie_title, year, director, actor)
    VALUES (1, "Matrix", 1999, "Wachoski Brothers", "Keanu Reeves");
INSERT INTO movies VALUES (2, "The Batman", 2022, "Matt Reeves", "Robert Pattinson");
INSERT INTO movies VALUES (3, "Deadpool", 2016, "Tim Miller", "Ryan Renolds");