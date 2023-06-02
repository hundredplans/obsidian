# Single Patterns
- \* - 0 or more of the preceding match
- + - 1 or more of the preceding match
- . - Any character
- \[ab] - Match character a or b
- \[0-9] - Match number 0 to 9
- \(ab) - Match character a and b, together
- ^ - Match the beginning of a line
- $ - Match the end of a line

# Combo Patterns
- \.\*\"I" - 0 or more of any character followed by input string
- ^PATTERN$ - Has to match from the beginning to the end of the line exactly, this is called anchoring the regex
- \*? - Non-greedy match, only matches first instance of input string