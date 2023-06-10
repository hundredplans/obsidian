- Print all files and directories recursively on seperate lines
- find \<path> \<expression> -exec \<command> {} \\;

# Options
- -type f / -type d -> Used to find only files and only directories respectively
- -mtime NUM -> Find files that have been modified in the last NUM days
- -exec command {} \\;-> Execute a command on each file found
- -name -> Find files with a specified name, use "\*.txt" to find all txt files
- -size +/-NUM -> Find files above or below a certain file size
- -iname -> Case insensitive search
- -print0 -> Print with NUL seperated characters