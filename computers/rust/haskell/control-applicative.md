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
instance Applicative IO where
    pure = return -> Takes a value and return an Empty IO
    a <\*> b = do
        f <- a
        x <- b
        return (f x) -> Takes function and value out of IO context and returns function applied to value in IO context

    (<\*>) :: IO (a -> b) -> IO a -> IO b

__(->) r__
instance Applicative ((->) r) where
    pure x = (\_ -> x)
    f <\*> \x -> f x (g x)

pure :: a -> (r -> a) -> Return yourself 
pure 3 "blah" -> Returns 3

__ZipList__
instance ZipList where
    pure x = ZipList (repeat x)
    ZipList fs <\*> ZipList xs = ZipList (zipWith (\f x -> f x) fs xs)

Applies first function in fs to first value in xs, second func to second value etc
Resulting list is as long as the shorter of two lists

getZipList extracts a regular list out of a ZipList

__liftA2__
liftA2 :: (Applicative f) => (a -> b -> c) -> f a -> f b -> f c
liftA2 f a b = f <\$> a <\*> b
(a -> b -> c) -> (f a -> f b -> f c) -> Takes a normal binary function and promotes it to a function that operates on two functors
liftA2 (:) (Just 3) (Just [4]) -> : returns a new list with an element at the beginning

__sequenceA__
sequenceA :: (Applicative f) => [f a] -> f [a] -> Transforms a list of [Just 3, Just 5] to Just [3, 5]
sequenceA [] = pure []
sequenceA (x:xs) = (:) <\$> x <\*> sequenceA xs

sequenceA = foldr (liftA2 (:)) (pure [])

The two functions below are equivalent (and returns True if a list of booleans is true)
and $ map (\f -> f 7) [(>4),(<10),odd]
and $ sequenceA [(>4)(>10),odd] 7
sequenceA function transforms (Num a) => [a -> Bool] into (Num a) => a -> [Bool]
sequenceA [[1,2,3],[3,4]] -> [[1,3],[1,4],[2,3],[2,4],[3,3],[3,4]]

__APPLICATIVE LAWS__
pure f <\*> x == fmap f x
pure id <\*> v = v
pure (.) <\*> u <\*> v <\*> w = u <\*> (v <\*> w)
pure f <\*> pure x = pure (f x)
u <\*> pure y = pure ($ y) <\*> u
