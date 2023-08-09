Use newtype when you want to take a type, wrap it in something and present it as a keyword
Faster than data keyword (defining a new type)
newtype can only have one value constructor (e.g. Maybe has two, Just or Nothing) with one field (arguments)

newtype ZipList a = ZipList {getZipList :: [a]}

Can use derive with newtype
newtype CharList = CharList {getCharList :: [Char]} deriving (Eq, Show)

CharList :: [Char] -> CharList
getCharList :: CharList -> [Char]

newtype Pair b a = Pair {getPair :: (a,b)}
instance Functor (Pair c) where
    fmap f (Pair (x,y)) = Pair (f x, y) -> Using pattern matching (Pair (x,y)) on a newtype

Notice the similarities -> Pair c becomes f
fmap :: (a -> b) -> Pair c a -> Pair c b
fmap :: (a -> b) -> f a -> f b
