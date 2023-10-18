-- script that lists the umber of records with the same score
-- USING NUMBER and COUNT and GROUPE BY
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
