^u - Up half a page
^b - Up a whole page
	^d - Down one screen

G - End of buffer
- n(G) - Moves you to line n in buffer.
^g(n) - Moves n lines relative to current position away
- Also displays file status and line position at bottom
gg - Start of buffer

L - Lowest line on screen
M - Middle line on screen
H - First line on screen

^o - Jumps one behind in the [[Jumplist]]
^i - Jumps one ahead in the [[Jumplist]]
- When end of file is reached, it wraps back to the start unless wrapscan option has been disabled

% - Moves between matching parantheses even if they're not on the same line
- Useful for debugging programs with unmatched parantheses

zz - Shift current line to center of screen
zt - Shift current line to top of screen
zb - Shift current line to bottom of screen
z- - Like zb but moves cursor to start of line
z\<CR> - Like zt but moves cursor to start of line