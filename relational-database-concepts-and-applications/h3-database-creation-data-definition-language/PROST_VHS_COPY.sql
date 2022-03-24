-- DROP TABLE IF EXISTS VHS_COPY;

-- CREATE TABLE IF NOT EXISTS VHS_COPY (
--   vhs_id integer PRIMARY KEY NOT NULL,
--   distributor_id char NOT NULL,
--   distributor_serial_number char(10) NOT NULL,
--   movie_id integer NOT NULL,
--   rental_rate float NOT NULL,
--   is_available_for_rental boolean NOT NULL
-- );


INSERT INTO VHS_COPY(vhs_id, distributor_id, movie_id, distributor_serial_number, rental_rate, is_available_for_rental)
VALUES (1001, 1004, 1005, 'vhs8273645', 1.99, TRUE);

INSERT INTO VHS_COPY(vhs_id, distributor_id, movie_id, distributor_serial_number, rental_rate, is_available_for_rental)
VALUES (1002, 1001, 1002, 'vhs1951039', 2.99, TRUE);

INSERT INTO VHS_COPY(vhs_id, distributor_id, movie_id, distributor_serial_number, rental_rate, is_available_for_rental)
VALUES (1003, 1005, 1003, 'vhs3153532', 1.99, TRUE);

INSERT INTO VHS_COPY(vhs_id, distributor_id, movie_id, distributor_serial_number, rental_rate, is_available_for_rental)
VALUES (1004, 1002, 1001, 'vhs1029381', 0.99, TRUE);

INSERT INTO VHS_COPY(vhs_id, distributor_id, movie_id, distributor_serial_number, rental_rate, is_available_for_rental)
VALUES (1005, 1003, 1004, 'vhs5091823', 1.49, TRUE);
