import Control.Monad.State
Handles all state related business
A value that takes some state and returns a value with a new state
``` haskell
s -> (a, s) -- s is the state and a is the result of the computation
newtype State s a = State {runState :: s -> (a, s)}

instance Monad (State s) where
	return x = State $ \s -> (x, s)
	(State h) >>= f = State $ 
		\s -> let (a, newState) = h s
				  (State g) = f a
				  in g newState
```

# MonadState
typeclass inside Control.Monad.State, features two functions get & put
``` haskell
get = State $ \s -> (s,s) -- Take current value and present as result
put newState = State $ \s -> ((), newState) -- Replace current state with value using stateful function
stackNow <- get -- Literally gets value of current state
if stackNow == [1,3,5]
	then put [8,3,5] -- Replace the entire state with provided values
```

(>>=) :: State s a -> (a -> State s b) -> State s b

# Randomness with State
[[system-random]]
``` haskell
import System.Random
import Control.Monad.State

randomSt :: (RandomGen g, Random a) => State g a
randomSt = State random -- Makes randomSt part of State

threeCoins :: State StdGen (Bool,Bool,Bool)
threeCoins = do
	a <- randomSt
	b <- randomSt
	c <- randomSt
	return (a,b,c)
```