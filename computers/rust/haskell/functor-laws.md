__ID SHOULD RETURN ITSELF__
fmap id = id -> If you map id over a function it should return the same function
id (identity function) is just (\x -> x)

__SECOND LAW__
Composing two functions and then mapping the result over a functor should be the same as first mapping one function over the functor and then mapping the other one

fmap (f . g) = fmap f . fmap g
fmap (f . g) F = fmap f (fmap g F)

