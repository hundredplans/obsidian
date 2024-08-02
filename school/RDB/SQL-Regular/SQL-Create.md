```sql
CREATE TABLE TableName (
	name VARCHAR(16) NOT NULL DEFAULT 'John',
	lastName VARCHAR(64) DEFAULT 'Doe',
	PESEL CHAR(11) PRIMARY KEY,
	age INT CHECK(age>=18),
	gender ENUM('male', 'female', 'other') NOT NULL,
)
```
# Constraints
- NOT NULL -> Has to be specified
- UNIQUE -> Each value has to be unique
- DEFAULT 'value' -> Takes a value when not specified
- CHECK (predicate) -> Doesn't accept entry if check not fulfilled
- PRIMARY KEY -> Equal to NOT NULL UNIQUE

[[SQL-Insert]]
[[SQL-Alter]]
![[select-add.png]]