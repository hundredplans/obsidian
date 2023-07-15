# Data.List
numUniques list -> Returns amount of unique elements in list
nub list -> Returns a list with all duplicate elements removed
intersperse elem list -> Place new elem index after each element in list
intercalate list 2Dlist -> Insert list between each list of 2Dlist and flatten the result
transpose 2Dlist -> Create new lists consisting of each index from each list
foldl'/foldr' -> Non-lazy, use when you get stack overflow errors
concat 2Dlist -> Flattens list (only one level)
concatMap func list -> Apply func that returns a list to each element in list then flatten the list
iterate func val -> Apply function to value infinitiely and return an infinite list -> iterate (\*5) 3 [3, 15, 75..]
splitAt num list -> Return list as two tuples, one containing 0-n and the other as n+1 end
takeWhile predicate list -> Take elements from a list while predicate holds True
dropWhile predicate list -> Return the list from where predicate is False
span predicate list -> Works like takeWhile but returns two lists, first is all elements while predicate held True, second is all other elements
break predicate list -> Same as span but breaks when predicate is True, first element of second list is when predicate changed to True
sort list -> Sort a list of Ord typeclass
group list -> Returns a list of lists where equal elements are grouped [1,1,2,3,3] -> [[1,1],[2],[3,3]]
inits list -> inits "w00t" -> ["", "w", "w0", "w00", "w00t"]
tails list -> tails "w00t" -> ["w00t", "w00", "w0", "w", ""]
isInfixOf list list2 -> Search for sub-list list inside list2
isPrefixof/isSuffixOf list list2 -> Sane as isInfixOf but at the start/end respectively
elem/notElem -> Return True if element is/isn't in list
partition predicate list -> Return a tuple of two lists, based on whether the element satisfies the predicate

find predicate list -> Return first element that satisfies list, as a Maybe type (Just elem or Nothing)
elemIndex element list -> Return first element that matches condition, as a Maybe type
findIndex/findIndices predicate list -> Return first/all elements that match condition, findIndex return element as a Maybe type

zipWith3 func list1 list2 list3 -> Works same as zipWith but for 3 elements, goes up to 7 (zipWith7)
zip3 list1 list2 list3 -> Works same as zip but for 3 elements, goes up to 7 (zip7)

lines string -> Return seperate lines as seperate elements in a list (uses \n) -> "Hello \nmy name is" -> ["Hello", "my name is"]
unlines list -> Return string from a list of strings (using \n) -> ["hello", "my name is"] -> "Hello\nmy name is"
words/unwords list -> Same as lines/unlines but with words

delete elem list -> Delete first occurence of element in list

list1 \\ list2 -> Set difference, remove first occurence of each element in list2 in list1
union list1 list2 -> Append all non duplicates from list2 to list1, removes all duplicates in list2
interesect list1 list2 -> Return elements found in both lists

insert elem list1 -> Place an element inside a list where it is equal to or greater than the next element (list of numbers) -> insert 4 [3,5,6,3] -> [3,4,5,6,3]

genericTake, genericDrop, genericSplitAt, genericLength, genericIndex (!!), genericReplicate -> Don't only take Int values but Ord/Num typeclass
nubBy, deleteBy, unionBy, intersectBy, groupBy -> Take equality function rather than no argument -> func arg -> funcBy (==) arg || Those are the same
sortBy, insertBy, maximumBy, minimumBy -> Take ordering function rather than no argument (GT/LT/EQ)

When dealing with equality functions use (==) `on` something
When dealing with ordering functions use compare `on` something`

## Conditionals
and listbool -> Return true if all values in list are True (and $ map (>4) [5, 6]) is a good example
or listbool -> Returns true if any value in a list is True
any predicate list -> Return true if any element satisfies predicate
all predicate list -> Return true if all elements in list satisfy predicate

