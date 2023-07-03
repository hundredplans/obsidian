# General
- 's/PATTERN/REPLACEMENT/FLAGS'
- Replaces matched PATTERN with REPLACEMENT where PATTERN was found
- If /REPLACEMENT/ is empty '//' PATTERN found is removed
- / Character or replacement can only be used if escaped
- \\n = \\d

## Flags
- \\NUM -> Utilize [[regex-capture-groups]]
- & -> Reference to found PATTERN, e.g. 's/word/&s' turns word into words and 's/word/\\L&' converts whole word into lower case
- \\n -> Create a newline character
- \\t -> Create a tab character

### GNU Extension
- \\L -> Convert replacement to lower case
- \\l -> Convert next character to lower case
- \\U -> Convert replacement to upper case
- \\u -> Convert new character to upper case
- \\E -> Terminate case convertion started by \\L and \\U, can also use opposite e.g. \\L is terminated by \\U as well as \\E
- i, I -> Case-insensitive matching
- M, m -> Allows ^ and $ to function at start and end of regex