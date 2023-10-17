If you want to assign a probability to each value in a list (value = non-deterministic value)
``` haskell
[(3, 0.5), (5, 0.25), (9, 0.25)]
[(3, 1%2), (5, 1%4), (9, 1%4)] -- Using [[Rational]]
```
