``` haskell
liftM :: (Monad m) => (a -> b) -> m a -> m b -- Transform monad a to monad b values, exactly the same as fMap but has a Monad constraint not Functor
liftM f m = m >>= (\x -> return (f x))
liftM f m = do
	x <- m
	return (f x)
```

``` haskell
ap :: (Monad m) => m (a -> b) -> m a -> m b -- Same as <*> but has Monadic context not Applicative
ap mf m = do -- Take two monadic values and return a Monadic value with first value applied to second value
	f <- mf
	x <- m
	return (f x)
[(+1), (*3), (+5)] `ap` [3,5] -> [4, 9, 8, 6, 15, 10]
```

Often when you have a Monad you can make an Applicative by just doing
pure = return
<\*> = ap
fmap = liftM (for Functors)

``` haskell
liftM2 :: (Monad f) => (a -> b -> c) -> f a -> f b -> f c
liftM2 f x y = f <$> x <*> y -- Note liftM3,4,5 exist
```

join is used to flatten monadic values e.g \[\[5, 6]] -> \[5, 6] or Just Just(9) -> Just 9
Maybe values get flattened as you think, if it's Nothing returns Nothing
Either is same as Maybe, returns Error if it's Left
For Writer values it mappends the log
For State values the two operations are run sequentially, the second one on the new state
``` haskell
join :: (Monad m) => m (m a) -> m a
join mm = do -- Take monadic value out of context and return it in context
	m <- mm -- This takes care of both values e.g mm = Just (Just 9)
	m
-- Two functions below are equivalent
m >>= f
join (fmap f m)
```

``` haskell
filterM :: (Monad m) => (a -> m Bool) -> [a] -> m [a]
keepSmall x  -- Implementation of a filter function
	| x < 4 = do
		tell ["Keeping " ++ show x]
		return x
	| otherwise = do
		tell [show x ++ " is too large, throwing it away"]
		return False
fst $ runWriter $ filterM keepSmall [9,1,5,2,10,3]
Output: [1,2,3]

powerset :: [a] -> [[a]] -- all possible sets aka [1, 2] -> [1, 2], [1], [2], []
powerset xs = filterM (\x -> [True, False]) xs -- for each value apply True or False
```

``` haskell
foldM :: (Monad m) => (a -> b -> m a) -> a -> [b] -> m a
```
Will return Nothing for example if the fold fails a predicate when the Monad is Just

``` haskell
<<= is the same as . for regular Functors
let f = (+1) . (*100)
f 4
-- Output: 401

let g = (\x -> return (x + 1) <=< (\x -> return(x * 100)))
Just 4 >>= g -- Take g out of monadic and apply 4
-- Output: 401

let f = foldr (.) id [(+1), (*100), (+1)] -- So this works and works the same way for Monads but with <=< and return instead of id, this allows you to replicate the same Monad x amount of times
f 1
-- Output: 201
```