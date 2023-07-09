# Data.List
numUniques list -> Returns amount of unique elements in list
nub list -> Returns a list with all duplicate elements removed
intersperse elem list -> Place new elem index after each element in list
intercalate list 2Dlist -> Insert list between each list of 2Dlist and flatten the result
transpote 2Dlist -> Create new lists consisting of each index from each list
foldl'/foldr' -> Non-lazy, use when you get stack overflow errors
concat 2Dlist -> Flattens list (only one level)
concatMap func list -> Apply func that returns a list to each element in list then flatten the list

## Conditionals
and listbool -> Return true if all values in list are True (and $ map (>4) [5, 6]) is a good example
or listbool -> Returns true if any value in a list is True
any predicate list -> Return true if any element satisfies predicate
all predicate list -> Return true if all elements in list satisfy predicate

