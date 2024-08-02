```php
date("Y-m-d") # Year, month, day
date("H:i:s") # Hour, minute, second
mktime(0, 0, 0, 5, 10, 2024) # Returns linux time
getdate(mktime()) # Returns current time
strtotime() # Changes str to a date ("now", "18 march 2020")
checkdate() # Returns false if it doesn't exist
gmdate() # Same as date but in gmt
```