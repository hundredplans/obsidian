import Control.Applicative

Typeclass Applicative
Beefed up Functors

Defines two methods but no implementation for them

pure
<\*>

class (Functor f) => Applicative f where -> Any variable that wants to be an instance of Applicative must be a functor
    pure :: a -> f a  -> Takes a value and wraps it in a function box
    (<\*>) :: f (a -> b) -> f a -> f b -> Pronounced apply, used typically in infix notation

__MAYBE APPLICATIVE__
instance Applicative Maybe where 
    pure = Just -> Equivalent to pure x = Just x
    Nothing <\*> _ = Nothing
    (Just f) <\*> something = fmap f something -> Map whatever is inside Just over another Functor (something)

Use pure when dealing with Maybe values in applicative context (<\*>)

__UNDERSTANDING APPLY__ (<\*>)
<\*> is left associative
pure (+) <\*> Just 3 <\*> Just 5
(Just (+) <\*> Just 3) <\*> Just 5
Just (3+) <\*> Just 5
Just 8

(<\$>) -> Is just fmap but as an infix
(<\$>) :: (Functor f) => (a -> b) -> f a -> f b

f <\$> x <\*> y <\*> z
(++) <\$> Just "John" <\*> Just "Voltra -> "JohnVoltra"

__LIST APPLICATIVE__
instance Applicative [] where
    pure x = [x] -> Takes a value and puts it in a singleton list
    fs <\*> xs = [f x | f <- fs, x <- xs] -> fs is a list of functions, xs is a list of values, creates a new list with each fs applied to each xs (not more than once)

[(+),(\*)] <\*> [1,2] <\*> [3,4]
[(1+),(2+),(1\*),(2\*)] <\*> [3,4]
[4,5,5,6,3,4,6,8]

__IO APPLICATIVE__


__APPLICATIVE LAWS__
pure f <\*> x == fmap f x
