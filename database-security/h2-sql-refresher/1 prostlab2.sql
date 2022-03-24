-- Brian Prost
-- Lab 2
-- prostlab2.sql
-- SDEV350 6380
-- Prof. Haseltine

--
-- 1. DROP TABLES
--

DROP TABLE Engineers CASCADE CONSTRAINTS;
DROP TABLE Faculty CASCADE CONSTRAINTS;
DROP TABLE Classes CASCADE CONSTRAINTS;
DROP TABLE ClassEnrollments CASCADE CONSTRAINTS;

-- set date format
ALTER SESSION SET nls_date_format='YYYY-MM-DD';


--
-- 2. CREATE TABLES
--

-- create Engineer table
CREATE TABLE Engineers (
	EID NUMBER(10) GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
	Lastname VARCHAR2(256) NOT NULL,
	Firstname VARCHAR2(256) NOT NULL,
	Email VARCHAR2(256) NOT NULL,
	Graddate DATE NOT NULL,
	PRIMARY KEY(EID)
);

-- create Faculty table
CREATE TABLE Faculty (
	FID NUMBER(10) GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
	Lastname VARCHAR2(256) NOT NULL,
	Firstname VARCHAR2(256) NOT NULL,
	Email VARCHAR2(256) NOT NULL,
	Hiredate DATE NOT NULL,
	PRIMARY KEY(FID)
);

-- create Classes table
CREATE TABLE Classes (
	CID NUMBER(10) GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
	Subject VARCHAR2(256) NOT NULL,
	Catalognbr NUMBER(10) NOT NULL,
	Title VARCHAR2(256) NOT NULL,
	PRIMARY KEY (CID)
);

-- create ClassEnrollments table
CREATE TABLE ClassEnrollments (
	EnID NUMBER(10) GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
	CID NUMBER(10) NOT NULL,
	FID NUMBER(10) NOT NULL,
	EID NUMBER(10) NOT NULL,
	PRIMARY KEY(EnID),
	FOREIGN KEY(CID) REFERENCES Classes(CID),
	FOREIGN KEY(FID) REFERENCES Faculty(FID),
	FOREIGN KEY(EID) REFERENCES Engineers(EID)
);


--
-- 3. INSERT RECORDS INTO EACH TABLE
--

-- insert data into ENGINEERS
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('Mouse','Mickey','MMouse@student.disney.com','2022-05-13');
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('Mouse','Minnie','MMouse@student.disney.com','2023-05-19');
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('Duck','Donald','DDuck@student.disney.com','2023-05-19');
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('Duck','Daisy','DDuck@student.disney.com','2022-05-13');
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('McDuck','Scrooge','SMcDuck@student.disney.com','2023-05-19');
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('McQuack','Launchpad','LMcQuack@student.disney.com','2023-05-19');
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('Bell','Tinker','TBell@student.disney.com','2022-05-13');
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('Pan','Peter','PPan@student.disney.com','2023-05-19');
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('Hook','Captain','CHook@student.disney.com','2023-05-19');
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('Hatter','Mad','MHatter@student.disney.com','2023-05-19');
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('White','Snow','SWhite@student.disney.com','2022-05-13');
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('Charming','Prince','PCharming@student.disney.com','2022-05-13');
-- Cinderella's last name is Tremaine: https://disney.fandom.com/wiki/Cinderella
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('Tremaine','Cinderella','CTremaine@student.disney.com','2022-05-13');
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('Hood','Robin','RHood@student.disney.com','2023-05-19');
INSERT into Engineers (Lastname, Firstname, Email, Graddate) VALUES ('Pooh','Winnie The', 'WPooh@student.disney.com','2022-05-13');

-- insert data into Faculty
INSERT into Faculty (Lastname, Firstname, Email, Hiredate) VALUES ('Iger','Bob','bob.iger@faculty.disney.com','1999-02-25');
INSERT into Faculty (Lastname, Firstname, Email, Hiredate) VALUES ('Disney','Roy O.','roy.disney@faculty.disney.com','1929-06-24');
INSERT into Faculty (Lastname, Firstname, Email, Hiredate) VALUES ('Disney','Walt','walt.disney@faculty.disney.com','1923-10-16');

-- insert data into Classes
INSERT into Classes (Subject, Catalognbr, Title) VALUES ('FINC','210','Making Money as an Animated Character');
INSERT into Classes (Subject, Catalognbr, Title) VALUES ('DRAW','100','Introduction to Drawing');
INSERT into Classes (Subject, Catalognbr, Title) VALUES ('BUSI','460','Introspection into Self Worth in International Markets: A Study of Global Intellectual Property');

-- insert data into ClassEnrollments
INSERT into ClassEnrollments (CID,FID,EID) VALUES (2,3,2);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (3,1,14);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (1,2,6);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (3,1,11);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (2,3,4);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (2,3,5);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (2,3,3);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (3,1,9);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (2,3,8);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (3,1,13);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (1,2,7);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (1,2,10);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (3,1,1);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (1,2,12);
INSERT into ClassEnrollments (CID,FID,EID) VALUES (2,3,15);


--
-- 4. SELECT RECORDS FROM EACH TABLE
--

-- select all records from Engineers table in descending order by EID
SELECT * FROM Engineers ORDER BY EID DESC;

-- select all records from Faculty table in descending order by FID
SELECT * FROM Faculty ORDER BY FID DESC;

-- select all records from Classes table in descending order by CID
SELECT * FROM Classes ORDER BY CID DESC;

-- select all records from ClassEnrollments table in descending order by EnID
SELECT * FROM ClassEnrollments ORDER BY EnID DESC;


--
-- 5. UPDATE RECORDS
--

-- update the Lastname of one faculty to be "Friendship"
UPDATE Faculty SET Lastname = 'Friendship' WHERE FID=1;

-- update the Firstname of one engineer to be "Amadeus"
UPDATE Engineers SET Firstname = 'Amadeus' WHERE EID=5;

-- update the subject of one class to be "IOT Cyber"
UPDATE Classes SET Subject = 'IOT Cyber' WHERE CID=2;


--
-- 6. Delete the ClassEnrollments record with the lowest EnID
--

DELETE FROM ClassEnrollments WHERE EnID = (SELECT MIN(EnID) from CLASSENROLLMENTS);


--
-- 7. Create a view joining the required tables such that a user can retreive the
--    Engineer's Lastname and Firstname, the Faculty Lastname and Email and the
--    Class's Subject and Title for each Course enrollment.
--

CREATE OR REPLACE VIEW Detailed_Course_Enrollment_Info AS
SELECT
	EnID,
	Engineers.Lastname AS Student_Lastname,
	Engineers.Firstname AS Student_Firstname,
	Faculty.Lastname AS Faculty_Lastname,
	Faculty.Email AS Faculty_Email,
	Classes.SUBJECT AS Class_Subject,
	Classes.TITLE AS Class_Title
FROM
	ClassEnrollments
LEFT JOIN
	Engineers ON ClassEnrollments.EID = Engineers.EID
LEFT JOIN
	Faculty ON ClassEnrollments.FID = Faculty.FID
LEFT JOIN
	Classes ON ClassEnrollments.CID = Classes.CID
ORDER BY
	EnID;

SELECT * from Detailed_Course_Enrollment_Info;