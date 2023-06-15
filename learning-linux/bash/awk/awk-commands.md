- print -> Regular old print
- printf -> Print with special formatting options available
- /pattern/ {command} -> If pattern is found in line execute command, default command is to print
	- ++var -> Count up every time pattern matches, no need to declare var

- < > -> Can use comparisons in string
# Functions
- length(string) -> Output length of string in place of function in text, use $0 to get length of line
- match(string, /regex/ or string)

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
- 