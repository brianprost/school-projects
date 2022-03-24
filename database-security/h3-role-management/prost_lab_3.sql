-- Brian Prost
-- Lab 3
-- prost_lab_3.sql
-- SDEV350 6380
-- Prof. Haseltine


--
-- 1. Create unique Profile
--

CREATE PROFILE PBrianProst LIMIT
    PASSWORD_VERIFY_FUNCTION ora12c_verify_function
    SESSIONS_PER_USER 3
    FAILED_LOGIN_ATTEMPTS 4
    PASSWORD_LIFE_TIME 120
    PASSWORD_LOCK_TIME 1 / 24;


--
-- 2. Verify Profile was successfully created
--

SELECT
    PROFILE, RESOURCE_NAME, RESOURCE_TYPE, LIMIT
FROM
    DBA_PROFILES
WHERE
    PROFILE = 'PBRIANPROST';


--
-- 3. Create 2 users and assign them to the:
--    Permanent Tablespace of Users
--    Quota of 30M
--    Profile from step 1
--

CREATE USER U1BrianProst
    IDENTIFIED by "razHkXCVVXQ3eV!"
    DEFAULT TABLESPACE USERS
    QUOTA 30M on USERS
    PROFILE "PBRIANPROST"
    PASSWORD EXPIRE;

CREATE USER U2BrianProst
    IDENTIFIED by "n4i-98Ctjo@7jYf"
    DEFAULT TABLESPACE USERS
    QUOTA 30M on USERS
    PROFILE "PBRIANPROST"
    PASSWORD EXPIRE;


--
-- 4. Create a role allowing those users to connect to DB and create TABLES
--

CREATE ROLE R1BrianProst;
GRANT CONNECT, CREATE TABLE TO R1BrianProst;


--
-- 5. create two tables in root/admin schema containing
--

CREATE TABLE User1Data (
    album_record NUMBER(10) GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) NOT NULL,
    album_name VARCHAR2(128) NOT NULL,
    album_artist VARCHAR2(128) NOT NULL,
    release_date DATE NOT NULL,
    PRIMARY KEY(album_record)
);

CREATE TABLE User2Data (
    movie_record NUMBER(10) GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) NOT NULL,
    video_name VARCHAR2(128) NOT NULL,
    video_type VARCHAR2(64) NOT NULL,
    director_name VARCHAR2(128) NOT NULL,
    release_date DATE NOT NULL,
    PRIMARY KEY(movie_record)
);

-- insert records
-- insert records

INSERT INTO User1Data (album_name, album_artist, release_date) VALUES ('1984', 'Van Halen', '09-JAN-84');
INSERT INTO User1Data (album_name, album_artist, release_date) VALUES ('Gone Now', 'Bleachers', '02-JUN-17');
INSERT INTO User1Data (album_name, album_artist, release_date) VALUES ('The Rise and Fall of Ziggy Stardust and the Spiders From Mars', 'David Bowie', '06-JUN-72');

INSERT INTO User2Data (video_name, video_type, director_name, release_date) VALUES ('Free Churro - Bojack Horseman', 'TV Show', 'Amy Winfrey','14-SEP,18');
INSERT INTO User2Data (video_name, video_type, director_name, release_date) VALUES ('Tommy Boy', 'Movie', 'Peter Segal', '31-MAR-95');
INSERT INTO User2Data (video_name, video_type, director_name, release_date) VALUES ('Deadpool', 'Movie', 'Tim Miller', '12-FEB-16');


--
-- 6. Provide privileges to connect to the database and create tables
--

GRANT R1BrianProst TO U1BrianProst, U2BrianProst;

GRANT SELECT ON User1Data TO U1BrianProst;
GRANT INSERT ON User1Data TO U1BrianProst;

GRANT SELECT ON User1Data TO U2BrianProst;
GRANT SELECT ON User2Data TO U2BrianProst;