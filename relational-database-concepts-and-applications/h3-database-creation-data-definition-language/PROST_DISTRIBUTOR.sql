-- DROP TABLE IF EXISTS DISTRIBUTOR;

-- CREATE TABLE IF NOT EXISTS DISTRIBUTOR (
--   distributor_id integer PRIMARY KEY NOT NULL,
--   distributor_name varchar(256) NOT NULL,
--   distributor_address varchar(512) NOT NULL,
--   distributor_zip varchar(5) NOT NULL,
--   distributor_phone varchar(12) NOT NULL
-- );


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
