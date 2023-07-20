Simple enumeration data-type
data IOMode = ReadMode | WriteMode | AppendMode | ReadWriteMode  

ReadMode -> Opened for reading
WriteMode -> Opened for writing
AppendMode -> Opened for appending
ReadWriteMode -> 
    Creates new file if it doesn't exist
    Opened for both read and write
    Existing file content is preversed
    New content can be written at any position in the file

