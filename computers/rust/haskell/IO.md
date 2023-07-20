I/O stands for Input/Output
You need to compile your programs to perform I/O

To print to the terminal use
Returns an IO action that has a result type of ()
    putStrLn :: String -> IO () 
    putStrLn String 

IO Actions always have a side-effect, if it's not needed an empty tuple (unit) is used

We use do to chain together IO actions into one IO action that has the return type of the last IO action in the chain
you can use do with one IO action to no effect (then do return () == then return ())
We can use <- to store the result of a function in a variable
getLine returns user input 
    main = do
        putStrLn "Hello, what's your name"
        name <- getLine (getLine :: IO String, types name as String)
        putStrLn ("Hey " ++ name ++ ", you rock!")

Except for the last line each line in a do block can be bound with <-
Use <- for IO and use let to bind pure expressions

return is used to wrap a pure action into an IO
You can use <- to bind return values to a name (name <- return getLine -> name :: IO String
You can think of <- as the opposite of return, unwrapping an IO value in contrast to wrapping it
Since every if needs two values of the same type you can use return () to return nothing wrapped in IO

putStr -> Same as putStrLn but doesn't end with a \n so you can chain them into one line
putChar -> prints a Char
print is equivalent to putStrLn . show (used by GHCI when using Enter with a value)
Use print for all types except Strings as it adds quotes to strings while putStrLn doesn't
getChar -> Gets a char from user input, if used for user input it repeats for each char typed (getChar :: IO Char)
getLine -> Get line from STDIN
getConents -> Read everything from STDIN until EOF (getContents :: IO String)

sequence -> Creates an IO actions out of multiple smaller IO actions
sequence :: [IO a] -> IO [a]
    main = do
        rs <- sequence [getLine, getLine, getLine]
        print rs
-- Same as below
    main = do
        a <- getLine
        b <- getLine
        c <- getLine
        print [a,b,c]

mapM func list -> Maps the function over the list then sequences it
mapM_ func list -> Does what mapM does but throws away the result

interact (String -> String) -> Takes a function that returns a String as a parameter and returns an IO action that takes STDIN, runs the function then prints out the function's result

    main = interact shortLinesMatter

    shortLinesMatter:: String -> String
    shortLinesMatter = 
        let allLines = lines input
            shortLines = filter (\line -> length line < 10) allLines
            result = unlines shortLines
        in result
-- Same as below (Where lines is input received and result is printed)
    main = interact $ unlines . filter ((<10) . length) . lines
    
