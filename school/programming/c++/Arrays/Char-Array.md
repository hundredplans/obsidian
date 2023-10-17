Ends in null character (0) signifying the end of the array
To define -> 
``` c++
char text[80] = {"C++"}; // Creates null at end
char text[80] = {'C', '+', '+'}; // Doesn't create NULL at end
text[0] = 'C';
```
If defined all empty space will be replaced with null (0)
if define with char text\[] = {...} -> Will reserve space for defind chars + null

to save a string to another string you can't do arr1 = arr2 you need to copy each value individually as otherwise it's passed by reference