import Control.Monad.Instances
A Monad with the context of a value that isn't present yet
also known as the Reader monad

``` haskell
instance Monad ((-> r)) where
	return x = \_ -> x
	h >>= f = \w -> f (h w) w
```
We get the result of (h w) and apply f to it
f returns a monadic value so we apply it to w
example
``` haskell
addStuff :: Int -> Int
addStuff = do
	a <- (*2)
	b <- (+10)
	return (a+b)
```
addStuff 3 -> (3\*2) + (3 + 10) -> 19

Function does the same thing
``` haskell
addStuff x = let
	a = (*2) x
	b = (+10) x
	in (a+b)
```

Gives all functions the values of passed parameters by using \>>= (lifts value out of monad context then places it back in)