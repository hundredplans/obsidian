```php
-- Directories --
$fd = $opendir("") #fd is dir id
if (!$opendir("")) {
	exit("Nie istnieje katalog")
}
while ($file = readdir($fd) !== false) # Returns the first file from opendir
{} # Will print out ., .. first

scandir($fd, 1) # Returns array of files inside dir
scandir($fd, 1) # Reverses sorting order
mkdir("dir_name", 0777, true) # Name, Perms, Recursive
rmdir("dir_name") # Has to be empty
getcwd() # Get name of current working directory
chdir('name_of_dir') # cd

-- Files (Reading) --
file_exists("file_name")
fopen("name", 'r') # Returns file id (r, w, x, a, w+, r+)
fclose($file)
fgets($file) # Returns the first string of the file
fread($file, 4096) # Specify the amount of bytes to read from the file
filesize("file_name") # Returns filesize
readfile("file_name") # Reads whole file as one string
file_get_contents("file_name") # Same as readfile

-- Files (Writing) --
fwrite($fd, "name") # Returns false if fails
file_put_contents("name", $data, FILE_APPEND) # Enum at the end optional 
fseek($file, offset, SEEK_END) # Changes where the line pointer is, last arg is enum
rewind($file) # Changes line pointer to the start
flock($file, LOCK_SH) # Reserves file for a specific script
unlink("name") # Deletes a file
fileatime("name") # Access time
filectime("name") # Creation time
filetype("name") # Is it a file or a directory
fileperms("name")
fileowner("name")
disk_free_space()
disk_total_space()

#LOCK_SH -> Blocks from writing
#LOCK_EX -> Total lock
#LOCK_UN -> Unlock
```