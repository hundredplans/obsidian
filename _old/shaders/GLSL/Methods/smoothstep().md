- Takes two values (usually in [[normalized 0]] range) and a third value
- If third value is > than upper bound returns 1.0, < returns 0.0
- Otherwise it interpolates the third value in the range
```
smoothstep(x, y, z)
if z > y return 1.0;
elif x > z return 0.0
else; return y / z 
```