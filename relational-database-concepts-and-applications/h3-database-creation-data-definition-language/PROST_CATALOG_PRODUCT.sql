-- DROP TABLE IF EXISTS CATALOG_PRODUCT;

-- CREATE TABLE IF NOT EXISTS CATALOG_PRODUCT (
--   product_id integer PRIMARY KEY NOT NULL,
--   catalog_id integer NOT NULL,
--   movie_id integer NOT NULL,
--   dvd_price double NOT NULL,
--   vhs_price double NOT NULL
-- );

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
