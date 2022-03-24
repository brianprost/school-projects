-- Brian Prost
-- Project 3

-- movie
DROP TABLE IF EXISTS MOVIE;

CREATE TABLE IF NOT EXISTS MOVIE (
  movie_id integer PRIMARY KEY NOT NULL UNIQUE,
  vhs_copies integer,
  dvd_copies integer,
  title varchar(256) NOT NULL,
  genre varchar(128),
  running_length time,
  imdb_rating double,
  release_year smallint(4),
  director varchar(256) NOT NULL,
  actors varchar,
  academy_awards_won integer,
  academy_awards_nominated integer
);

-- distributor
DROP TABLE IF EXISTS DISTRIBUTOR;

CREATE TABLE IF NOT EXISTS DISTRIBUTOR (
  distributor_id integer PRIMARY KEY NOT NULL UNIQUE,
  distributor_name varchar(256) NOT NULL,
  distributor_address varchar(512) NOT NULL,
  distributor_zip varchar(5) NOT NULL,
  distributor_phone varchar(12) NOT NULL
);

-- customer
DROP TABLE IF EXISTS CUSTOMER;

CREATE TABLE IF NOT EXISTS CUSTOMER (
  customer_id integer PRIMARY KEY NOT NULL UNIQUE,
  first_name varchar(128) NOT NULL,
  last_name varchar(128) NOT NULL,
  address varchar(512) NOT NULL,
  zip_code varchar(5) NOT NULL,
  phone_number char(12) NOT NULL,
  email_address varchar(256) NOT NULL
);

-- catalog
DROP TABLE IF EXISTS CATALOG;

CREATE TABLE IF NOT EXISTS CATALOG (
  catalog_id integer PRIMARY KEY NOT NULL UNIQUE,
  distributor_id integer,
  FOREIGN KEY (distributor_id) REFERENCES DISTRIBUTOR (distributor_id)
);

-- catalog product
DROP TABLE IF EXISTS CATALOG_PRODUCT;

CREATE TABLE IF NOT EXISTS CATALOG_PRODUCT (
  product_id integer PRIMARY KEY NOT NULL UNIQUE,
  catalog_id integer NOT NULL,
  movie_id integer NOT NULL,
  dvd_price double NOT NULL,
  vhs_price double NOT NULL,
  FOREIGN KEY (catalog_id) REFERENCES CATALOG (catalog_id),
  FOREIGN KEY (movie_id) REFERENCES MOVIE (movie_id)
);

-- dvd copy
DROP TABLE IF EXISTS DVD_COPY;

CREATE TABLE IF NOT EXISTS DVD_COPY (
  dvd_id integer PRIMARY KEY NOT NULL UNIQUE,
  distributor_id integer NOT NULL,
  distributor_serial_number char(10) NOT NULL UNIQUE,
  movie_id integer NOT NULL,
  rental_rate float NOT NULL,
  is_available_for_rental boolean NOT NULL,
  FOREIGN KEY (distributor_id) references DISTRIBUTOR (distributor_id),
  FOREIGN KEY (movie_id) REFERENCES MOVIE (movie_id)
);

-- vhs copy
DROP TABLE IF EXISTS VHS_COPY;

CREATE TABLE IF NOT EXISTS VHS_COPY (
  vhs_id integer PRIMARY KEY NOT NULL UNIQUE,
  distributor_id char NOT NULL,
  distributor_serial_number char(10) NOT NULL UNIQUE,
  movie_id integer NOT NULL,
  rental_rate float NOT NULL,
  is_available_for_rental boolean NOT NULL,
  FOREIGN KEY (distributor_id) references DISTRIBUTOR (distributor_id),
  FOREIGN KEY (movie_id) REFERENCES MOVIE (movie_id)
);

-- rental
DROP TABLE IF EXISTS RENTAL;

CREATE TABLE IF NOT EXISTS RENTAL (
  rental_id integer PRIMARY KEY NOT NULL UNIQUE,
  customer_id integer NOT NULL,
  movie_id integer NOT NULL,
  dvd_id integer,
  vhs_id integer,
  rental_date date NOT NULL,
  return_date date NOT NULL,
  rental_price double NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES CUSTOMER (customer_id),
  FOREIGN KEY (dvd_id) REFERENCES DVD_COPY (dvd_id),
  FOREIGN KEY (vhs_id) REFERENCES VHS_COPY (vhs_id)
);