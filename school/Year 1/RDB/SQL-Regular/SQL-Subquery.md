```sql
SELECT * FROM Cars WHERE make in (SELECT DISTINCT make FROm Cars WHERE year<1972)
-- Select distinct is kind of like creating an array and then searching what matches
SELECT * FROM CARS WHERE year < (SELECT AVG(year) FROM Cars) 
-- Repeat doesn't matter
```

```sql
SELECT * FROM Cars WHERE make IN ('Ford', 'Dodge') -- Mixes the data
--
SELECT * FROM Cars WHERE make='Ford'
UNION
SELECT * FROM Cars WHERE make='Dodge'
AS NewTabela -- Can treat it as a new table
-- Joins but doesn't mix the data
```