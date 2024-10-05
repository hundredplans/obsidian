Used to update a database as one thing
```sql
START TRANSACTION
-- Any inserts / deletes / show / Anything goes here, treated as one thing when it ends
-- Use even for single inserts / deletes
COMMIT / ROLLBACK -- Rollback ends the transaction
```