General Debugger
gdb allows you to debug any executable, displays very low-level information
--args to provide args
can be used on commands, such as sleep
e.g. 
	gdb --args sleep 20 -> Loads
	run -> To run the loaded executable

[[pwndbg]], [[lldb]] are better versions of this