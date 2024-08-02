```php
strlen($str)

trim($str) # Removes whitespace from beginning and end
trim($str, " ") # Don't trim specific characters

htmlentities("Ü") # Changes illegal characters to a valid html one, this becomes &Uuml
htmlspecialchars("<>&") # ;&lt;&gt
striptags("<p>Some text</p>") # Removes html tags

3 === "3" # Check if values are equivalent and equivalent type
$str1 < $str2 # Compares strlen? 
strcmp($str1, $str2) # -1 if second is >, 0 if both equal, 1 if first is > 
similar_text($str1, $str2) # Returns how equal two strings are
levenshtein($str1, $str2) # Returns how different two strings are

substr($str1, offset, length) # -offset returns from end, length is max characters
substr_count($str1, "wa") # How many of specified string occur in $str1
substr_replace($str1, "ara", offset, length) # Offset is where to begin
strrev($str1) # Reverses string

str_repeat($str1, amount)
$array = explode(",", "str1,str2") # Returns array of string from delimiter
$znaki = implode(":", $array) # Returns string from array

$token = strtok("a b c", " ") # Token set to a
$token = strtok(" ") # Sets token to b 

$int = strpos("water", "w") # Returns position of first element
strstr("anytextany", "y", length) # Returns string starting from after found character 
```