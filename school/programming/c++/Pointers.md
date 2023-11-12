Store the [[Memory Address]] of a variable as it's value (note it's in hexadecimal form)
Special type of variable type that of string \* (stores a pointer to a string variable)
``` c++
string food = "Paipuri"
string *p = &food
cout << *p; // Output: "Paipuri" not a hexadecimal
cout << p // Output: 0x549546
```

You need to define the type of the variable the address points to aswell
Note \* not used when declaring a variable will give the value of an address
	Sort of the opposite of & which gets the memory address of a defined variable