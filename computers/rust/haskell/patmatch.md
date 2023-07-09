# Pattern Matching/Guards
- You can define a function multiple times to give different result, get checked top down and if one value works the repeated functions don't get checked
    sayMe 1 = "One!"
    sayMe 2 = "Two!:"
    sayMe x = "Not a number between 1 and 5"

- Guards can be used as aswell to check if expressions evaluate to True
- If expression true return specified value
    | num <= 1 = "You're a one"
    | num <= 2 = "You're a two"
    | otherwise = "You're NOTHING you HEAR ME, YOURE NOTHING"

- The num can even be an expression instead
    | num / num2 <= 5 = "You're a 5/5"

# Introducing Where Bindings
- Think of where bindings as helper functions for a specific function
- You can even avoid repeating yourself with __WHERE__
    | func <= 10 = "Fuck you"
    | func <= 500 = "Great"
    where num * num2 (replace func with num * num2)

- You can go even further beyond!!
    | func <= somenum = "Fuck you"
    | func <= somenum2 = "Great"
    where num * num2
        somenum = 10
        somenum2 = 500

- These variables don't pollute the namespace as they're assigned in the function only
- You can also use where to pattern match itself ?!!?!?
    where num = arg1 \* arg2
        (somenum, someothernum, dad) = (20, 50, "dad?")

- You can even use where as function
calcNumbers: (RealFloat a) -> [(a, a)] ->  [a]
calcNumbers xs = [numadd n1 n2 | (n1, n2) <- xs]
    where numadd num1 num2 = num1 + num2

- Finally, you can nest where functions

# Introducing Let Bindings
- lambda function, all it is
- Don't span across guards, let you define variables locally
let area = w * h
    height = num * h
in area + height
- Form is let var = exp var2 = exp2 var3 = exp3 in exp (including all vars presumably)
- let bindings are expressions, you can put em anywhere
    - 4 * (let a = 9 in a * num)
- (let a=50;b=20;c=30 in a/b+c) + 100
- (let (a,b,c) = (1,2,3) in a/b+c) * 100 
calcNumbers: (RealFloat a) -> [(a, a)] -> [a]
calcNumbers xs = [numadd n1 n2 | (n1,n2) <- xs, let numadd = num1 + num2]
- You can omit __IN__ when defining a function with let

# Case Expressions
case expression of pattern -> result
                   pattern -> result
                   pattern -> result

case xs of [] -> error "This is an empty string my friend"
           (x:\_) -> x
- Similar but stronger than match/switch expressions
- If it fails error is returned
- Matches top first obviously then goes down
- if expression is true for pattern return specified result

describeList :: [a] -> String  
describeList xs = "The list is " ++ case xs of [] -> "empty."  
                                               [x] -> "a singleton list."   
                                               xs -> "a longer list."  
