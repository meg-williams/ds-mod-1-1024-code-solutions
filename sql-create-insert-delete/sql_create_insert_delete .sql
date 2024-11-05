person_megan_williams

/* SQL create insert delete exercise*/

person_megan_williams

CREATE TABLE person_megan_williams
		(person_id INT, 
			first_name VARCHAR(20),
			last_name VARCHAR(20), 
			city VARCHAR(25), 
			CONSTRAINT pk_person_megan_williams PRIMARY KEY (person_id));

INSERT INTO person_megan_williams 
			(person_id, first_name, last_name, city)
VALUES
	(1, 'Megan', 'Williams', 'Lowell');
	
SELECT * FROM person_megan_williams;

INSERT INTO person_megan_williams 
			(person_id, first_name, last_name, city)
VALUES
	(2, 'Barbara', 'Morse', 'San Diego'), 
	(3, 'Cassandra', 'Cain', 'New York');
	
SELECT * FROM person_megan_williams;

ALTER TABLE person_megan_williams 
ADD gender VARCHAR(9);

UPDATE person_megan_williams 
SET gender = 'female'

ALTER TABLE person_megan_williams 
DROP COLUMN gender;

SELECT * FROM person_megan_williams;

DELETE FROM person_megan_williams WHERE person_id = 2;

DROP TABLE person_megan_williams;












