DROP TABLE IF EXISTS RENTAL;

CREATE TABLE IF NOT EXISTS RENTAL (
  rental_id integer PRIMARY KEY NOT NULL,
  customer_id integer NOT NULL,
  movie_id integer NOT NULL,
  dvd_id integer,
  vhs_id integer,
  rental_date date NOT NULL,
  return_date date NOT NULL,
  rental_price double NOT NULL
);

INSERT INTO RENTAL(rental_id, customer_id, movie_id, dvd_id, vhs_id, rental_date, return_date, rental_price)
VALUES (1001, 1002, 1002, NULL, 1001, '2021-02-19', '2021-02-24', 9.95);

INSERT INTO RENTAL(rental_id, customer_id, movie_id, dvd_id, vhs_id, rental_date, return_date, rental_price)
VALUES (1002, 1003, 1003, 1005, NULL, '2021-03-23', '2021-03-26', 20.97);

INSERT INTO RENTAL(rental_id, customer_id, movie_id, dvd_id, vhs_id, rental_date, return_date, rental_price)
VALUES (1003, 1001, 1005, 1004, NULL, '2021-03-09', '2021-03-16', 20.93);

INSERT INTO RENTAL(rental_id, customer_id, movie_id, dvd_id, vhs_id, rental_date, return_date, rental_price)
VALUES (1004, 1005, 1001, NULL, 1004, '2020-06-16', '2020-06-27', 10.89);

INSERT INTO RENTAL(rental_id, customer_id, movie_id, dvd_id, vhs_id, rental_date, return_date, rental_price)
VALUES (1005, 1004, 1004, 1001, NULL, '2020-06-18', '2020-06-19', 3.99);
