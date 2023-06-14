- Opens a secure shell
- Allows to execute commands remotely
- Used to work with remote machines
- Find server-side config in /etc/ssh/sshd_config

[[ssh-commands]]
[[port]]

# Options
- -L -> Specify IP and port
- -i FILE -> Select identity file
- -v -> Simple debug mode, on your end
- -vv -> Inform you on low level on server and your end
- -vvv -> Inform you on everything from both ends

# Useful Knowledge
## Copying From Server
- cat localfile | ssh remote_server tee serverfile

## Why .ssh/config
- Found in ~/dotfiles/.sshconfig
- Can be used to set up your server configuration
- Other programs such as scp, rsync, mosh can read from it

## Restarting Virtual Machine Server
- sudo [[service]] sshd restart
- Specifies sshd service to restart
- Use this to apply sshd_config changes