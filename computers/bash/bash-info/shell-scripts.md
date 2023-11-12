Declare variables using foo=bar
Access variables using $foo
Do maths operations between ints using \[\*/+-\]
Use let to define variables with math let a=1+5
Use expr to print math results expr 5 + 2
To save the result of a command use backticks foo=\`ls -l | wc -l\`
See [[$]]
```sh
if [ condition ] then
	body
elif [ condition2 ] then
	body
else [ condition3 ]
	body
fi
```
To compare numbers use flags (eq, gt, lt, ge, le) e.g \[$foo -le $foo1\]
\= instead of == but != stays the same
&&, ||
Important that there's a space
=~ to do pattern matching eg $1 =~ ^\[0-9\]+\$ check if arg is an int
: to slice an array eg ${@:1:4} return args 1 to 4 from the @ array

to add 
n = $(n + 1))
# While Loops
``` sh
while [ $foo -le 5 ]
do
	# code goes here
done
```
There also exists Until Loops that are the opposite (while condition is false)
# For Loops
```sh
for i in arr
do
	# Code goes here
done
```

```sh
for ((i=0;i<10;i++))
do
	# Code goes here
done
```

# Case
```sh
case $foo in
	arg1)
	# code goes here
	;;
	arg2 | arg3)
	# code goes here
	*)
	# any other argument
	;;
esac
```
Ends with esac

# Functions
``` sh
func_name() {
	# code goes here
}
```
Called with func_name arg1 arg2, used within the function as $1, $2 etc