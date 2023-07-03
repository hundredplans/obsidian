- print -> Regular old print
- /pattern/ {command} -> If pattern is found in line execute command, default command is to print

# Operators
- ++/--var -> Count up every time pattern matches, no need to declare var
- var--/++ -> If b = var--/++ b is set to value one away from var value
- +=/\*%\*\*\^ -> These all work as well
- | += | -= | \*= | /= | %= | ^= / \*\*= | 
- | == | = | != | < | > | <= | >= |
- | && | || | ! |
- ? -> Same as if but placed after condition e.g. (a == b) ? b = fat, called a ternary operator
- -a / +a -> Add 1 to a, called a unary operator
- str1 = str2 str3 -> Concatenates two strings together
- in -> for i in array

# Arrays (Dictionaries)
- Can define array: {fruits\["mango"] = "yellow"; fruits\["orange"] = "orange"}
- delete fruits\["mango"]
- Accessing multi-dimensional arrays: array\["0,0"] = 100

# Control Statements
- if (condition) {action, action2} (curly braces unnecessary if only one action)
- if (condition) action else action2
- if (condition) action else if action2 (yes not elif)

# Files
- {"string" >/>>/| "file_name"} -> Creates output file if it doesn't exist
- |& -> e.g. (cmd |& getline output > 0) result is compared to > 0 while output is captured in output var 

# Loops
- { for (i = 1; i <= 5; i++) print i) } (C-style syntax)
- { i=1; while (i < 6) { print i, ++i } } -> Evaluates at start of loop
- { i=1; do {print i, ++i} while (i < 6) } -> Evaluates at end of loop
- BREAK, CONTINUE supported
- EXIT -> Stops script

# Regex
- string ~ regex -> Checks if string matches regex, can match each line with $0~regex
- string !~ regex -> Same as above

# Functions
- Note bit manipulation functions were avoided due to complexity
## Maths (head hurts)
- atan2(x, y) -> Returns arc tangent (da fuq) in radians
- cos(expr) -> Uses radians
- sin(expr) -> Uses radians
- exp(expr) -> expr^expr
- int(expr) -> Truncate to int value (floor)
- log(expr)
- rand() -> Return random number between 0 and 1
- sqrt(expr)
- srand(\[expr]) -> Use expr as seed value, if absent use time of day

## Strings
- asort(array) -> Sorts contents of array
- asorti(array, array2) -> Rearranges indices and stores them indices in array2, the original array is not modified at all
- gsub(regex, sub, string) -> Replace every instance of string with sub
- index(sub, str) -> Return position of sub if it's a substring of str, otherwise returns 0
- length(string) -> Output length of string in place of function in text, use $0 to get length of line
- match(string, /regex/ or string) -> Returns index of first longest match, 0 if not found
- split(str, array, regex/delimiter) -> Split string into fields and load fields into array, if regex is omitted uses FS delimiter instead
- printf(format, expr1, expr2) -> Format uses format specifiers, expr1, expr2 are inserted into the string, printf is also an advanced string that can process escape characters
	- %s -> string
	- %d/%i -> int
	- %f/%g -> float
	- %c -> char
	- %x/%X -> hexadecimal
	- %o -> octal
	- %e/%E -> scientific notation
	- %numFORMAT -> e.g. %10d prints a digit character with a field width of 10 characters
	- %0numFORMAT -> Pad with 0 instead of spaces
	- %-numFORMAT -> Pad behind character instead of in-front
 
- strtonum(str) -> Convert string into num, leading 0 = octal number, leading 0X = hexadecimal
- sub(regex, sub, string) -> Converts first instance, string is optional if not provided $0 is used
- substr(str, start, L) -> Return substring of str at start up to length L
- tolower(str) / toupper(str) -> Converts upper/lower to lower/upper case

## Time
- systime() -> Seconds since unix epoch
- mktime(datespec) -> Converts datespec string ("YYYY MM DD HH MM SS") into since unix epoch
- strftime(format, unix-epoch) -> Formats seconds into a date since unix-epoch
- https://www.tutorialspoint.com/awk/awk_time_functions.htm to see supported Time Formats

## Misc
- close(expr) -> Closes file that was previously opened inside awk
- fflush(\[output-expr]) -> Default flushes STDOUT (writes immediatelly), if output-expr is provided will flush for specified file/device
- getline \[file] -> Read next line and assign to $0, can provide file/command to read from
- next -> Stops execution and moves on to the next line
- nextfile -> Immediatelly stops processing current file and moves to next file
- system(cmd) -> Return exit status of command

## User-Defined Functions
- function name(arg1, arg2) {result = arg1 + arg2 return result}

# Environment Variables
## Standard
- ARGC -> Number of commands provided at command line (+1 as awk is one)
- ARGV -> Actual variables stored in format ARGV\[0] = awk\\nARGV\[1] = arg2
- CONVFMT -> Conversion value for floats for the input (%.6g)
- OFMT -> Conversion value for floats for the output (%.6g)
- ENVIRON -> Dictionary of environment variables (ENVIRON\["KEY"])
- FILENAME -> Current filename, undefined in BEGIN
- FS -> Delimiter for input (' ')
- OFS -> Delimiter for output (' ')
- NF -> Field number in current line
- NR -> Line number of current line
- FNR -> NR but relative to current file
- RS -> Input line seperator (\\n)
- ORS -> Output line seperator (\\n)
- RLENGTH -> When a match is performed set RLENGTH to length of matched substring, RLENGTH is 0 if no match was found
- RSTART -> When a match is performed sets RSTART to starting index of matched substring, RSTART is 0 if no match was found
- SUBSEP -> When accessing values inside an array e.g. SUBSEP=":" (default null) array\["key1":"key2]
- $0 -> Refers to the whole line
- $n -> Refers to specific field

## GNU Specific
- ARGIND -> Index of current file being processed (starts at 1) (stored in ARV so ARGV\[ARGIND] returns name of file)
- BINMODE -> Specifies binary mode
- ERRNO -> Holds the error status of the most recent file i/o operation (input/output)
- FIELDWIDTHS "num1 num2 num3" -> Change from using delimiters to specifying length of each field
- IGNORECASE = 0/1
- LINT = 0/1/fatal -> Behaves the same as --lint
- PROCINFO\[val] -> Allows to see the pid, uid, gid etc of the awk process [[procinfo-info]]
- TEXTDOMAIN -> Stores the name of the translation file used for awk, useless