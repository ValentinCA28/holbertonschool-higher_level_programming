-- displays the score and number of records for each score in second_table, ordered by number of records (most first)
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
