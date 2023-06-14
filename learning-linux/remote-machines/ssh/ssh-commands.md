# Connecting To Server
- ssh user@ip
# SSH Key Pair
## ssh-keygen
### Options
- -o -> Store private key in new format (recommended)
- -b BITS-> Set bit length to BITS instead of default 1024
- -t TYPE -> Set encryption type, just use rsa
- -y -> Read a private key and spit out the public
- -f FILE -> Specify the file-name of the key file
## ssh-copy-id
- Installs an ssh-key as an authorized key, allows automated logins
### Options
- -i -> Look for keys in identity file, rather than ssh-add or default id folder
## ssh-agent
- Used to store private keys
## scp
- Used to copy large amounts of data between hosts
- scp LOCAL_FILE_PATH host_name:REMOTE_FILE_PATH, copies local file to remote file
## rsync
- Better scp, advertised as a fast, versatile and local file copying tool
- Identifies identical files in local and remote and doesn't copy