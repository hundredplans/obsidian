# Functions
## Math 
succ/pred -> Return num +/- 1
odd/even -> Return true if num is odd/even
round/floor/ceiling/truncate
\*\* -> Result can be a float

## Infix
- 5 `div` 10 -> Surround in backticks

# Weird Behaviour
- If statements require an else to function
- As if statements return a value surround them in () to work with that value
- e.g. (if x > 20 then x else x + 50) + 20
- Strings are lists of characters ['h','e','l','l','o']
- /= == !=

# GHCI
- Invoke with ghci
## Loading Functions
- :l myfunction
- :r -> Reloads whole script (and functions)
## Define Variables in GHCI
- let foo = bar
- Equivalent to loading in a variable from a script
## View  Operator Precedence
- :info (operator)
- infixl/infixr -> Read left to right if operator has higher preference
## Loading Modules
- :module/:m + module-name
## GHCI Specific Vars
- it -> Stores result of last function, doesn't change if last evaluation fails
## Set/Unset
### +t
- Lets you see the type of your command input
- Format is input :: Type
- Same as :type command
## GHCI Show
- :show bindings -> Show types of loaded variables

# Integers
- Bounded only by your system's memory capacity

# Rational Numbers (Fractions)
- Have to load Data.Ratio module
- 11%29 -> 11 divided by 29
- Both numbers have to be integers

# Types
- Type names start with uppercase character -> Char
- Var names start with lowercase character

## Different Types
- String/[Char]
- Chars
- Int
- Float
- List
- Tuple
- Num -> Something numeric int, float, ratio whatever

# Strings
- Single characters denoted by ' '
- Sequences of characters denoted by "text", under the hood is ['t', 'e', 'x', 't']
- "" is a synonym for []
- Since a string is a list this works -> 'a':"bc" abc / "foo" ++ "bar" foobar

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
- Takes a list and cycles it into an infinite list e.g. [1,2,3]
- If you try to display the result it will go on forever so you have to take somewhere
- Repeat takes one element and produces an infinite list of that element
- replicate num1 num2 -> Creates list of num1 size with element num2

# List Comprehensions
- [a | b, c, d] -> a -> Specify var, b -> Test that var against a list, c/d -> Test if var outputs true on condition
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

# Tuples
- Can contain multiple types, denoted by ()
- Tuples have a predefined size, each size is considered a different object by lists
- This is useful when storing vectors -> [(1,2),(7,11),(4,5)]
- Tuples containing one string and one number are also considered different objects to a tuple of two numbers
- Use Tuples when you know the types and how many components a piece of data should have

## Comparing Tuples
- fst (8, 11) -> Return first component
- snd (5, 20) -> Return second component
- The commands above only operate on pairs not triples or higher

## Zip
- zip list1 list2 -> Creates one list where each index becomes a tuple of the two values
- If the lists have different sizes the longer list gets cut off
- You can even zip infinite lists this way
