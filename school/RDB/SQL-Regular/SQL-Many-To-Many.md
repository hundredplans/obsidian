```sql
CREATE TABLE Team (
    TeamID INT PRIMARY KEY,
    TeamName VARCHAR(255)
);

CREATE TABLE Staff (
    StaffID INT PRIMARY KEY,
    StaffName VARCHAR(255)
);

CREATE TABLE StaffTeam (
    StaffID INT,
    TeamID INT,
    PRIMARY KEY (StaffID, TeamID),
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID),
    FOREIGN KEY (TeamID) REFERENCES Team(TeamID)
);
```