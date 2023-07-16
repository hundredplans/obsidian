Specify which functions module should export at top

module Name (used to refer to module in script)
    ( func1
    , func2
    , func3
    ) where

Module has to be in the same folder as the program that's importing it
To access modules inside folder use 
    import FolderName.ModuleName
