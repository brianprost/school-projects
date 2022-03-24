-- DROP TABLE IF EXISTS CATALOG;

-- CREATE TABLE IF NOT EXISTS CATALOG (
--   catalog_id integer PRIMARY KEY NOT NULL,
--   distributor_id integer
-- );


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
