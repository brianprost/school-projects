-- Brian Prost
-- Lab 5
-- prost_lab_5.sql
-- SDEV350 6380
-- Prof. Haseltine

--
-- 1. Create Tables
--

create table Customers (
	CustomerID int not null,
	CustomerLastName varchar2(40) not null,
	CustomerFirstName varchar2(40) not null,
	CustomerEmail varchar2(80) not null,
	CustomerPhone varchar2(12) not null,
	CustomerCellPhone varchar2(12) not null,
	PRIMARY KEY (CustomerID)
);

create table Sales2019 (
    CustomerID      int           not null,
    TransactionDate DATE          not null,
    SalesAmount     number(10, 2) not null,
    ProfitAmount    number(10, 2) not null,
    FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID),
    PRIMARY KEY(CustomerID, TransactionDate)
);

create table Projections2020 (
	CustomerID int not null,
	QuarterlyPurchaseAmount number(10,2) not null,
	QuarterlyProfitAmount number(10,2) not null,
	Confidence number(4,2) not null,
	FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID)
);

--
-- 2. Initialize Audit
--

AUDIT SELECT ON Customers;
AUDIT INSERT ON Customers;
AUDIT UPDATE ON Customers;
AUDIT DELETE ON Customers;
AUDIT SELECT ON Sales2019;
AUDIT INSERT ON Sales2019;
AUDIT UPDATE ON Sales2019;
AUDIT DELETE ON Sales2019;
AUDIT SELECT ON Projections2020;
AUDIT INSERT ON Projections2020;
AUDIT UPDATE ON Projections2020;
AUDIT DELETE ON Projections2020;

--
-- 3. Create Role
--
create role R5BrianProst;
grant CONNECT to R5BrianProst;

-- for customers
grant SELECT on CUSTOMERS to R5BrianProst;
grant INSERT on CUSTOMERS to R5BrianProst;
grant UPDATE on CUSTOMERS to R5BrianProst;
grant DELETE on CUSTOMERS to R5BrianProst;
-- for sales2019
grant SELECT on SALES2019 to R5BrianProst;
grant INSERT on SALES2019 to R5BrianProst;
grant UPDATE on SALES2019 to R5BrianProst;
grant DELETE on SALES2019 to R5BrianProst;
-- for projection
grant SELECT on PROJECTIONS2020 to R5BrianProst;
grant INSERT on PROJECTIONS2020 to R5BrianProst;
grant UPDATE on PROJECTIONS2020 to R5BrianProst;
grant DELETE on PROJECTIONS2020 to R5BrianProst;

--
-- 4. Create 3 users
--

CREATE USER Lab5_1BrianProst IDENTIFIED by "V-tVhmJ2DYQVHJ!";

CREATE USER Lab5_2BrianProst IDENTIFIED by "MtJXJMDWqKvW@9J";

CREATE USER Lab5_3BrianProst IDENTIFIED by "9c!wVHsdwD!qyCD";

-- grant role R5BrianProst to these users

grant R5BrianProst to Lab5_1BrianProst;
grant R5BrianProst to Lab5_2BrianProst;
grant R5BrianProst to Lab5_3BrianProst;


--
-- 5. Populate data
--

-- CUSTOMERS COME FIRST

-- this one is done by Lab5_1BrianProst
insert into MADMIN.Customers (CUSTOMERID, CUSTOMERLASTNAME, CUSTOMERFIRSTNAME, CUSTOMEREMAIL, CUSTOMERPHONE, CUSTOMERCELLPHONE) values (1,'Sanders','Bernie','the_socialist@senate.gov','802-862-0697','800-339-9834');

-- this one is done by Lab5_2BrianProst
insert into MADMIN.Customers (CUSTOMERID, CUSTOMERLASTNAME, CUSTOMERFIRSTNAME, CUSTOMEREMAIL, CUSTOMERPHONE, CUSTOMERCELLPHONE) values (2,'Cruz','Ted','colder_than_cancun@senate.gov','512-916-5834','202-224-5922');

-- this one is done by Lab5_3BrianProst
insert into MADMIN.Customers (CUSTOMERID, CUSTOMERLASTNAME, CUSTOMERFIRSTNAME, CUSTOMEREMAIL, CUSTOMERPHONE, CUSTOMERCELLPHONE) values (3,'Manchin','Joe','filibuster_luver@senate.gov','304-342-5855','304-343-7144');


-- SALES ARE NEXT, BUT REALLY FIRST IN OUR COLD HEARTS

-- these are done by Lab5_1BrianProst
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '20-JAN-19', 16.19, 2.58);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '02-APR-19', 57.75, 2.31);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '05-AUG-19', 20.27, 0.81);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '07-SEP-19', 99.00, 3.96);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '06-NOV-19', 16.57, 0.66);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '10-OCT-19', 5.04, 0.20);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '26-MAY-19', 82.31, 3.29);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '16-MAY-19', 67.69, 2.71);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '17-JAN-19', 73.47, 2.94);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '09-MAY-19', 86.98, 3.48);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '11-AUG-19', 8.06, 0.32);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '04-OCT-19', 64.78, 2.59);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '15-AUG-19', 90.43, 3.62);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '18-NOV-19', 23.08, 0.92);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (2, '13-NOV-19', 11.16, 0.45);


