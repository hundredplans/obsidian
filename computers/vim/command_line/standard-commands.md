# :q (Quit)
- Quits files, if you have multiple buffers open it quits the most recent one
- When you have no buffers it quits Vim
- You can force quit and not save changes with :q!

# :w (Write)
## Saves file (Writes), optionally can do:
- :w file_name, this will save the file to file_name in current directory
- The save is a copy, if you make changes after it will not affect the save

## Saving Selection
- If you're in [[visual-mode]] when you press :'<,'> will appear
- :'<,'>w file_name will only save the selection in a seperate file

# :h (Help)
- Help command, type relevant command after e.g. :h :q

# :qa (Quit All)
- Quit all files

# :e file (Edit)
- Edit specified file (open in current buffer)

# :ls (List)
- Lists open buffers

# :s (Substitute)
Replace name1 with name2 using sed syntax
- :s/name1/name2/g replaces all instances in line
- :s/name1/name2 replaces first instance in line
- :%s/name1/name2 replaces every occurence in file
- :%s/name1/name2/gc replaces every file in the whole file with a prompt
- :#,#s/name1/name2/g replaces all occurences on line # to #

# :sp (Split Horizontally)
- Splits window horizontally

# :vsp (Split Vertically)
- Splits window vertically

# :r (Append File)
- Retrieves text from a file or command output below cursor
- :r TEST will insert it's contents below the cursor line
- :r !ls will insert the output of ls and put it below the cursor

# :set (Change Options)
- :set ic - Ignores case
- :set hls - Turns on search highlighting found text
- :set is - Incremental search, as you type Vim matches to the content in real time

## Toggle On/Off
- :set inv - Toggle setting on/off
- :set no - Turn setting off
	- e.g. noic, invic will set ignore case off and toggle it respectively

 # :NUM (Move to Line)
 - Moves to specified line number