```php
array_pad($array, length, $var) # Fills array with length amount of $var
list($var1, $var2) = $array # Assign values of $array[0], $array[1] to $var 
print_r($array) # print raw

array_keys($array)
array_values($array)

# Same Thing
array_key_exists()
isset()

array_chunk($array, length) # split into array of arrays each length size

array_splice($array, begin, length, replace_array) # returns array from begin to length, and also modifies #array, replace_array is optional

extract($array) # Creates global vars of array key name with value
compact('var1', 'var2') # Creates dictionary based on vars

$array[] = "New Value" # Append
foreach ($array as $i) {}
array_walk($array, 'walk_func') # Runs value, key through a bool function
function walk_func($value, $key) {}

in_array(val, $array) # Value is inside 
array_search(val, $array) # Same as is_array

sort()
asort() # Value sort, arsort (reverse)
ksort() # Key sort, krsort (reverse)

array_flip()
array_diff($array, $array2, $array3)
array_sum()
array_merge($array, $array2, $array3) # Returns joining n arrays
array_filter()
array_map() # Can't change input values of array like array_walk, and returns new arr
```
