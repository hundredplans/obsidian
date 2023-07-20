import Control.Monad

when IO Bool -> Returns IO action if Bool true and returns return () if False
when :: Monad m => Bool -> m () -> m ()
when allows us to encapsulate if something then do some IO else return ()

forever IO -> Repeats IO action forever (so repeatedly asks for Input)
forM list func -> Same as mapM but parameters are swapped (personal preference)
