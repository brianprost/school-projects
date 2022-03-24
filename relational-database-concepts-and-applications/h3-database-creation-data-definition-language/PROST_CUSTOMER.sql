-- DROP TABLE IF EXISTS CUSTOMER;

-- CREATE TABLE IF NOT EXISTS CUSTOMER (
--   customer_id integer PRIMARY KEY NOT NULL,
--   first_name varchar(128) NOT NULL,
--   last_name varchar(128) NOT NULL,
--   address varchar(512) NOT NULL,
--   zip_code varchar(5) NOT NULL,
--   phone_number char(12) NOT NULL,
--   email_address varchar(256) NOT NULL
-- );

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
