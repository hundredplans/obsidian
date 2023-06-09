	 General
- Commands can be seperated using ; or \\n and can be preceded with any amount of whitespace
- sed counts lines countinously across files unless -i or -s

# Selecting Lines (Start of SCRIPT)
- NUM -> Match only NUM line in input
- $ -> Match last line of input or file if -i or -s
- /REGEXP/ -> Match lines which match specified regexp, / inside has to be escaped
- \\%REGEXP% -> Changes delimiter from / to % (can be changed to any character) 

## GNU Extensions
- START~STEPs/ -> Start on line START and match a line every STEP, 1~2 is odd lines
- /REGEXP/I -> Matches in a case-insensitive manner
- /REGEXP/M -> Enables ^ and $ to match start and end of lines, "\\\`" and "\\\'" does this natively

# Substitute
- 's/PATTERN/REPLACEMENT/'
- Replaces matched PATTERN with REPLACEMENT where PATTERN was found
- If /REPLACEMENT/ is empty '//' PATTERN found is removed, see below for removing multiple instances in one line
- /REPLACEMENT/g will match multiple times per line
- /REPLACEMENT/\\2 -> Employs [[regex-capture-groups]]

# Delete
- '/PATTERN/d' removes lines that match the pattern
