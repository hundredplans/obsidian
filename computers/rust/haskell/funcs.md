# Functions
- compare a b -> Return an ordering (first value compared to second)
    - EQ -> Equal
    - LT -> Lesser than
    - GT -> Greater than

- show a -> Return value as String if it's part of the Show typeclass
- read a -> Takes a string and a non-string if it's part of the Read typeclass
- id -> Return passed argument unchanged

## Higher-Order Functions
- Functions that can take functions as arguments or return functions
max :: (Ord a) => a -> (a -> a)
- Max takes an a and returns a function that takes an a that returns an a
- You can create custom functions like so
compareWithHundred x = compare 100 x
- Short form method
compareWithHundred = compare 100

## Infix Curried-Functions

divideByTen :: (Floating a) => a -> a  
divideByTen = (/10)  

- You can use infix functions with Curried functions by surrounding the equation in ()
- And leaving one side of the infix empty

isUpperAlphanum :: Char -> Bool  
isUpperAlphanum = (`elem` ['A'..'Z'])  

## Type Declaration on Functions with Return Values    

applyTwice :: (a -> a) -> a -> a  
applyTwice f x = f (f x)  

- applyTwice takes a function that takes something and returns the same value
- applyTwice then takes another parameter of the same type and returns something of the same type
e.g. 
1. applyTwice :: (String -> String) -> String -> String
2. applyTwice (++ " HAHA") "HEY"  
   "HEY HAHA HAHA" 

- Functions that accept a -> b -> c will also accept a -> b -> c

## Maps
- Apply a function to each item in a list
- Applied recursively
map :: (a -> b) -> [a] -> [b] -- take a function that returns type b
map _ [] = []  
map f (x:xs) = f x : map f xs 

- Use List Comprehensions for when you're dealing with more than one function application per element

## Filters
- Filter takes a predicate (True or False) and returns all elements that satisfy the predicate

## Cool Example
sum (takeWhile (<10000) (filter odd (map (^2) [1..])))
sum (takeWhile (<10000) [n^2 | n <- [1..], odd (n^2)])

- The above example are identical

let listOfFuns = map (\*) [0..]
- Produces a list of [(0\*), (1\*)..]
- If you get a value you can apply the \* -> (listOfFuns !! 4) 5 -> Returns 20 same as writing (4\*) 5 || 4 \* 5

- flip f x y -> Takes a function of two arguments and returns a new function with the arguments flippedgt

# Creating Infix Operators
- infixr/l precedence (operator precedence num) operator
- Operator becomes automatically infixed
- Precedece is optional

# Weird Functions
(,) same as \x y -> (x, y)
(,,) same as \x y z -> (x,y,z)
