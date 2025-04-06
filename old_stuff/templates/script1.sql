-------------------- PART 1 ----------------------------------------
CREATE TABLE countries (
  country_code char(2) PRIMARY KEY,
  country_name text UNIQUE
  );

INSERT INTO countries (country_code, country_name)
VALUES ('us', 'United States'),
       ('mx', 'Mexico'),
       ('au', 'Australia'),
       ('gb', 'United Kingdom'),
       ('de', 'Germany');

select * from countries

insert into countries VALUES ('us', 'United States') -- country name already exists!

delete from countries
where country_code = 'de';

------------------------------------------------------------------------------------------

CREATE TABLE cities (
  name text NOT NULL,
  postal_code varchar(9) CHECK (postal_code <> ''),
  country_code char(2) REFERENCES countries,
  PRIMARY KEY (country_code, postal_code)
  );

INSERT INTO cities
VALUES ('Toronto', 'M4C1B5', 'ca');

insert into countries VALUES ('ca', 'Canada') 

insert into cities
VALUES ('Portland', '97206', 'us');

SELECT cities.*, country_name
FROM cities INNER JOIN countries /* or just FROM cities JOIN countries */
ON cities.country_code = countries.country_code;

------------------------------------------------------------------------------------------

CREATE TABLE venues (
  venue_id SERIAL PRIMARY KEY,
  name varchar(255),
  street_address text,
  type char(7) CHECK ( type in ('public', 'private') ) DEFAULT 'public',
  postal_code varchar(9),
  country_code char(2),
  FOREIGN KEY (country_code, postal_code)
  REFERENCES cities (country_code, postal_code) MATCH FULL
  );

INSERT INTO venues (name, postal_code, country_code)
VALUES ('Crystal Ballroom', '97206', 'us');

INSERT INTO venues (name, postal_code, country_code)
VALUES ('Voodoo Donuts', '97206', 'us') RETURNING venue_id;

------------------------------------------------------------------------------------------

CREATE TABLE events (
  event_id SERIAL PRIMARY KEY,
  title text NOT NULL,
  starts timestamp,
  ends timestamp,
  venue_id integer,
  FOREIGN KEY (venue_id) REFERENCES venues
  );

INSERT INTO events (title, starts, ends, venue_id)
VALUES ('LARP Club', '2012-02-15 17:30:00', '2012-02-15 19:30:00', 5);

INSERT INTO events (title, starts, ends)
VALUES ('April Fools Day', '2012-04-01 00:00:00', '2012-04-01 23:59:00'),
       ('Christmas Day', '2012-12-25 00:00:00', '2012-02-25 23:59:00');

SELECT e.title, v.name
FROM events e JOIN venues v -- 'INNER' is not required
ON e.venue_id = v.venue_id;

SELECT e.title, v.name
FROM events e LEFT JOIN venues v -- Retrieving all events with/without a venue
ON e.venue_id = v.venue_id;

------------------------------------------------------------------------------------------

CREATE INDEX events_title ON events USING hash (title);
CREATE INDEX events_starts ON events USING btree (starts);

-------------------- PART 2 ----------------------------------------

-- Delete data from "events" table
DELETE FROM events;

-- Delete data from "venues" table
DELETE FROM venues;

-- Delete data from "cities" table
DELETE FROM cities;

-- Delete data from "countries" table
DELETE FROM countries;


-- Insert countries
INSERT INTO countries (country_code, country_name) VALUES
  ('US', 'United States');

-- Insert cities
INSERT INTO cities (name, postal_code, country_code) VALUES
  ('Cityville', '12345', 'US'),
  ('Artland', '23456', 'US'),
  ('Conftown', '34567', 'US'),
  ('Foodville', '45678', 'US'),
  ('Music City', '56789', 'US'),
  ('Booktown', '67890', 'US'),
  ('Photoville', '78901', 'US'),
  ('Fashionville', '89012', 'US'),
  ('Communitytown', '90123', 'US'),
  ('Cinemacity', '01234', 'US');


-- Venue 1
INSERT INTO venues (venue_id, name, street_address, type, postal_code, country_code)
VALUES (1, 'Fitness Center', '123 Main St', 'public', '12345', 'US');

-- Venue 2
INSERT INTO venues (venue_id, name, street_address, type, postal_code, country_code)
VALUES (2, 'Art Gallery', '456 Art Ave', 'public', '23456', 'US');

-- Venue 3
INSERT INTO venues (venue_id, name, street_address, type, postal_code, country_code)
VALUES (3, 'Conference Center', '789 Conference Rd', 'public', '34567', 'US');

-- Venue 4
INSERT INTO venues (venue_id, name, street_address, type, postal_code, country_code)
VALUES (4, 'Tasting Hall', '101 Flavor St', 'public', '45678', 'US');

-- Venue 5
INSERT INTO venues (venue_id, name, street_address, type, postal_code, country_code)
VALUES (5, 'Music Park', '555 Melody Ln', 'public', '56789', 'US');

