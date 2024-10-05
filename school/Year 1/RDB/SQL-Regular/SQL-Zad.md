```sql
SELECT Aircrafts_ID, Routes_flight_nr FROM Airports  
    JOIN Flights ON Flights.Routes_flight_nr = 69
```

Zad 6

7.1: 
```sql
SELECT COUNT(id_gry) as Amount, id_gry from oceny GROUP BY id_gry ORDER BY Amount
```

7.2:
```sql
SELECT gry.nazwa, ROUND(AVG(oceny.ocena), 2) AS AvgOcena
    FROM gry JOIN oceny ON gry.id_gry = oceny.id_gry
    WHERE kategoria='imprezowa'
    GROUP BY gry.id_gry
    ORDER BY AvgOcena
```

7.3:
```sql
SELECT COUNT(DISTINCT gracze.id_gracza) FROM gracze
    JOIN oceny ON gracze.id_gracza = oceny.id_gracza
    WHERE oceny.id_gracza NOT IN
        (SELECT oceny.id_gracza FROM gracze
        JOIN oceny on gracze.id_gracza = oceny.id_gracza
        WHERE stan = 'posiada')
```

7.4:
```sql
SELECT COUNT(oceny.id_gry) as Amount, nazwa FROM oceny JOIN gry ON gry.id_gry = oceny.id_gry  
    WHERE oceny.id_gracza IN (SELECT id_gracza FROM gracze WHERE wiek BETWEEN 50 AND 99)  
    GROUP BY oceny.id_gry ORDER BY Amount
```