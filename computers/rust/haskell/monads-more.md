All these Monads are part of the mtl package

# Writer
## Attaching Logs
Has a log value attached
(a,String)

applyLog appends the log message to the snd in the tuple and transforms first value
applyLog :: (a, [c]) -> (a -> (b, [c])) -> (b, [c])
applyLog (x,log) f = let (y,newLog) = f x in (y,log ++ newLog)

applyLog :: (Monoid m) => (a,m) -> (a -> (b,m)) -> (b,m) # Works for any type of Monoid
applyLog (x,log) f = let (y, newLog) = f x in (y,log `mappend` newLog)

## Writer Main
newtype Writer w a = Writer {runWriter::(a,w)} # Creates a tuple of (a,w) that can be outsourced with runWriter

instance (Monoid w) => Monad (Writer w) where
    return x = Writer (x, mempty) (mempty returns identity function)
    (Writer (x,v)) >>= f = let (Writer (y, v')) = f x in Writer (y, v `mappend` v')

There is no fail notation for Writer so if a pattern match fails in do an error is called

## Tell (Dummy Logs)
multWithLog :: Writer [String] Int
multWithLog = do
    a <- logNumber 3
    b <- logNumber 5
    tell ["Gonna multiply these two]
    return (a\*b)
output: [15, ["Got number: 3", "Got number: 5", "Gonna multiply these two"]]
