-- create a table unique_id with id as an integer that is unique and name as a varchar of 256 characters
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
