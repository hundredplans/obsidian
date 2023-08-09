import qualified Foldable as F

Foldable is a Typeclass used with Monoids
Uses Monoids to fold non-lists
Defines foldr, foldrl, foldr1, foldl1

Comparison of Prelude and Foldable foldr
foldr :: (a -> b -> b) -> b -> [a] -> b
F.foldr :: (F.Foldable t) => (a -> b -> b) -> b -> t a -> b

t (found in t a) is a Foldable type (e.g Maybe)
Both Prelude and Foldable work the exact same way for lists

__foldMap__
foldMap :: (Monoid m, Foldable t) => (a -> m) -> t a -> m
Takes a function that maps elements to Monoids then mappends the result into one Monoid
