import Data.Monoid
Monoids are a Typeclass in Haskell

# What are Monoids?
\* and ++ have some common properties
- They take two parameters and produce an output (binary function, often curried)
- Parameters and returned values have the same type
- There's a value that causes no change to occur (e.g. x \* 1 = x, \[] ++ \["C"] = \["C"]) (identity)
- The order in which the function is applied doesn't affect the outcome (associativity)

Monoids are an associative binary function (two inputs) with a value which acts as an identity with respect to that function (\[] for ++, 1 for \*)

# Monoid Typeclass Definition
```haskell
class Monoid m where
    mempty :: m
    mappend :: m -> m -> m
    mconcat :: [m] -> m
    mconcat = foldr mappend mempty
```

mempty is the identity function
mappend is the binary function (takes two values of a type and returns a value of the same type)
mconcat takes a list of monoid values and mappends them into a single value

# Monoid Laws
mempty \`mappend\` x = x -> (identity function returns itself)
x \`mappend\` mempty = x -> (order doesn't matter)
(x \`mappend\` y) \`mappend\` z = x \`mappend\` (y \`mappend\` z) -> (order doesn't matter v2)

# Lists as Monoids
instance Monoid \[a] where -> Notice \[a] not \[] as Monoid requires a concrete type
    mempty = \[]
    mappend = (++) -> Currying in action as (++) takes two values
Notice how mappend is just function composition and mempty is just id
# What is a Monoid
Multiplication (\*) (Identity is 1)
Addition (+) (Identity is 0)
Lists (\[a]) (Identity is \[])
Or (||) (Identity is False)
And (&&) (Identity is True)

Product and Sum (newtypes of Monoid Typeclass as numbers can be monoids in different ways (+ and \*)
newtype Product a = Product {getProduct :: a}
    deriving (Eq, Ord, Read, Show, Bounded)

instance Num a => Monoid (Product a) where (When Monoid takes a value of Product a use these functions)
    mempty = Product 1
    Product x \`mappend\` Product y = Product (x \* y)

Sum is defined like Product and can be used in the same way but for (+)

# Any and All
newtype Any = Any {getAny :: Bool} deriving {Eq, Ord, Show, Read, Bounded}
instance Monoid Any where
    mempty = Any False
    Any x \`mappend\` Any y = Any (x || y)

All is defined similarly
instance Monoid All where
    mempty = All True
    All x \`mappend\` All y = All (x && y)

# Ordering Type
instance Monoid Ordering where
    mempty = EQ -> EQ is the identity
    LT \`mappend\` _ = LT
    EQ \`mappend\` y = y
    GT \`mappend\` _ = GT

Comparing string length, if EQ compare alphabetical order ("a" < "b")
lengthCompare :: String -> String -> Ordering
lengthCompare x y = (length x \`compare\` length y) \`mappend\` (x \`compare\` y)

Works since \`mappend\` keeps the left parameter unless it's EQ in which case it keeps right
Left most criteria are "more important" and kept if EQ is fulfilled otherwise it travels rightwards

```haskell
lengthCompare x y = (length x `compare` length y) `mappend` -- Checks for amount of vowels as second most important criteria
                    (vowels x `compare` vowels y) `mappend`
                    (x `compare` y)
    where vowels = length . filter (`elem` "aeiou")
```

# Maybe a 
```haskell
instance Monoid a => Monoid (Maybe a) where -- If a is a Monoid, Maybe a is also a Monoid
    mempty = Nothing
    Nothing `mappend` m = m
    m `mappend` Nothing = m
    Just m1 `mappend` Just m2 = Just (m1 `mappend` m2)
```

# First a and Last a
```haskell
newtype First a = First {getFirst :: Maybe a} deriving (Eq, Ord, Read, Show)
instance Monoid (First a) where
    mempty = First Nothing
    First (Just x) `mappend` _ = First (Just x) -- Returns first value when mappended if it's a Just value
    First Nothing `mappend` x = x -- If first value is nothing return second value
```

First returns the first Just value found in a list that could contain Nothing's
Last returns the last Just value found in a list that could contain Nothing's
map First $ \[Nothing, Just 7, Just 10] -> Just 7
map Last $ \[Nothing, Just 7, Just 10] -> Just 10
