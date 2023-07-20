import System.Random


RandomGen -> Typeclass for types that can act as a source of randomness (Generating randomness)
Random -> Typeclass for things that can take on random values (e.g. True | False, 0 | 1 | 2..)

StdGen -> Of RandomGen, we can create one or tell system to assign one to us based on randomness

mkStdGen :: Int -> StdGen
mkStdGen -> Takes an integer and returns a random generator

random :: (RandomGen g, Random a) => g -> (a, g)
You must declare the type that random returns as it can be any Type
Returns a tuple of our random number and a textual representation of our generator
Change first type declaration parameter to change what Type is returned (unless specified in func it's used in)
    random (mkStdGen 100) :: (Int, StdGen) 
    random (mkStdGen 100) :: (Bool, StdGen)

randoms :: (RandomGen g, Random a) => g -> [a]
randoms' gen = let (value, newGen) = random gen in value:randoms' newGen
randoms -> Returns an infinite list based on the generator provided (use take to get values)
You can use type declaration to change what it returns
    take 3 $ randoms $ makeStdGen 42 :: [Bool]
    [True, True, False]

randomR :: (RandomGen g, Random a) :: (a, a) -> g -> (a, g)
randomR -> Take a tuple of values as the max and min bounds of the final random value produced and a gen

randomRs :: (RandomGen g, Random a) => (a, a) -> g -> [a]
randomRs -> Same as randomR but creates within an upper and lower bound

getStdGen :: IO StdGen
getStdGen -> Ask system for a random StdGen (generates for you)
Each time you run the program the result is different
Multiple getStdGen will give the same result in one program

    main = do
        gen <- getStdGen
        putStr $ take 20 (randomRs ('a', 'z') gen)

newStdGen :: IO StdGen
newStdGen -> Creates a new StdGen based on system time etc, and binds to IO
Also updates global getStdGen when used aswell as creating newGen
