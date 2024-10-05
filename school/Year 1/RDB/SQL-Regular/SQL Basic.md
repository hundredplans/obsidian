Structured Query Language

```sql
SELECT make, model, year, VIN FROM CARS;
SELECT make, model, year, VIN FROM Cars WHERE make="Ford";
SELECT make, model, year, VIN FROM Cars WHERE make="Ford" AND model="F150";
SELECT make, model, year, VIN FROM Cars WHERE make="Ford" AND model="F150" ORDER BY year;
WHERE make IN ('Ford', 'Dodge', 'Pontiac')
WHERE year BETWEEN 1995 AND 1999
```
```
Operatory logiczne
    AND
    OR
    NOT

Operatory porównawcze
    = - równy
    < - mniejszy
    > - większy
    <= - mniejszy lub równy
    >= - większy lub równy
    <> - nierówny
```