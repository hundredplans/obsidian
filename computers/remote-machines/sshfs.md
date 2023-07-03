- Used to mount a remote folder, allows to create files on remote server that transfer to local machine directly
- sudo sshfs -o OPTION1,OPTION2 user@ip:remote_mount_path local_mount_folder (run on local machine not server)
- If server is restarted you will have to remount, only works for current session

# Options
- -o -> Specifies options are present