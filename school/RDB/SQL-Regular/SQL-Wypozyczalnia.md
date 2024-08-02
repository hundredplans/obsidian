```sql
CREATE TABLE Pracownicy (  
    pracownik_id int PRIMARY KEY,  
    first_name varchar(20),  
    last_name varchar(30),  
    age int  
)

CREATE TABLE Clients (
    client_id  int PRIMARY KEY,  
    first_name varchar(20) NOT NULL,  
    last_name  varchar(30) NOT NULL,  
    PESEL      char(11)    NOT NULL UNIQUE  
)

CREATE TABLE Cars (  
    car_id int PRIMARY KEY,  
    color VARCHAR(10) NOT NULL,  
    brand varchar(20) NOT NULL  
)
CREATE TABLE Wypozyczenie(  
    wypozyczenie_id int PRIMARY KEY,  
    FOREIGN KEY (pracownik_id) REFERENCES Pracownicy(pracownik_id),  
    FOREIGN KEY (client_id) REFERENCES Clients(client_id),  
    FOREIGN KEY (car_id) REFERENCES Cars(car_id),  
    date DATE NOT NULL,  
    godzina_start int NOT NULL,  
    CHECK(godzina_start BETWEEN 0 AND 24),  
    godzina_end int NOT NULL,  
    CHECK(godzina_end BETWEEN 0 and 24),  
    cost int NOT NULL  
)
```