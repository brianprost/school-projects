-- Brian Prost
-- Project 3

SELECT * FROM RENTAL WHERE rental_date >= '2021-03-01' order by rental_date ASC; -- assuming chronological order means first entry is the least recent, if not, use DESC instead