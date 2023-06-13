- Terminates process
- Allows you to send any sort of Unix signal
- kill TERM %PID 

# Options
- -STOP -> Sends [[SIGSTOP]]
- -KILL -> Sends [[SIGKILL]]
- -HUP -> Sends [[SIGHUP]]
- -0 -> Does not send a signal but gives a nonzero exit status if process does not exist