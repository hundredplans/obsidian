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
- [ ] -> List of any types
- Ordering -> Returns an enum of LT, EQ, GT
- Either a b -> Definas Left a | Right b deriving (Eq, Ord, Read, Show) -> Used to capture two values and match either Left or Right
- Empty -> Used to define Empty lists
- ReadS -> Type declaration of: String -> [(a, String)]

## What Types Are
- Types are labels that values (including funcs) carry to reason about their values
- Types have their own labels called Kinds
- You can examine the Kind of a type by using :k Type

### Kinds
- * -> Concrete type, values can only be concrete types, doesn't take any parameters
- * -> * -> Takes one concrete type and returns a concrete type, used for Maybe (without a)
- * -> * -> * -> Takes two concrete types and returns a concrete type, used for Either (without a b)
