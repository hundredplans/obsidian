- Similar to folds but creates a list of each result

scanl (+) 0 [3,5,2,1] -> scanl (function to apply) (starting value) (apply function on each element of provided list)
[0,3,8,10,11]

scanr (+) 0 [3,5,2,1]
[11,10,8,3,0]

- Also have scanl1 and scanr1 which are identical to foldx1 (don't take starting value, assume first elem (or last) is starting value)

- If the previous value was lower replace it with a higher value
scanl1 (\acc x -> if x > acc then x else acc) [3,4,5,3,7,9,2,1]  
[3,4,5,5,7,9,9,9]

- scanl final result will be last
- scanr final result will be first
