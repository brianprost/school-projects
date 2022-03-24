-- Brian Prost
-- Project 3

-- movie
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

-- distributor
INSERT INTO DISTRIBUTOR(distributor_id, distributor_name, distributor_address, distributor_zip, distributor_phone)
VALUES (1001, 'Doug Smit Rentals, LLC.', '4806 Cook Hill Road', '15446', '203-520-3617');

INSERT INTO DISTRIBUTOR(distributor_id, distributor_name, distributor_address, distributor_zip, distributor_phone)
VALUES (1002, 'America Movies Inc.', '1073 Lighthouse Drive', '65802', '417-240-5249');

INSERT INTO DISTRIBUTOR(distributor_id, distributor_name, distributor_address, distributor_zip, distributor_phone)
VALUES (1003, 'Treehouse Film Distributors', '3310 Willis Avenue', '32083', '386-431-6818');

INSERT INTO DISTRIBUTOR(distributor_id, distributor_name, distributor_address, distributor_zip, distributor_phone)
VALUES (1004, 'World Cinema Rentals', '2783 Star Trek Drive', '36602', '850-366-0291');

INSERT INTO DISTRIBUTOR(distributor_id, distributor_name, distributor_address, distributor_zip, distributor_phone)
VALUES (1005, 'Premier Movie Rental Distributors, Inc.', '180 Patterson Street', '77025', '713-349-6733');

-- customer
INSERT INTO CUSTOMER(customer_id, first_name, last_name, address, zip_code, phone_number, email_address)
VALUES (1001, 'Brian', 'Prost', '123 Fake St.', '12345', '202-867-5309', 'bprost@student.umgc.edu');

INSERT INTO CUSTOMER(customer_id, first_name, last_name, address, zip_code, phone_number, email_address)
VALUES (1002, 'Joe', 'Biden', '1600 Pennsylvania Ave.', '20006', '202-123-4567', 'joe@whitehouse.gov');

INSERT INTO CUSTOMER(customer_id, first_name, last_name, address, zip_code, phone_number, email_address)
VALUES (1003, 'Donny', 'Trump', '1100 S. Ocean Blvd', '33404', '561-832-2600', 'donald@trumpuniversity.ru');

INSERT INTO CUSTOMER(customer_id, first_name, last_name, address, zip_code, phone_number, email_address)
VALUES (1004, 'George', 'Washington', '3200 Mount Vernon Memorial Highway', '22309', '703-780-2000', 'good_ole_george@usa.gov');

INSERT INTO CUSTOMER(customer_id, first_name, last_name, address, zip_code, phone_number, email_address)
VALUES (1005, 'Ariana', 'Grande', '3435 Positional St.', '90210', '310-882-4123', 'one_less_problem@interscopercs.com');

-- catalog
INSERT INTO CATALOG(catalog_id, distributor_id)
VALUES (1001, 1002);

INSERT INTO CATALOG(catalog_id, distributor_id)
VALUES (1002, 1001);

INSERT INTO CATALOG(catalog_id, distributor_id)
VALUES (1003, 1005);

INSERT INTO CATALOG(catalog_id, distributor_id)
VALUES (1004, 1004);

INSERT INTO CATALOG(catalog_id, distributor_id)
VALUES (1005, 1003);

-- catalog product
INSERT INTO CATALOG_PRODUCT(product_id, catalog_id, movie_id, dvd_price, vhs_price)
VALUES (1001, 1005, 1002, 1.49, 0.49);

INSERT INTO CATALOG_PRODUCT(product_id, catalog_id, movie_id, dvd_price, vhs_price)
VALUES (1002, 1004, 1005, 1.99, 0.29);

INSERT INTO CATALOG_PRODUCT(product_id, catalog_id, movie_id, dvd_price, vhs_price)
VALUES (1003, 1001, 1003, 2.09, 0.69);

INSERT INTO CATALOG_PRODUCT(product_id, catalog_id, movie_id, dvd_price, vhs_price)
VALUES (1004, 1003, 1001, 2.49, 0.99);

INSERT INTO CATALOG_PRODUCT(product_id, catalog_id, movie_id, dvd_price, vhs_price)
VALUES (1005, 1002, 1004, 1.89, 0.59);

-- dvd copy
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

-- vhs copy
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

-- rental
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