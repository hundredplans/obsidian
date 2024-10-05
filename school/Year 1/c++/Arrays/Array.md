Uses [[Contiguous Memory Allocation]], must have a pre-defined size
```c++
type var_name[num of elements] = {arg1, arg2, arg3}
```
Similar to Haskell, Arrays can only contain one type of data
You need to define the number of elements when initialising an Array
``` c++
int Numbers[3] = {3, 7, 20}
```
Elements are accessed by index number
Strings are just char Arrays
You can change the value in an array by using the index number e.g. Numbers\[2] = 20

The size of an Array doesn't have to be defined, it will take up as much space as args
If an Array is defined at a higher size than the args inside, it will ocuppy the empty space regardless
```c++
string Words[] = {"Word2", "Word5"}
```