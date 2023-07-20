import System.Directory

getCurrentDirectory :: IO FilePath (String)
getCurrentDirectory -> Returns an IO String of the current directory

removeFile filename -> Removes file of specified name
renameFile filename newname -> Renames file to new name

copyFile :: fileName -> fileName -> IO ()
copyFile -> Copies file to a new name and returns an empty IO

doesFileExist :: IO Bool
doesFileExist filename -> Returns true if file exists
