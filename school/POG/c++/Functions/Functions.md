[[main]] is predefined
To call a function just do funcName();
functions are read from top to bottom so define functions accordingly

To pass data to a function, aka set the parameters (calling the function is providing args)
``` c++
void function(type var; type var;){
	// code goes here
}
```
Note the ; on the last var declared

To return values
``` c++
int myFunc(int x; int y;){
	return x + y
}

void swapNumbers(int &x; int&y)
	int z = x
	x = y
	y = z
```

Note how swapNumbers can take regular ints as parameters, then transform them into addresses and swap the values without giving a return value