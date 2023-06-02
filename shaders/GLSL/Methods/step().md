- Takes two values (can be [[Vectors]]) and restricts to a [[normalized 0]] range
- If first value is less than second it returns 0.0, else it retuns 1.0 
```
step(x, y)
if x < y;
	return 0.0 
else; 
	return 1.0
```