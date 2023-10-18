-- script that lists all recordes with a score >= 10
--recods should be ordered by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
