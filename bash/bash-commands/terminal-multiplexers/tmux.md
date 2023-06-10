# Core Tmux Concepts
## Sessions
- Sessions have windows
## Windows
- Windows have panes
- Windows are similar to tabs
## Panes
- Used to display multiple views in the same window

# tmux commands
- tmux -> Runs tmux or attaches to an existing session if one exists
- tmux a -> Attach to most recent session, use -t to specify
- tmux new -> Creates a new tmux sesion, use -t to name it
- tmux ls -> Shows current running sessions

# tmux options
- tmux -t session_name -> Used to specify session name

# tmux command line commands
- :kill-session -> Kills current session

# Ctrl-A/Ctrl-B
## Sessions
- d -> Detach from current session
- : -> Opens command line

## Windows
- c -> Create a new window
- p -> Jump to previous window
- n -> Jump to next window
- NUM -> Jump to NUM window
- , -> Rename current window

## Panes
- " -> Split current window horizontally
- % -> Splut current window vertically
- ARROW KEYS -> Moves through panes
- SPACE -> Change position of current pane, repeat for different formats
- z -> Zoom into current pane, repeat to unzoom