-- these are done by Lab5_2BrianProst
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (2, '18-FEB-19', 89.54, 2.67);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (2, '07-OCT-19', 72.42, 2.17);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '04-SEP-19', 36.53, 1.10);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (2, '03-FEB-19', 35.23, 1.06);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '18-JUN-19', 13.29, 0.40);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '02-APR-19', 59.44, 1.78);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '26-DEC-19', 33.62, 1.01);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '28-OCT-19', 92.73, 2.78);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '27-JAN-19', 58.87, 1.77);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '22-JUL-19', 62.29, 1.87);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '01-MAR-19', 75.87, 2.28);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (2, '04-APR-19', 16.53, 0.50);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (2, '08-DEC-19', 2.95, 0.09);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '26-AUG-19', 50.46, 1.51);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '27-JUL-19', 77.00, 2.31);

-- these are done by Lab5_3BrianProst
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '14-JUN-19', 52.92, 18.63);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '12-SEP-19', 96.86, 7.75);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '18-MAR-19', 44.80, 3.58);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (2, '15-APR-19', 97.26, 7.78);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '09-DEC-19', 74.53, 5.96);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (2, '05-NOV-19', 66.16, 5.29);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '06-NOV-19', 46.84, 3.75);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (2, '06-FEB-19', 3.90, 0.31);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (2, '16-JUL-19', 13.45, 1.08);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (2, '21-JAN-19', 96.39, 7.71);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (2, '22-OCT-19', 45.41, 3.63);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (1, '04-FEB-19', 88.57, 7.09);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '07-DEC-19', 99.53, 7.96);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (3, '26-NOV-19', 31.75, 2.54);
insert into MADMIN.Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount) VALUES (2, '20-OCT-19', 73.91, 5.91);

-- LASTLY, PROJECTIONS

-- this one is done by Lab5_1BrianProst
insert into MADMIN.Projections2020 (CustomerID, QuarterlyPurchaseAmount, QuarterlyProfitAmount, Confidence) VALUES (3, 500.29, 177.19, 0.82);

-- this one is done by Lab5_2BrianProst
insert into MADMIN.Projections2020 (CustomerID, QuarterlyPurchaseAmount, QuarterlyProfitAmount, Confidence) VALUES (2, 3527.18, 2366.23, 0.91);

-- this one is done by Lab5_3BrianProst
insert into MADMIN.Projections2020 (CustomerID, QuarterlyPurchaseAmount, QuarterlyProfitAmount, Confidence) VALUES (1, 40.21, 25.32, 0.68);

--
-- 6. update some data
--

-- these are done by Lab5_1BrianProst
UPDATE MADMIN.CUSTOMERS
SET CUSTOMEREMAIL = 'bernie.sanders@senate.gov'
WHERE CUSTOMERID = 1;

UPDATE MADMIN.SALES2019
SET PROFITAMOUNT = 0.50
WHERE SALESAMOUNT < 14.00;

UPDATE MADMIN.PROJECTIONS2020
SET CONFIDENCE = .75
WHERE CUSTOMERID = 2;


-- these are done by Lab5_2BrianProst
UPDATE MADMIN.CUSTOMERS
SET CUSTOMEREMAIL = 'joe.manchin@senate.gov'
WHERE CUSTOMERID = 3;

UPDATE MADMIN.SALES2019
SET PROFITAMOUNT = 9.80
WHERE SALESAMOUNT between 50.23 and 75.25;

UPDATE MADMIN.PROJECTIONS2020
SET CONFIDENCE = .99
WHERE CUSTOMERID = 1;

-- these are done by Lab5_3BrianProst
UPDATE MADMIN.CUSTOMERS
SET CUSTOMEREMAIL = 'teddy.cruz@senate.gov'
WHERE CUSTOMERID = 2;

UPDATE MADMIN.SALES2019
SET PROFITAMOUNT = 15.24
WHERE SALESAMOUNT > 75.25;

UPDATE MADMIN.PROJECTIONS2020
SET CONFIDENCE = .05
WHERE CUSTOMERID = 1;


--
-- 7. Delete some data
--

-- these are done by Lab5_1BrianProst
DELETE FROM MADMIN.SALES2019 WHERE TransactionDate like '%-OCT-%';
DELETE FROM MADMIN.SALES2019 WHERE PROFITAMOUNT > 12.00;

-- these are done by Lab5_2BrianProst
DELETE FROM MADMIN.SALES2019 WHERE CUSTOMERID = 2;
DELETE FROM MADMIN.SALES2019 WHERE SALESAMOUNT between 35.00 and 55.00;

-- these are done by Lab5_3BrianProst
DELETE FROM MADMIN.SALES2019 WHERE TransactionDate LIKE '%-DEC-%';
DELETE FROM MADMIN.PROJECTIONS2020 WHERE CUSTOMERID = 2;
DELETE FROM MADMIN.CUSTOMERS WHERE CUSTOMERID = 2;


--
-- 8. View each table as each user
--

-- these are done by Lab5_1BrianProst
SELECT * FROM MADMIN.CUSTOMERS;
SELECT * FROM MADMIN.SALES2019;
SELECT * FROM MADMIN.PROJECTIONS2020;

-- these are done by Lab5_2BrianProst
SELECT * FROM MADMIN.CUSTOMERS;
SELECT * FROM MADMIN.SALES2019;
SELECT * FROM MADMIN.PROJECTIONS2020;

-- these are done by Lab5_3BrianProst
SELECT * FROM MADMIN.CUSTOMERS;
SELECT * FROM MADMIN.SALES2019;
SELECT * FROM MADMIN.PROJECTIONS2020;


select * from
dba_audit_trail;