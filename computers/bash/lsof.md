List of open files
sudo lsof | grep "wanted info"
Lets you find out which process is using which file
lsof run alone shows you all files
run sudo lsof to get perms

e.g
sudo lsof | grep ":PORT .LISTEN" -> Outputs process number
kill PNUM