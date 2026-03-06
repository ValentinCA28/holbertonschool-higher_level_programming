-- create a table id_not_null with id as an integer that cannot be null and name as a varchar of 256 characters
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR (256)
);
