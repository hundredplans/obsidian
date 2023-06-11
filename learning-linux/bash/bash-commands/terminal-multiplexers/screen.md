- Write screen to launch
- New panes are empty, you have to select a window

# Specific Commands
- screen vim file -> Creates new window and launches vim, if done outside screen it will open 
- screen -list / -ls -> List running sessions on system
- screen -d -r -> Detach a screen session from the previous terminl and reattach to current
- screen -D -R -> Do what -d -r does then log off thte previous terminal and attach to the new terminal
- screen -r pid -> Reattach to pid session
- exit -> Kills session

# Ctrl-A Commands
- c -> Creates new window
- p -> Return to previous window
- 0-9 -> Go to window 0-9
- \" -> Lists all windows
- A -> Rename current window
- k / exit -> Terminates program

## Scrollback Mode
- \[ -> Enters scrollback mode, designed to copy text
- Space -> Start selection and stop selection
- Arrow Keys -> Select selection
- \] -> Paste selected text

###
- S -> Splits horizontally
- | -> Splits vertically
- tab -> Move to new pane
- Q -> Remove all panes except the current
- X -> Remove the current pane
- d -> Detach from current session
- : -> Open command line

# Resources
https://www.computerhope.com/unix/screen.htm
http://linuxcommand.org/lc3_adv_termmux.php