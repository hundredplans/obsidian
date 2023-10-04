```c++
for (Var; Condition; increment/decrement operator)
{
	// code block
}

for (s1;s2;s3) {
	// code block
}
```

s1 is executed once
s2 is the condition for when the for loop runs
s3 is executed after the code block has been executed (even for the last execution)

e.g.
```c++
int main(){
	for (int i=0, i <= 5, i++) {
		cout << i << "\n";
	}
	return 0;
}
```

Nested loops work exactly as you think they do

for-each is a special type of loop used exclusively to loop through data-sets
```c++
int myNumbers[5] = {10,20,30,40,50}
for (int i : myNumbers) {
	cout << i << "\n"
}
```