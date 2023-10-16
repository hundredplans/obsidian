(>>=) :: (Monad m) => m a -> (a -> m b) -> m b 
    Takes a out of context, applies function to transform it into b and puts it back in same context then returns

If we have a fancy value and a function that takes a normal value but returns a fancy value
how do we feed that fancy value into the function

Monads are just applicative functors that support >>= (bind)

# Binds
\>>= -> Takes a monadic value, a function that takes a normal value and returns a monadic value and applies function to monadic value

```haskell
>>= :: Maybe a -> (a -> Maybe b) -> Maybe b
>>= Nothing f = Nothing
>>= (Just x) f = f x
```

# Monad Typeclass
```haskell
class Monad m where # Should be class (Applicative m) => Monad m where

    return :: a -> m a -- Wraps value in Monadic context (same as pure, for maybe wraps a value in Just)

    (>>=) :: m a -> (a -> m b) -> m b -- Take a monadic value, lift it out of context, apply function and rewrap it in monadic context

    (>>) :: (Monad m) => m a -> m b -> m b -- Returns a value wrapped in a predetermined monadic context
    m >> n = m >>= \_ -> n

    fail :: String -> m a
    fail msg = error msg
```
## Maybe as a Monad
```haskell
instance Monad Maybe where
    return x = Just x
    Nothing >>= f = Nothing
    Just x >>= f = f x
    fail _ = Nothing
```

## Lists as a Monad
```haskell
instance Monad [] where
    return x = [x]
    xs >>= f = concat (map f xs) # Apply f, a function that takes a value and returns a list of values then concat
    fail _ = []
```

```haskell
[3,4,5] >>= \x -> [x,-x]
[3,-3,4,-4,5,-5]
```

```haskell
listOfTuples :: [(Int,Char)]
listOfTuples = do
    n <- [1,2]
    ch <- ['a','b']
    return (n,ch)
```

\[] is the failure state, if a \[] is fed into a lambda it will return a \[]

## MonadPlus
Used for Monads that are also Monoids

```haskell
class Monad m => MonadPlus m where
    mzero :: m a -- mempty (identity/failed monadic value)
    mplus :: m a -> m a -> m a -- mappend (binary)
```

For lists mzero represents a failed computation
For lists mplus joins two lists into one

### guard
guard :: (MonadPlus m) => Bool -> m ()
guard True = return () # Puts in minimal context that still succeeds
guard False = mzero # Acts as a failed value (Nothing for Maybe)

guard (5 > 2) :: Maybe ()
Just ()
```haskell
[1..50] >>= (\x -> guard ('7' `elem` show x) >> return x)
[7,17,27,37,47]
```
Puts value in monadic context with \>>=
guard returns a failed value if False and the minimal monadic context if it works (empty tuple)
\>> return x -> If guard fails returns Nothing (as guard returns Nothing or \[], in a >>= if a failed context is reached that's what will be returned), if it works returns the value wrapped in context

guard (5 > 2) >> return "cool"
\["cool"]
guard (1 > 2) >> return "cool"
\[]

Guard -> If boolean is False produce a failure, if boolean is True return a dummy tuple to continue the computation

```haskell
sevensOnly :: [Int]
sevensOnly = do
    x >= [1..50]
    guard ('7' `elem` show x)
    return x
```
Filtering in list comprehensions is the same as using guard
# do notation
```haskell
foo :: Maybe String
foo = do
    x <- Just 3 -- Takes a value out of a monadic context and assigns it a value
    y <- Just "!"
    Just (show x ++ y) -- Returns last value in a Monadic context
-- If any of the values above are Nothing the do computation fails
```

do is just syntactic sugar for chaining >>=
Every line in a do expression is a Monadic value
Not using <- is equivalent to writing >> (It will ignore the result of the previous value)
Last line is the value assigned to the do notation (unless a fail is computed, from a guard or such)

You can use pattern matching in do notation
```haskell
justH :: Maybe Char
justH = do 
	(x:xs) <- Just "Hello"
	return x
```

# Failure Contexts
Some Monads have a failure context, say Maybe (Nothing)
fail _ = Nothing
The error message is ignored if the program is to fail and produces a Nothing
When using pattern matching that can fail in do notation using Maybe with a failure context it will produce Nothing
```haskell
wopwop :: Maybe Char
wopwop = do
	(x:xs) <- Just ""
	return x
```
wopwop will result in Nothing
# Monad Laws
return x >>= f = f x
m >>= return = m
(m >>= f) >>= g = m >>= (\x -> f x >>= g) # Associativity
