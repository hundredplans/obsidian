<<<<<<< HEAD
General
=======
[[sed-selecting-lines-addresses]]
# General
>>>>>>> ddab8a483ab78c29726f2f19960ceefa11eea485
- Commands can be seperated using ; or \\n and can be preceded with any amount of whitespace
- sed counts lines countinously across files unless -i or -s

# Commands
- Commands can be enclosed within {}, sed '/pattern/ {command1, command2;}' file.txt
## Delete
- '/PATTERN/d' removes lines that match the pattern
- sed 's/foo/bar/;1,4d' -> Delete lines 1-4

## Quit
- Standalone q sed 's/foo/bar/; q' file.txt will quit sed after command is processed
- sed 's/foo/bar/;5q' file.txt will quit sed after a specific line number

## Print
- Print to standard-output, sed '2,5p', typically used with -n

## Substitute
- 's/PATTERN/REPLACEMENT/'
- Replaces matched PATTERN with REPLACEMENT where PATTERN was found
- If /REPLACEMENT/ is empty '//' PATTERN found is removed, see below for removing multiple instances in one line
- /REPLACEMENT/g will match multiple times per line
- /REPLACEMENT/\\2 -> Employs [[regex-capture-groups]]

# Comments
- Use # in sed-script to denote comments, anything following is ignored