General
[[sed-selecting-lines-addresses]]
# General
- Commands can be seperated using ; or \\n and can be preceded with any amount of whitespace
- sed counts lines countinously across files unless -i or -s

# Commands
- Commands can be enclosed within {}, sed '/pattern/ {command1, command2;}' file.txt, useful for specifying one address range for multiple commands
## Delete
- '/PATTERN/d' removes lines that match the pattern
- sed 's/foo/bar/;1,4d' -> Delete lines 1-4

## Quit
- Standalone q sed 's/foo/bar/; q' file.txt will quit sed after command is processed
- sed 's/foo/bar/;5q' file.txt will quit sed after a specific line number

## Print
- Print to standard-output, sed '2,5p', typically used with -n

## Substitute
- 's/PATTERN/REPLACEMENT/FLAGS'
- Replaces matched PATTERN with REPLACEMENT where PATTERN was found
- If /REPLACEMENT/ is empty '//' PATTERN found is removed
- / Character or replacement can only be used if escaped
- \\n = \\d

### Flags
- g -> Match multiple times per line
- \\NUM -> Utilize [[regex-capture-groups]]
- & -> Reference to found PATTERN, e.g. 's/word/&s' turns word into words and 's/word/\\L&' converts whole word into lower case
- \\n -> Create a newline character
- \\t -> Create a tab character
- p -> Print modified line to output, typically all commands are run before print
- w FILE -> Write result to specified file
	- GNU Extensions supports two special values
	- w /dev/stderr writes to standard error
	- w /dev/stdout writes to STDOUT

#### GNU Extension
- \\L -> Convert replacement to lower case
- \\l -> Convert next character to lower case
- \\U -> Convert replacement to upper case
- \\u -> Convert new character to upper case
- \\E -> Terminate case convertion started by \\L and \\U, can also use opposite e.g. \\L is terminated by \\U as well as \\E
- e -> Execute REPLACEMENT as command then substitute output of command into input
- i, I -> Case-insensitive matching
- M, m -> Allows ^ and $ to function at start and end of regex

# Comments
- Use # in sed-script to denote comments, anything following is ignored