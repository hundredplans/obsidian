# Single Patterns
- \* - 0 or more of the preceding match
- + - 1 or more of the preceding match
- . - Any character
- \[ab] - Match character a or b
- \[a-z] - Match any character that's in the alphabet
- \[0-9] - Match number 0 to 9
- \(ab) - Match character a and b, together
- ^ - Match the beginning of a line
- $ - Match the end of a line
- \\d can be used in place of any digit
- \\. for actual dots
- \[^abc] - Match any character that isn't a,b or c
- \[^n-p] - Match any character that isn't in n to p
- \\w - Equivalent to \[A-Za-z0-9_]



# Repetitions
- a{3} - Matches character a 3 times exactly
- a{1,3} - Match no more than 3 times but less than 1
- .{2,6} - Match between 2 and 6 of any character

# Optionality
- .* & .+ -> 0 or 1 or more of any amount of characters before input string
- a+ -> 1 or more a's
- \[abc]+ -> 1 or more of any character a,b or c
- ab?c -> String abc or ac, character b is optional
- files? -> Can be file or files

# Combo Patterns
- \.\*\"Input" - 0 or more of any amount of characters followed by input string
- .+"Input" - 1 or more of any amount of characters followed by input string
- ^PATTERN$ - Has to match from the beginning to the end of the line exactly, this is called anchoring the regex
- \*? - Non-greedy match, only matches first instance of input string