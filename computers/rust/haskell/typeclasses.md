Typeclasses define behaviour and specify Types which can use said behaviour
- Eq -> Any type which can be equally compared can be of the Eq class
    - All Eq types use == or /= in their definition
- Ord -> Types that have an ordering
- Show -> Types that can be presented as strings
- Read -> Types that can be turned into non-strings
- Enum -> Types that can be enumerated
- Bounded -> Types that have an upper and lower bound (Tuples are bounded if the types inside are
- Num -> Types that can act like a number
- Floating/Integral -> Float/Double & Int/Integer
- Maybe Type -> Can either be one element or nothing, similar to empty lists
- Read -> Used for ReadS, result from reads function

Define classes with the class keyword where a is a Type of Eq typeclass
    class Eq a where
    (==) :: a -> a -> Bool
    (/=) :: a -> a -> Bool
    x == y = not (x /= y)
    x /= y = not (x == y)

Use instance (or derive) to make Types part (an instance) of Typeclass
You only have to define the minimum of functions when creating an instance (since == is used recursively with /= we don't have to define it here)
This is minimal complete definition for a typeclass
    data TrafficLight = Green | Red | Yellow
    instance Eq TrafficLight where
        Red == Red = True
        Green == Green = True
        Yellow == Yellow = True
        _ == _ = False

You can also make Typeclasses that are subclsses of other Typeclasses
Subclasses are just class constraints on class declarations
You can think of below as abc has to be an instance of Eq before being an instance of Num
    class (Eq abc) => Num abc where
    ...

    instance (Eq m) => Eq (Maybe m) where (All Maybe m's where m is part of Eq should be part of Eq too)
        Just x == Just y = x == y
        Nothing == Nothing = True
        _ == _ = False
