Defined using & (address of)
``` c++
string subject = "Math";
string &study = subject;
```
The memory address of study is set to that of subject
In the above example study is set to refer to subject, if you change study subject will change aswell
& gets the [[Memory Address]] of the set variable

To get the reference of an index in an Array (these are identical)
```c++
int x[10];
x+3
&x[3]
```