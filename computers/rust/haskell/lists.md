# Lists
- Can either be a list of numbers or of characters
## Appending Lists
- [3,5] ++ [6,6] -> [3,5,6,6]
- Slower than inserting at front
- Can only append between two lists
## Insert at Front
- 5:[9,5]
- Works for both lists and single characters
- Quicker than appending
- 5: [3,6] returns [5,3,6] // [5,9]:[3,6] returns [5,9,3,6]
## Specifying Index
- list !! index
## List within a List
- Can be of different lengths but not of different types
## Comparing Lists
- Each element is compared with each element in another list
- Starts at index 0 and moves throughout
## List Functions
- head list -> returns index 0
- tail list -> chops off index 0 and returns the remainder list
- last list -> returns last index of list
- init list -> returns everything except last
- length list -> returns list length
- null list -> returns if list is empty (True if null)
- reverse list -> returns a reversed list
- take num list -> returns index 0 to index num - 1
    - when num is 0 returns an empty list
- drop num list -> returns list with the first n elements removed
- maximum list -> returns biggest element in list
- minimum list -> returns smallest element in list
- sum list -> returns the sum of the list
- product list -> returns a product of the list
- elem num/char list -> returns true if num/char is inside the list
- Do not use the above functions on empty lists as it errors
- show list -> Return a string from value e.g. 121 returns ['1', '2', '1']

## Texan Ranges
- [1..20] represents 1-20 in a list
- ["a".."r"] represents a-r in a list
- [3,6..20] every third number from 3-20 (excluding 20)
- [20,19..1] to get a negative range
- Do not use floats as they're imprecise
- create an infinite range using [10,20..]
- take 24 [13,26,..] creates a list that is 24 long

## Cycle/Repeat/Replicate
- Cycle -> Takes a list and cycles it into an infinite list e.g. [1,2,3]
    - If you try to display the result it will go on forever so you have to take somewhere
- Repeat -> Takes one element and produces an infinite list of that element
- Replicate num1 num2 -> Creates list of num1 size with element num2

# List Comprehensions
- [a | b, c, d] -> a -> Specify var, b -> Test that var against a list, c/d -> return true if all predicates are matched
- [x\*2 | x <- [1..10]] -> For each element from 1 to 10 return x \* 2 and create a list of [2..20]
- [x\*2 | x <- [1..10], x\*2 >= 12] -> The last part is called the condition/predicate
- Weeding out lists by predicates is called filtering
- An element is only included in the list if all the predicates evaluate to true
- You can include many predicates seperated by commas [x | x <- [5..10], x > 6, x\*5 > 30]
- You can include many lists, the amount of outputs for list x, y is x\*y
- Many list example -> [x\*y | x <- [1..3], y <- [4..6]] returns all product of x, y from lists
- _ is the default for unused vars -> sum [1 | _ <- xs] -> Replaces every element of a list with 1 and sums it
- Strings are lists -> removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]
- You can nest list comprehensions for lists that contain lsits
    - [ [ x | x <- xs, even x ] | xs <- xxs]

# New Notes
- (x:xs) -> Match anything that's a non-empty list, x is first element, xs is tail
- To take first three vars out of a list do x:y:z:xyz where xyz is a list of size 3 or more
- takeWhile(predicate) -> While predicate is true return take, useful for infinite lists
