# Single Patterns
- \* - 0 or more of the preceding match
- + - 1 or more of the preceding match
- ? - 0 or 1 of the preceding match
- . - Any character

- \[ab] - Match character a or b or ab
- \[a-z] - Match any character that's in the alphabet
- \[0-9] - Match characters 0 to 9 or any combination that does not repeat e.g. 45 but not 455

- \(ab) - Match character a and b, together
- ^ - Match the beginning of a line
- $ - Match the end of a line

- \[^abc] - Match any character that isn't a,b or c
- \[^n-p] - Match any character that isn't in n to p
	
- \\d can be used in place of any digit
- \\. for actual dots
- \\w - Equivalent to \[A-Za-z0-9_]
- \\s - Match any whitespace character
- Use the capital of \\w, \\s, \\d (\\W, \\S, \\D) to denote the opposite (non-alphanumeric character (such as punctuation), non-whitespace and non-digit character)

- \\b'one' - Will match every word of one preceded by a non-word character (non-letters, numbers or underscores)
- \\B'one' - Will match anything not bounded by a word (inside a word), e.g. **one**self but not **one**

- \<Input - Match Input only if it as the start of a word
- >Input - Match Input only if it as the end of a word

# Whitespace Characters
- \\t - Tab character
- \\n - New-line character
- \\r - Carriage return (Enter) or \<CR>
- \\v - Vertical tab (?)
- \\f - Form feed (page break, used in printers?)

# Repetitions
- a{3} - Matches character a 3 times exactly
- a{1,3} - Match no more than 3 times but less than 1
- .{2,6} - Match between 2 and 6 of any character
- a{2,} - Match at least 2 a characters

# Optionality
- .* & .+ -> 0 or 1 or more of any amount of characters before input string
- a+ -> 1 or more a's
- \[abc]+ -> 1 or more of any character a,b or c
- files? -> Can be file or files
- | or symbol

# Combo Patterns
- \.\*\"Input" - 0 or more of any amount of characters followed by input string
- .+"Input" - 1 or more of any amount of characters followed by input string- ^PATTERN$ - Has to match from the beginning to the end of the line exactly, this is called anchoring the regex
- \*? - Non-greedy match, only matches first instance of input string
- ^$ - Match start to end of string exactly
- \\b'one'\\b - Will match specifically one and not also words such as oneself
- \\w+\\b - Capture any entire word that is made of alpha-numeric characters
- wo\*rd - Can be woooord or word or wrd
- (,\d+) - Match a comma or any amount of digits together
- \[a-c0-2]\* - Match zero or more occurences of a,b,c,0,1,2 even if they repeat
- (a-c){3} - Grouped expressions can be treated as a unit

# Worthy of Study
```
'^-?\d+(,\d+)*(\.\d+(e\d+)?)?$' # Match any negative or positive digits with scientific notation, any amount of commas and a potential .
'(\d\s)?(\(?(\d{3}))[-\)]?\s?\d+((-|\s)?\d+)?' # My solution for matching phone numbers
'1?[\s-]?\(?(\d{3})\)?[\s-]?\d{3}[\s-]?\d{4}' # Online solution, ensure first capture group so it's better
((\w+)\.?(\w+))[\+\w]*@(.)* # My solution for matching emails
'^([\w\.]*)' # From start of string match one or more \w or . characters
[WE]/\w*\(\s\d{4}\):\s*at\s\w+\.\w+\.(\w+)\((.+):(\d+)\) # My solution to Problem 7 in RegexOne see [[learning-linux/regex/resources]]
```