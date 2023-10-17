A data structure that supports efficient appending
Works by being a list that prepends another list
``` 
List example [1,2,3]
Difference List Equivalent -> \xs -> [1,2,3] ++ xs
Empty Difference List -> \xs -> [] ++ xs
```
To append using difference lists f \`append\` g = \\xs -> f (g xs)
equivalent to \\xs -> "string" ++ ("string2" ++ xs) where f is "string" and g is "string" (remember lists are functions too)
