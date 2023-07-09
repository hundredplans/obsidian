# Syntax
## If Statements
- If statements require an else to function
- As if statements return a value surround them in () to work with that value
    - e.g. (if x > 20 then x else x + 50) + 20
- if Predicate then a (True) else b (False)
    - If predicate evaluates true return else return b
    - a and b are branches, they must have the same type
- if statements are just expression, you can put them anywhere
    - (if 5 > num then 6 else 5, 70) is completely valid as a pair tuple
    - 4 * (if 3 > num then 10 else 0) is also valid

## Infix Functions
- Define infix functions with backticks e.g. 5 `div` 20

## Other
- Surround operators in () when used outside of their functionality

## Comments
- Defined with -> -- example comment

## Order of Operations
- Functions have priority over operators

## Aliases
- xs@(x:y:xy) -> xs becomes an alias for x:y:xy
