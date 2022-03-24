-- DROP TABLE IF EXISTS DVD_COPY;

-- CREATE TABLE IF NOT EXISTS DVD_COPY (
--   dvd_id integer PRIMARY KEY NOT NULL,
--   distributor_id integer NOT NULL,
--   distributor_serial_number char(10) NOT NULL,
--   movie_id integer NOT NULL,
--   rental_rate float NOT NULL,
--   is_available_for_rental boolean NOT NULL
-- );


INSERT INTO DVD_COPY(dvd_id, distributor_id, movie_id, distributor_serial_number, rental_rate, is_available_for_rental)
VALUES (1001, 1005, 1004, 'dvd1582961', 3.99, TRUE);

INSERT INTO DVD_COPY(dvd_id, distributor_id, movie_id, distributor_serial_number, rental_rate, is_available_for_rental)
VALUES (1002, 1004, 1001, 'dvd4957284', 2.99, TRUE);

INSERT INTO DVD_COPY(dvd_id, distributor_id, movie_id, distributor_serial_number, rental_rate, is_available_for_rental)
VALUES (1003, 1001, 1003, 'dvd5718543', 5.99, TRUE);

INSERT INTO DVD_COPY(dvd_id, distributor_id, movie_id, distributor_serial_number, rental_rate, is_available_for_rental)
VALUES (1004, 1003, 1005, 'dvd1135920', 2.99, TRUE);

INSERT INTO DVD_COPY(dvd_id, distributor_id, movie_id, distributor_serial_number, rental_rate, is_available_for_rental)
VALUES (1005, 1002, 1002, 'dvd9949993', 6.99, TRUE);
