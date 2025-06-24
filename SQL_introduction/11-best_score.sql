-- Select the best
SELECT score, name FROM second_table
WHERE score BETWEEN 10 AND 14
ORDER BY score DESC;