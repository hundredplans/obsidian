d([[movement-commands]]) - Combines to delete selection
- d(k) - Removes current line and one above
- d(j) - Removes current line and one below
- d(d) - Deletes current line
- d(w) - Removes next word
- d(e) - Removes end of current word
- d($) - Removs end of line
- When using with [[vim-repeating]] syntax is:
	nd([[movement-commands]])

c([[movement-commands]]) - Exactly like d but [[vim-entering-insert-mode]]
- c(c) - Removes current line and enters insert mode

C - Removes end of line and enters insert mode where cursor is
x - Deletes character
r - Replace current character
R - Replace current character and move cursor one character ahead while still replacing
