```sql
ALTER TABLE TableName ADD COLUMN column_name DataType 
ALTER TABLE TableName ADD COLUMN 'car_id' INT
```

```sql
ALTER TABLE TableName ADD CONSTRAINT FOREIGN KEY (column_name) REFERENCES TableName2(column_name)
ALTER TABLE TableName ADD CONSTRAINT FOREIGN KEY ('id') REFERENCES TableName2('id')
```

```sql
ALTER TABLE TableName DROP COLUMN column_name // Removes the column
```

```sql
ALTER TABLE TableName ADD CONSTRAINT PRIMARY KEY (column_name)
```