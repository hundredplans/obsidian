- Opens a secure shell
- ssh user@ip/DNS
- Allows to execute commands remotely
- ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519 generates a keygen pair

# Useful Knowledge
## Copying From Server
- cat localfile | ssh remote_server tee serverfile