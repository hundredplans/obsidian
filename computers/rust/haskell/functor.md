Functor is a [[typeclass.md]]
Used for things that can be mapped over

f is a type constructor that takes one type parameter (function that takes one arg)
How it's implemented
    class Functor f where
        fmap :: (a -> b) -> f a -> f b

    instance functor [] where (not [a] because fmap takes a func that takes a type)
        fmap = map

How Maybe is implemented (it's a Functor)
Functors want a type constructor that takes one type, not a concrete type (Maybe vs Maybe a)
    instance Functor Maybe where
        fmap f (Just x) = Just (f x)
        fmap f Nothing = Nothing

Implemented on custom Tree type
    instance Functor Tree where
        fmap f EmptyTree = Emptytree
        fmap f (Node x leftbranch rightbranch) = Node (f x) (fmap x leftbranch) (fmap x rightbranch)

You can partially apply functions to make them work for Functor's limitation of a type constructor that takes only one type
    instance Functor (Either a) where
        fmap f (Right x) = Right (f x)
        fmap f (Left x) = Left x
