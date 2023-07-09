- Use folds whenever you want to traverse a list element by element and return something
- Recursively apply a combining function to the right-most or left-most value
- [5, 3, 2, 1] becomes [8, 2, 1] then [10, 1] then 11 if you're doing a right fold and adding
- When an element is returned the folding process stops
- Some examples below (foldr, foldl) 

sum' :: (Num a) => [a] -> a  
sum' xs = foldl (\acc x -> acc + x) 0 xs 

sum' :: (Num a) => [a] -> a  
sum' = foldl (+) 0 

- foldl (func with two args -> accumulator, current index) (starting value aka accumulator) (list to apply to)
- foldr (func with two args -> current index, accumulator) (starting value aka accumulator) (list to apply to)

map' :: (a -> b) -> [a] -> [b]  
map' f xs = foldr (\x acc -> f x : acc) [] xs

- Take each value and prepend (:) it to the accumulator
- e.g. xs = [6,1,2] func = (+3) -> 9:[] -> [9] -> 4:[9] -> [4, 9] -> 5:[4, 9] -> [5, 4, 9]
- We use foldr as we are prepending the values

- Left folds don't work on infinite lists but right folds do

- foldr1 and foldl1 work the same as usual folds but they assume the first or last index as the starting value
- As they require a value they cause runtime errors if it's not provided

f 3 (f 4 (f 5 (f 6 z))) is foldr of [3,4,5,6] with the starting value of z
