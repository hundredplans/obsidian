- file func -> Runs func in file
```
function func_name {
	func_result="some result" # global variable, usable outside func with $func_result
	return 55 # (0 for success, 1-255 for failure), returns exit status
	echo "$func_result" # print value to stdout, used to return
}
```