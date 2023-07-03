# General
- sed counts lines countinously across files unless -i or -s
- Commands can be seperated using ; or a newline (not \\n) and can be preceded with any amount of whitespace
- Commands can be enclosed within {}, sed '/pattern/ {command1, command2;}' file.txt, useful for specifying one address range for multiple commands
- n -> Tells sed to move down one line
- \# Starts a comment until the next newline character
