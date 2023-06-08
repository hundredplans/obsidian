# Output Control
- --color -> Output matches in color
- -c -> Return count of lines found rather than output, use -v to return non-match count
- -l -> Print file/s where PATTERN matched, scan stops on first match
- -L -> Print file/s where PATTERN did not match, scan stops on first match
- -m NUM -> Stop output after NUM matching lines
- -o -> Print only matched part instead of whole line
- -q -> Do not write to STDOUT and exit with zero status if match is found, even if error was detected
- -s -> Supress error messages about nonexistent or unreadable files

# Output Prefix Control
- -n -> Prefix each line with the line output was found on in input
	- Usual output is **line-number:line-text**
	- If multiples files are searched will output **file-name:line-number:line-text**
	- If file is not in the same directory will specify **file-path:line-number:line-text**
- -b -> Prefix each line with offset to start of file, if -o is used prefixes with offset to match
- -H -> Prefix each line with file-searched, default if multiple files are searched
- -h -> Do not prefix each line with file-searched, default for one file or STDIN
- \--label=file.txt -> changes STDIN from grep to the file specified 
- -T -> Prefix each line with TAB if it doesn't already exist
- -u -> Strip \<CR> characters, useless on Unix, useful on Windows 
- -Z -> Output files with a null-delimiter instead of \\n, use grep -IZ with print0 and xargs -0
- -z -> Output lines with a null-delimiter instead of \\n

# Match Selection
- -E -> Evaluates as [[extended-regex]] rather than a simply RegEx
- -F -> Take PATTERN as string-literal (fixed strings) rather than RegEx, seperated by newlines
- -G -> Take PATTERN as basic RegEx expression (default setting)
- -P -> Interpet PATTERN as a Perl RegEx (it's different?)

# File Fuckery
- -r -> Searches recursively ignoring [[symlinks]]
- -R -> Searches recursively not ignoring [[symlinks]]
- -a -> Treat binary as text
- -d ACTION -> If input file is directory process it using ACTION
	- -d recursive -> Same as -r
	- -d skip -> Skip directories
	- -d read -> Default ACTION
- --exclude=GLOB -> Skip files that match GLOB
- --exclude-from=FILE -> Skip files that match line-seperated GLOBS read from file
- --exclude-dir=DIR -> Exclude directories who match pattern DIR
- -I -> Ignore binary files
- --include=GLOB -> Opposite of --exclude
- -U -> Treat files as binary, has no effect on non-Windows platforms

# Match Control
- -f FILE, -> Obtain PATTERN from file, can state multiple with space-seperated list
- -e PATTERN -> Search stated pattern, used to help with patterns that start with '-' or to specify multiple search patterns
- -w -> Select only line which form whole words (start, end and or whitespace seperated)
- -x -> Select only matches that match the whole line
- -i/-y -> Ignore case of input in PATTERN and FILE
- -v -> Find input that doesn't match

# Context Line Control
- -A NUM - After
- -B NUM - Before
- -C NUM - Before and After
- Print NUM lines before or after output

# Info Commands
- -V -> Prints grep version
- --help -> Prints grep help