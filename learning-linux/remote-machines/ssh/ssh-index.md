- Opens a secure shell
- Allows to execute commands remotely
- Used to work with remote machines
- Find server-side config in /etc/ssh/sshd_config

[[ssh-commands]]
[[port]]

# Options
- -L -> Specify IP and port
- -i FILE -> Select identity file

# Useful Knowledge
## Copying From Server
- cat localfile | ssh remote_server tee serverfile

## Why .ssh/config
- Found in ~/dotfiles/.sshconfig
- Can be used to set up your server configuration
- Other programs such as scp, rsync, mosh can read from it