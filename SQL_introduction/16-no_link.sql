-- displays the score and name of all records in second_table where name is not NULL and not empty, ordered by score (top first)
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