-- Venue 6
INSERT INTO venues (venue_id, name, street_address, type, postal_code, country_code)
VALUES (6, 'Bookstore', '222 Literary St', 'public', '67890', 'US');

-- Venue 7
INSERT INTO venues (venue_id, name, street_address, type, postal_code, country_code)
VALUES (7, 'Photography Studio', '777 Shutter Rd', 'public', '78901', 'US');

-- Venue 8
INSERT INTO venues (venue_id, name, street_address, type, postal_code, country_code)
VALUES (8, 'Fashion Mall', '888 Style Blvd', 'public', '89012', 'US');

-- Venue 9
INSERT INTO venues (venue_id, name, street_address, type, postal_code, country_code)
VALUES (9, 'Community Center', '333 Charity Ave', 'public', '90123', 'US');

-- Venue 10
INSERT INTO venues (venue_id, name, street_address, type, postal_code, country_code)
VALUES (10, 'Cinema Complex', '444 Film St', 'public', '01234', 'US');


-- Event 1
INSERT INTO events (title, starts, ends, venue_id) VALUES ('Tech Conference', '2023-08-27 09:00:00', '2023-08-27 17:00:00', 1);

-- Event 2
INSERT INTO events (title, starts, ends, venue_id) VALUES ('Art Exhibition', '2023-09-10 10:30:00', '2023-09-10 18:00:00', 1);

-- Event 3
INSERT INTO events (title, starts, ends, venue_id) VALUES ('Music Festival', '2023-09-15 14:00:00', '2023-09-17 23:59:00', 2);

-- Event 4
INSERT INTO events (title, starts, ends, venue_id) VALUES ('Fitness Workshop', '2023-09-02 08:30:00', '2023-09-02 11:00:00', 2);

-- Event 5
INSERT INTO events (title, starts, ends, venue_id) VALUES ('Food Tasting', '2023-09-08 18:00:00', '2023-09-08 20:30:00', 3);

-- Event 6
INSERT INTO events (title, starts, ends, venue_id) VALUES ('Book Launch', '2023-09-12 16:00:00', '2023-09-12 18:00:00', 3);

-- Event 7
INSERT INTO events (title, starts, ends, venue_id) VALUES ('Fashion Show', '2023-09-20 19:30:00', '2023-09-20 21:30:00', 3);

-- Event 8
INSERT INTO events (title, starts, ends, venue_id) VALUES ('Workshop: Photography Basics', '2023-09-05 11:00:00', '2023-09-05 13:30:00', 4);

-- Event 9
INSERT INTO events (title, starts, ends, venue_id) VALUES ('Charity Gala', '2023-09-18 18:30:00', '2023-09-18 23:00:00', 5);

-- Event 10
INSERT INTO events (title, starts, ends, venue_id) VALUES ('Film Screening', '2023-09-25 20:00:00', '2023-09-25 22:30:00', 6);

INSERT INTO events (title, starts, ends) VALUES ('No venue', '2023-09-25 20:00:00', '2023-09-25 22:30:00');

INSERT INTO events (title, starts, ends) VALUES ('Day 1 holiday', '2023-09-25 20:00:00', '2023-09-25 22:30:00');


-- Aggregate Functions
SELECT COUNT(*) AS total_events FROM events;

SELECT AVG(ends - starts) AS average_duration FROM events;

SELECT MIN(starts) AS earliest_start, MAX(starts) AS latest_start FROM events;

SELECT SUM(ends - starts) AS total_duration FROM events;

SELECT venue_id, COUNT(*) AS event_count
FROM events
GROUP BY venue_id
ORDER BY event_count DESC
LIMIT 1;

-- Grouping
select venue_id, count(*) from events
group by venue_id

-- Group Events by Venue and Count the Number of Events at Each Venue
SELECT venue_id, COUNT(*) AS event_count
FROM events
GROUP BY venue_id
ORDER BY event_count DESC;

-- Group Events by Year and Count the Number of Events in Each Year
SELECT EXTRACT(YEAR FROM starts) AS event_year, COUNT(*) AS event_count
FROM events
GROUP BY event_year
ORDER BY event_year;

-- Group Events by Month and Count the Number of Events in Each Month
SELECT EXTRACT(MONTH FROM starts) AS event_month, COUNT(*) AS event_count
FROM events
GROUP BY event_month
ORDER BY event_month;

-- Group Events by Venue and Calculate the Total Duration of Events at Each Venue:**
SELECT venue_id, SUM(ends - starts) AS total_duration
FROM events
GROUP BY venue_id
ORDER BY total_duration DESC;

-- Window functions
SELECT venue_id, starts, ends, COUNT(*) OVER (PARTITION BY venue_id)
FROM events

--Transaction
-- Begin a transaction
BEGIN;

-- Attempt to delete events
DELETE FROM events WHERE venue_id = 1;

-- Check the deleted rows
SELECT * FROM events WHERE venue_id = 1;

-- Rollback the transaction
ROLLBACK;
-- COMMIT

-- Stored Procedures
CREATE OR REPLACE FUNCTION add_event(
  title text,
  starts timestamp,
  ends timestamp,
  venue text,
  postal varchar(9),
  country char(2))
