-- DROP TABLE IF EXISTS MOVIE;

-- CREATE TABLE IF NOT EXISTS MOVIE (
--   movie_id integer PRIMARY KEY NOT NULL,
--   vhs_copies integer,
--   dvd_copies integer,
--   title varchar(256) NOT NULL,
--   genre varchar(128),
--   running_length time,
--   imdb_rating double,
--   release_year smallint(4),
--   director varchar(256) NOT NULL,
--   actors varchar,
--   academy_awards_won integer,
--   academy_awards_nominated integer
-- );

INSERT INTO MOVIE(movie_id, vhs_copies, dvd_copies, title, genre, running_length, imdb_rating, release_year, director, actors, academy_awards_won, academy_awards_nominated)
VALUES (1001, 5, 9, 'The Godfather', 'Drama', '02:55:00', 9.2, 1972, 'Francis Ford Coppola', 'Marion Brando, Al Pacino, James Caan, Diane Keaton', 3, 11);

INSERT INTO MOVIE(movie_id, vhs_copies, dvd_copies, title, genre, running_length, imdb_rating, release_year, director, actors, academy_awards_won, academy_awards_nominated)
VALUES (1002, 4, 8, 'The Shawshank Redemption', 'Drama', '02:22:00', 9.3, 1994, 'Frank Darabont', 'Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler', 0, 7);

INSERT INTO MOVIE(movie_id, vhs_copies, dvd_copies, title, genre, running_length, imdb_rating, release_year, director, actors, academy_awards_won, academy_awards_nominated)
VALUES (1003, 6, 4, 'Schindler''s List', 'Drama', '03:15:00', 8.9, 1993, 'Steven Spielberg', 'Liam Neeson, Ralph Fiennes, Ben Kingsley, Caroline Goodall', 7, 12);

INSERT INTO MOVIE(movie_id, vhs_copies, dvd_copies, title, genre, running_length, imdb_rating, release_year, director, actors, academy_awards_won, academy_awards_nominated)
VALUES (1004, 5, 4, '2001: A Space Odyssey', 'Sci-Fi', '02:29:00', 8.3, 1968, 'Stanley Kubrick', 'Keir Dullea, Gary Lockwood, William Sylvester, Daniel Richter', 1, 4);

INSERT INTO MOVIE(movie_id, vhs_copies, dvd_copies, title, genre, running_length, imdb_rating, release_year, director, actors, academy_awards_won, academy_awards_nominated)
VALUES (1005, 8, 12, 'Titanic', 'Romance', '03:14:00', 7.8, 1997, 'James Cameron', 'Leonardo DiCaprio, Kate Winslet, Billy Zane, Kathy Bates', 11, 14);
