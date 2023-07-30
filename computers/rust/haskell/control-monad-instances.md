import Control.Monad.Instances

instance Functor ((->) r) where
    fmap f g = (\x -> f (g x))

(->) r is a function that takes on parameter (think of r as equivalent to a in (a -> b)
instance Functor (r ->) where (If syntax allowed it)
    fmap f g = (\x -> f (g x))

fmap :: (a -> b) -> f a -> f b
fmap :: (a -> b) -> ((->) r a) -> ((->) r b)
fmap :: (a -> b) -> (r -> a) -> (r -> b)