RETURNS boolean AS $$
DECLARE
  did_insert boolean := false;
  found_count integer;
  the_venue_id integer;
BEGIN
  SELECT venue_id INTO the_venue_id
  FROM venues v
  WHERE v.postal_code=postal AND v.country_code=country AND v.name ILIKE venue
  LIMIT 1;

  IF the_venue_id IS NULL THEN
    INSERT INTO venues (name, postal_code, country_code)
    VALUES (venue, postal, country)
    RETURNING venue_id INTO the_venue_id;

    did_insert := true;
  END IF;

  -- Note: this is a notice, not an error as in some programming languages
  RAISE NOTICE 'Venue found %', the_venue_id;

  INSERT INTO events (title, starts, ends, venue_id)
  VALUES (title, starts, ends, the_venue_id);

  RETURN did_insert;
END;
$$ LANGUAGE plpgsql;

select add_event('House Party', '2018-05-03 23:00', '2018-05-04 02:00', 'Run''s House', '12345', 'US');
--------------------------

CREATE OR REPLACE FUNCTION calculate_duration_avg(
  ven_id integer
	)
RETURNS interval AS $$
DECLARE
    duration interval;
BEGIN
SELECT AVG(ends - starts) into duration
FROM events
WHERE venue_id = ven_id;
return duration;
END;
$$ LANGUAGE plpgsql;

select calculate_duration_avg(1)

-- compare the result of the above function to the below script when venue_id = 1
SELECT AVG(ends - starts)
FROM events
WHERE venue_id = 1

-- Triggers
CREATE TABLE logs (
  event_id integer,
  old_title varchar(255),
  old_starts timestamp,
  old_ends timestamp,
  logged_at timestamp DEFAULT current_timestamp
  );

  CREATE OR REPLACE FUNCTION log_event() RETURNS trigger AS $$
DECLARE
BEGIN
  INSERT INTO logs (event_id, old_title, old_starts, old_ends)
  VALUES (OLD.event_id, OLD.title, OLD.starts, OLD.ends);
  RAISE NOTICE 'Someone just changed event #%', OLD.event_id;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER log_events
 AFTER UPDATE ON events
FOR EACH ROW EXECUTE PROCEDURE log_event();

UPDATE events SET ends = '2012-05-04 01:00:00' WHERE title = 'House Party';

--Views
CREATE VIEW upcoming_events AS
SELECT event_id, title, starts
FROM events
WHERE starts > NOW();

select * from upcoming_events

CREATE VIEW holidays AS
  SELECT event_id AS holiday_id, title AS name, starts AS date
  FROM events
  WHERE title LIKE '%Day%' AND venue_id IS NULL;

select * from holidays

UPDATE holidays SET name ='Holiday 2' where name = 'Day 1 holiday'; -- Error!

--Rules
--holidays is a view, to enable update, we define a rule
CREATE RULE update_holidays AS ON UPDATE TO holidays DO INSTEAD
  UPDATE events
  SET title = NEW.name,
      starts = NEW.date,
  WHERE title = OLD.name;

-------------------- PART 3 ----------------------------------------
-- Run the movies scripts first
-- -- movies_data.sql
-- -- movies_schema.sql

--Install pacakges
create extension if not exists tablefunc
create extension if not exists fuzzystrmatch
create extension if not exists cube

select * from pg_extension where extname = 'tablefunc'
-- Like and ILIKE
select title from movies where title ilike 'stardust%'
select title from movies where title ilike 'star%'
select title from movies where title ilike 'stard___'

--regex
SELECT COUNT(*) FROM movies WHERE title !~* '^the.*';

--LEVENSHTEIN
SELECT 'kitten', 'sitting', LEVENSHTEIN('kitten', 'sitting')
SELECT movie_id, title FROM movies WHERE levenshtein(lower(title), 'a hard day nght') < 3;


-- Full Text and multidimensions
select title, to_tsvector(title) from movies; 

Select title 
from movies
where title @@ 'night & day';

--cube
select name, cube_ur_coord('(0,7,0,0,0,0,0,0,0,7,0,0,0,0,10,0,0,0)', position) as score
from genres G
where cube_ur_coord('(0,7,0,0,0,0,0,0,0,7,0,0,0,0,10,0,0,0)', position) > 0;

select *, cube_distance(genre, '(0,7,0,0,0,0,0,0,0,7,0,0,0,0,10,0,0,0)') dist
from movies
order by dist;

CREATE TABLE spatial_data (
    id serial PRIMARY KEY,
    point_data cube
);

INSERT INTO spatial_data (point_data) VALUES ('(1, 2, 3)');
INSERT INTO spatial_data (point_data) VALUES ('(4, 5, 6)');
-- You can insert more data as needed

-- Calculate the distance between two 3D points
-- the <-> operator calculates the distance between the stored 3D points and the specified point (2, 3, 4).
SELECT point_data <-> '(2, 3, 4)' AS distance
FROM spatial_data;
