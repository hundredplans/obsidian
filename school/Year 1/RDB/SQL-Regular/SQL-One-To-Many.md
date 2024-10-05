```sql
CREATE TABLE Team (
    TeamID INT PRIMARY KEY,
    TeamName VARCHAR(255)
);

CREATE TABLE Staff (
    StaffID INT PRIMARY KEY,
    StaffName VARCHAR(255),
    TeamID INT,
    FOREIGN KEY (TeamID) REFERENCES Team(TeamID)
);
```