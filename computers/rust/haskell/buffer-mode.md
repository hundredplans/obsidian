Simple enumeration data-type
data BufferMode = NoBuffering | LineBuffering | BlockBuffering (Maybe Int)

NoBuffering -> Reads and sends each character immediatelly (slow as it constantly accesses disk)
LineBuffering -> Reads file line by line
BlockBuffering -> Allows you to specify buffer size in bytes, if Nothing is used reverts to system default

