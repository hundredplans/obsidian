
# Awk Structure
```
Execute AWK Commands from BEGIN
Read a line from input stream
Execute AWK Commands on line from BODY
Repeat (2, 3) if not end of file
Execute AWK Commands from END
```

## BEGIN
- BEGIN {awk-commands}
- Good for initializing variables as it executes once at the start
- Optional
## BODY
- /pattern/ {awk-commands}
- Applies on every input line
- You can have multiple bodies in one command
## END
- END {awk-commands}
- Optional