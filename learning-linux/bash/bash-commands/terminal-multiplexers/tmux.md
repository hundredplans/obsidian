# outside tmux commands
- tmux -> Runs tmux or attaches to an existing session if one exists
- tmux a -> Attach to most recent session, use -t to specify
- tmux new -> Creates a new tmux sesion, use -t to name it
- tmux neww -> Create a new window within a tmux session, if used outside it will create a new window in the most recent tmux session used
- tmux ls -> Shows current running sessions
- tmux source-file ~/.tmux.conf -> Sources tmux conf
- tmux kill-server -> Destroy all open tmux sessions and servers
- tmux kill-session -a -> Close all other tmux session except most recent
- tmux kill-session -t target -> Close specified session

# tmux options
- -t / -s session_name -> Used to specify session name
- tmux rename-session -t session_name new_name
-  -n STRING -> Assign name to the first window
- -d -> Detach session from its previous terminal
- -f PATH -> Specify config file, usually in ~/.tmux.conf

# tmux command line commands
- :kill-session -> Kills current session

# Ctrl-A/Ctrl-B
## General
- ? -> Lists all available commands
- w -> List running windows and sessions in an interactive manner but auto hide panes
- s -> Similar to w, auto-hides windows

## Sessions
- d -> Detach from current session
- D -> Choose which session to detach from
- : -> Opens command line
- $ -> Rename current session

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
- CTRL ARROW KEYS -> Resize pane in that direction by 1 character
- ALT ARROW KEYS -> Resize pane in that direction by 5 characters
- SPACE -> Change position of current pane, repeat for different formats
- z -> Zoom into current pane, repeat to unzoom

### Scroll Mode
- \[ -> Enter Scroll Mode, use arrow keys to scroll up or down in pane
- Ctrl-SPACE -> Start selection in scroll mode
- Alt-w -> Copy selected text

### 
- ] -> Paste text copied in Scroll Mode
- x -> Closes current pane after asking for confirmation
- o -> Logically traverses panes
- t -> Show a digital clock in the current pane
- ! -> Create a new window out of the current pane

# Other Shortcuts
- Ctrl D / exit-> Closes not detache current pane/window/session

### Scroll Mode
- SPACE scrolls down
- ENTER exits scroll mode if you haven't performed any scrolling yet otherwise it will bring you to where you started scroll mode

# Resources
https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/
https://www.computerhope.com/jargon/t/tmux.htm