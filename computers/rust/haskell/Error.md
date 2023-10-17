Used to attach Error to values, monad
``` haskell
import Control.Monad.Error

instance (Error e) => Monad (Either e) where
	return x = Right x -- Right is the correct value, aka default context
	Right x >>= f = f x -- If Right apply func to x
	Left err >>= f = Left err -- If failure keep Left value and it's contents
	fail msg = Left (strMsg msg) -- strMsg aka error has to be part of Error             typeclass, such as strings
strMsg :: (Error e) => String -> a
```
