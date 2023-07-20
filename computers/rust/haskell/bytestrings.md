import Data.ByteString

Regular strings are slow when reading from big files
Bytestrings are similar to lists but each element is 8 bits
A lot of function names are similar so do a qualified import


-- STRICT BYTESTRINGS --

There are strict and lazy bytestrings (remember lazy is like a promise something will happen)
Strict bytestrings reside in memory so you cant have infinite strict bytestrings
Likely to fill your memory up faster but less overhead (less thunks), useful for big lists

toChunks bytestring -> Converts a lazy bytestring to a strict one

-- LAZY BYTESTRINGS --
ByteStrings are stored as 
    Chunk String Empty (empty representing end of string)
    Chunk String (Chunk String Empty) 

import Data.ByteString.Lazy
Stored in chunks of 64K, evaluated 64K at a time

Word8 = 8bit int (0, 255) (part of Num typeclass)
    Int wraps around if you choose a number above 255
ByteString = Basically a list

pack :: [Word8] -> ByteString
Creates a ByteString out of ASCII code [99, 97, 110] = "can"

unpack -> Inverse of pack converts a ByteString to bytes
fromChunks bytestring -> Converts a strict bytestring to a lazy one

cons byte -> Puts a byte at the beginning of a bytestring and creates a new chunk
cons' byte -> Adds byte to a pre-existing chunk or creates a new one if necessary

empty -> Creates an empty byte string

Most standard functions that work on list are available for ByteStrings
Most IO functions are available for ByteStrings
If you use readFile with a strict bytestring it will read the whole file at once, watch out!
