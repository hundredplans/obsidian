# Core Tmux Concepts
## Sessions
- Sessions have windows
## Windows
- Windows have panes
- Windows are similar to tabs
## Panes
- Used to display multiple views in the same window

# outside tmux commands
- tmux -> Runs tmux or attaches to an existing session if one exists
- tmux a -> Attach to most recent session, use -t to specify
- tmux new -> Creates a new tmux sesion, use -t to name it
- tmux ls -> Shows current running sessions

# tmux options
- tmux -t session_name -> Used to specify session name
- tmux -s session_name -> Also specifies session name
- tmux rename-session -t session_name new_name

# tmux command line commands
- :kill-session -> Kills current session

# Ctrl-A/Ctrl-B
## General
- ? -> Lists all available commands

## Sessions
- d -> Detach from current session
- D -> Choose which session to detach from
- : -> Opens command line

## Windows
- c -> Create a new window
- p -> Jump to previous window
- n -> Jump to next window
- NUM -> Jump to NUM window
- , -> Rename current window
- w -> List new windows and jump between with arrow keys

## Panes
- " -> Split current window horizontally
- % -> Splut current window vertically
- ARROW KEYS -> Moves through panes
- SPACE -> Change position of current pane, repeat for different formats
- z -> Zoom into current pane, repeat to unzoom
- \[ -> Enter Scroll Mode, use arrow keys to scroll up or down in pane
- x -> Closes current pane after asking for confirmation
- o -> Logically traverses panes

# Other Shortcuts
- Ctrl D / exit-> Closes not detache current pane/window/session

### Scroll Mode
- SPACE scrolls down
- ENTER exits scroll mode if you haven't performed any scrolling yet otherwise it will bring you to where you started scroll mode

# Resources
https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/
https://www.computerhope.com/jargon/t/tmux.htm