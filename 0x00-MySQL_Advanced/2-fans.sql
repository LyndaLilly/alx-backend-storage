--  this is the country's ranks origins, ordered by num of fans
SELECT origin AS origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
