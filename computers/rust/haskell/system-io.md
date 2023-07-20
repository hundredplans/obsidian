import System.IO

openFile :: FilePath -> IOMode -> IO Handle (FilePath is an alias for String)
openFile path IOMode -> Opens file located at path (relative to script or absolute) in IOMode

Handle -> Data type that provides functionality for reading/writing from file, can roughly represent an open file

hGetContents Handle -> Get contents (IO String) out of a Handle
hClose Handle -> Close a Handle (from an open file) (returns an IO action that closes the file technically)

withFile :: FilePath -> IOMode -> (Handle -> IO a) -> IO a
withFile -> Takes a path, IO mode and a function (it provides Handle argument for) to apply while contents are opened, then closes the file for you

    withFile' path mode f = do
        handle <- openFile path mode
        result <- f handle
        hClose handle
        return result

All work like their counterparts but take a Handle as an argument (operate on file not STDIN/STDOUT)
hGetLine
hPutStr
hPutStrLn
hGetChar

readFile :: FilePath -> IO String
readFile -> Closes and opens file automatically, often used to assign contents of string to var
Below acts like cat
    main = do
        contents <- readFile "file.txt"
        putStr contents

writeFile :: FilePath -> String -> IO ()
writeFile -> Takes a path to a file and writes contents, if it already exists, erases data
    main = do
        contents <- readFile "file.txt"
        writeFile "filecaps.txt" (map toUpper contents)

appendFile :: FilePath -> String -> IO ()
appendFile -> Same as writeFile but doesn't erase data if file already exists

hSetBuffering :: Handle -> BufferMode -> IO ()
hSetBuffering Handle BufferMode -> Controls how many bytes are read at a time for Handle

hFlush :: Handle -> IO ()
hFlush handle -> Flushes buffer of handle
    After every line for LineBuffering
    After every n bytes with BlockBuffering
    After flushing data is available to other programs that are running

openTempFile directory FileName -> Open temp file in specified directory with FileName (string)
    When you create a temp file it will be assigned a name + some random string of letters
    openTempFile returns an IO containing a tuple, IO (tempName, tempHandle)
