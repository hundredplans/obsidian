# Types
- Type names start with uppercase character -> Char
- Var names start with lowercase character
- :t var -> Infers var type

## Explicit Type Declaration
- :: [Char] -> Is of type [Char]
- func :: Int -> Int -> [Char] -> Defines multiple args
- Return type is the last item in the declaration
- Can be used on funcs or at the end of an expression e.g. read "5" :: Int
- To declare Tuple type use :: (Bool, [Char])
## Type Constraints
- func :: (Integral a) => a -> String
    - Only run func if given value is an Integral and return a String
- Type Constraints use =>, Specificing function types uses ->

## Different Types
- String/[Char]
- Char (denoted by ' ')
- Int (32-bit/64-bit depends on native integer)
- Integer (infinite but less efficient than int, can't overflow)
- Float (32-bit)
- Double (64-bit and very fast)
- Bool
- List
- Tuple (infinite amount of types, () is an empty tuple type)
- a/b/c/d -> Represent any type, usually use single letter to denote themself but could be any [Char]
- [a] -> List of any types

## Typeclasses
- Eq -> Any type which can be equally compared can be of the Eq class
    - All Eq types use == or /= in their definition
- Ord -> Types that have an ordering
- Show -> Types that can be presented as strings
- Read -> Types that can be turned into non-strings
- Enum -> Types that can be enumerated
- Bound -> Types that have an upper and lower bound (Tuples are bounded if the types inside are
- Num -> Types that can act like a number
- Floating/Integral -> Float/Double & Int/Integer
- Maybe Type -> Can either be one element or nothing, similar to empty lists
