Troubleshoots syscalls
Commands make syscalls, very lowlevel

format which syscalls are displayed in: 
- processid syscall(syscall args) return value

examples:
- open(file_name, perms)=[[file-descriptor-number]]
- linux tracks files with numbers you can see the fds for each pid by doing ls -l /proc/pid/fd
- read(file_descriptor, read_result)=bytes_read

flags
- -e syscall_name (e.g. open/read) or even open=[[file-descriptor-number]]
	- -e trace=file_name (only includes syscalls that mention filenames)
- -f (shows subprocesses)
- -ff writes each process into a seperate file
- -p PID (open for a specific program using PID) (if program runs as root make sure you're root)
- -s str_size (only shows the first str_size of each string)
- -o output_file (sends to output file)
- -t shows when syscall happened to second, -tt shows to milisecond instead
- -T how long a syscall took to perform